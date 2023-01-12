import libscrc
from Crc import Crc16, Calculator

crc16 = libscrc.ccitt(b'0xE2C00BE4A000F039')
calculator = Calculator(Crc16.CCITT)


print(crc16)