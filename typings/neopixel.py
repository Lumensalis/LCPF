from __future__ import annotations
import microcontroller
GRB:str="grb"

class NeoPixel(object):
    def __init__(self, pin: microcontroller.Pin, pixelCount: int,
                  pixel_order: str = GRB, brightness: float = 1.0
                  #, **kwds 
                  ) -> None:
        pass