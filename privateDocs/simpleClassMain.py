import board
import busio
import adafruit_lis3dh
from ProjectBase import ProjectBase

#############################################################################
# Accelerometer wrapper class
class Accelerometer:
    def __init__(self, i2c:busio.I2C) -> None:
        # generally, any time you create your own class which uses
        # an I2C device, you should pass the I2C object to it instead
        # of calling `board.I2C()`.
        self.lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)
        self.lis3dh.range = adafruit_lis3dh.RANGE_4_G

    @property
    def acceleration(self) -> tuple[float, float, float]:
        return self.lis3dh.acceleration

#############################################################################
# Main project class
class MyProject(ProjectBase):
    
    def setup(self) -> None:
        self.sayAtStartup("Setting up the project...")

        self.i2c = board.I2C()  # Initialize I2C
        self.accelerometer = Accelerometer(self.i2c)

    def loop(self) -> None:
        print( f"Acceleration: {self.accelerometer.acceleration}" )


#############################################################################
if __name__ == "__main__":
    project = MyProject(verbose=True)
    project.run()
