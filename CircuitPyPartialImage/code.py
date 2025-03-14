from TerrainTronics.Main import MainManager
main = MainManager()

from adafruit_simplemath import constrain

targetAngle = main.addControlVariable( "angle", "Servo Angle", min=20, max=160, kind="int" )
targetColor = main.addControlVariable( "color", "Pixel Strip Color", kind="RGB", startingValue=(255,0,0) )

caernarfon = main.addCaernarfon( "WemosS2Mini", neoPixelCount=9 )
caernarfon.initServo(1)

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
DISPLAY_WIDTH, DISPLAY_HEIGHT = 128, 32
display = main.i2cFactory.addDisplay_SSD1306(DISPLAY_WIDTH, DISPLAY_HEIGHT, caernarfon.i2c)
display.fill(0)
display.show()

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

    # clear the pixel we set last loop
    # setDisplayPixel( 0, displayTargetPixel )
    display.fill(0)
    
    # determine new location - wrapping based on cycle PLUS joystick position
    displayTargetPixel[0] = int(main.cycle + nx*DISPLAY_WIDTH) % DISPLAY_WIDTH
    displayTargetPixel[1] = int(main.cycle + ny*DISPLAY_HEIGHT) % DISPLAY_HEIGHT
    setDisplayPixel( 1, displayTargetPixel )
    
    # set LED on QTRotaryEncoder - targetColor changed via Web UI
    qtr.pixel.fill(targetColor.value)
    qtr.updateStemmaEncoder()
    
    # determine servo angle
    s1angle = constrain( 
            targetAngle.value + ( (ny * 40) if nunchuk.buttons.C else 0),
            20, 160
        )
    
    caernarfon.servo1.angle = s1angle
    if main.cycle % 10 == 0:
        display.text(f'{main.cycle} {s1angle}', 0, 0, 1 )
    display.show()

main.addTask( loop )

webServer = main.addBasicWebServer()

print( "calling main.run" )
main.run()