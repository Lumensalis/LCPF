import time, rainbowio
from TerrainTronics.Caernarfon import CaernfarfonCastle
from TerrainTronics.I2C.QtRotaryEncoder import QtRotary

caernarfon = CaernfarfonCastle( "WemosS2Mini", neoPixelCount=9 )
caernarfon.initServo(1)
qtr = QtRotary(caernarfon.i2c)

cycle = 0
cyclesPerSecond = 40

while True:
    cycle += 1
    color = rainbowio.colorwheel(cycle)
    servoAngle = 20 + (cycle % 120)   # 20 - 160
    
    caernarfon.servo1.angle = servoAngle
    caernarfon.pixels.fill(color)
    caernarfon.pixels.show()
    qtr.updateStemmaEncoder()

    time.sleep( 1.0 / (cyclesPerSecond *1.0) )