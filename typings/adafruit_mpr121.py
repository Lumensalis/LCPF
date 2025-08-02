import busio
class MPR121:
    def __init__(self, i2c:busio.I2C) -> None:  
        self.i2c = i2c
        self._touched = 0

    def touched(self) -> int:
        pass
        
