import busio

from typing import Optional, Iterable, TypedDict, TYPE_CHECKING
class TLV493D:
    def __init__(self, i2c:busio.I2C) -> None:
        pass

    magnetic: tuple[int, int, int]