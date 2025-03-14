
from TerrainTronics.Demos.CaernarfonLavaLights import demoMain

print( "running demo" )
demoMain()

print( "demo complete" )


import time, rainbowio  #type: ignore

from TerrainTronics.Main import MainManager
main = MainManager()

targetAngle = main.addControlVariable( "angle", "Servo Angle", min=20, max=160, kind="int" )
targetColor = main.addControlVariable( "color", "Pixel Strip Color", kind="RGB" )

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

    qtr.pixel.fill(targetColor.value)
    qtr.updateStemmaEncoder()
    caernarfon.servo1.angle = targetAngle.value

main.addTask( loop )

webServer = main.addBasicWebServer()

print( "calling main.run" )
main.run()