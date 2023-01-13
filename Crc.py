def crc16_ccitt(data_hex):
    data = bytearray.fromhex(data_hex)
    poly = 0x1021
    crc = 0x1021
    for byte in data:
        for i in range(8):
            bit = (byte >> (7-i) & 1) == 1
            c15 = (crc >> 15 & 1) == 1
            crc <<= 1
            if c15 ^ bit:
                crc ^= poly
    crc &= 0xffff
    return hex(crc)


print(crc16_ccitt("C00BE4A000F039"))