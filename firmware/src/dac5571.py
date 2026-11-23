from machine import I2C, Pin
from micropython import const

ADDRESS = const(0x4C)
ENABLE_MASK = const(0x00)
DISABLE_MASK = const(0x30)


class DAC5571:

    def __init__(self, i2c: I2C):
        self.i2c = i2c
        self.disable()

    def set(self, val: int):
        val = 0 if val < 0 else val
        val &= 0xFF
        ms = ((val & 0xF0) >> 4) | ENABLE_MASK
        ls = (val & 0x0F) << 4
        self._write_dat(bytearray([ms, ls]))

    def disable(self):
        self._write_dat(bytearray([DISABLE_MASK, 0]))

    def _write_dat(self, buf):
        self.i2c.writeto(ADDRESS, buf)


class VMControl(DAC5571):
    def __init__(self, i2c: I2C, enable_pin: int):
        super().__init__(i2c)
        self.en = Pin(enable_pin, Pin.OUT, value=0)  # Default to disabled
        self.voltage = 0

    def set_voltage(self, voltage: int):
        # Vin = 15.1 - 3.44*Vdac, solve for Vdac:
        # Vdac = (15.1 - Vin) / 3.44
        vdac = (15.1 - voltage) / 3.44
        # Scale to 8-bit DAC value (0-255)
        dac_value = int((vdac / 3.27) * 255) - 2
        self.set(dac_value)
        self.voltage = voltage

    @property
    def enabled(self):
        return self.en.value() == 1

    @enabled.setter
    def enabled(self, value: bool):
        self.en.value(1 if value else 0)
