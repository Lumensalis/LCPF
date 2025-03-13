#type: ignore
import time, rainbowio  

from TerrainTronics.Main import MainManager
main = MainManager()

targetAngle = main.addControlVariable( "angle", "servo 1 angle", min=20, max=160, kind="int" )
targetColor = main.addControlVariable( "color", kind="RGB" )

caernarfon = main.addCaernarfon( "WemosS2Mini", neoPixelCount=9 )
caernarfon.initServo(1)

def encoderChanged(delta): 
    targetAngle.move( delta )
    print( f"targetAngle now {targetAngle.value}")
    
qtr = main.adafruitFactory.createQTRotaryEncoder(caernarfon.i2c)
qtr.onMove( encoderChanged )

def loop():
    color = rainbowio.colorwheel(main.cycle)
    caernarfon.pixels.fill(color)
    caernarfon.pixels.show()

    qtr.pixel.fill(color)
    qtr.updateStemmaEncoder()
    caernarfon.servo1.angle = targetAngle.value

main.addTask( loop )

webServer = main.addBasicWebServer()

print( "calling main.run" )
main.run()