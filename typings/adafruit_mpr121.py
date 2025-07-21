class MPR121:
    def __init__(self, i2c):
        self.i2c = i2c
        self._touched = 0

    def touched(self):
        return self._touched
