from TerrainTronics.Main import MainManager
main = MainManager()

from adafruit_simplemath import constrain

#############################################################################
# ControlVariables are used to specify logical inputs which have their
# values published to the WebUI and can be modified
# by various control inputs (encoder movement, WebUI, ... )

targetAngle = main.addControlVariable( "angle", "Servo Angle", min=20, max=160, kind="int" )
targetColor = main.addControlVariable( "color", "Pixel Strip Color", kind="RGB", startingValue=(255,0,0) )

#############################################################################
# Add a CaernarfonCastle
caernarfon = main.addCaernarfon( neoPixelCount=9, servos=1 )

#############################################################################
# I2C devices 

# add an Adafruit QTRotaryEncoder, and set it up to adjust targetAngle
qtr = main.adafruitFactory.createQTRotaryEncoder(caernarfon.i2c)
def encoderChanged(delta): 
    targetAngle.move( delta )
    print( f"targetAngle now {targetAngle.value}")

qtr.onMove( encoderChanged )

# add a WII Nunchuk
nunchuk = main.adafruitFactory.createNunchuk(caernarfon.i2c)

# add a display
display = main.i2cFactory.addDisplay_SSD1306(128, 32, caernarfon.i2c)

def setDisplayPixel( state, location ):
    display.pixel( location[0], location[1], state )

#############################################################################

displayTargetPixel = [0,0]

def loop():
    global displayTargetPixel
    
    # nx and ny will be the WII Nunchuck joystick position from -1.0 to 1.0
    nx, ny = nunchuk.scaledJoystick
    
    # change color on neopixel strip - 
    #  main.cycle increments automatically on every loop
    color = main.wheel( main.cycle + nx*30 )
    caernarfon.pixels.fill(color)
    caernarfon.pixels.show()

    # set LED on QTRotaryEncoder - targetColor changed via Web UI
    qtr.pixel.fill(targetColor.value)
    qtr.updateStemmaEncoder()
    
    # update servo - angle must stay within range to avoid exceptions
    s1angle = constrain( 
            targetAngle.value + ( (ny * 40) if nunchuk.buttons.C else 0),
            20, 160
        )
    caernarfon.servo1.angle = s1angle
    
    #update display
    updateTextEveryNCycles = 10
    if main.cycle % updateTextEveryNCycles == 0:
        display.fill(0)
        display.text(f'{int(main.cycle/updateTextEveryNCycles)} {int(s1angle)}', 0, 0, 1, size=2 )
    else:
        # clear the pixel we set last loop
        setDisplayPixel( 0, displayTargetPixel )

    # determine new location - wrapping based on cycle PLUS joystick position
    displayTargetPixel[0] = int(main.cycle + nx*display.displayWidth) % display.displayWidth
    displayTargetPixel[1] = int(main.cycle + ny*display.displayHeight) % display.displayHeight
    setDisplayPixel( 1, displayTargetPixel )
    
    display.show()

main.addTask( loop )

webServer = main.addBasicWebServer()

print( "calling main.run" )
main.run()