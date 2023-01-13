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
    crcStr = str(hex(crc))
    # crcLower = crcStr[2:4]
    # crcHigher = crcStr[4:6]
    # CrcCalculated = crcLower + " " + crcHigher
    return crcStr



############## Datos Para Calcular CRC ###################

### dst ### length ### src ###    cmd    ###   ERD    ###  
#    C0       XX        E4       XX XX        XX XX             



# print(crc16_ccitt("C00BE4A000F039"))