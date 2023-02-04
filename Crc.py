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
    crcStr = "0x{:02x}".format(crc)
    longitudCrc = len(crcStr)
    if longitudCrc == 5:
        crcStr = crcStr[0:2] + "0" + crcStr[2: ]
    elif longitudCrc == 4:
        crcStr = crcStr[0:2] + "00" + crcStr[2: ]
    
    return crcStr

# print(crc16_ccitt("e421c0a10000007f1480fa0637d43bcfa77fb852caac7c54da2be8d3bee0"))

# e40ec0a10000f0390101387ee3
#387e


############## Datos Para Calcular CRC ###################

### dst ### length ### src ###    cmd    ###   ERD    ###  
#    C0       XX        E4       XX XX        XX XX             
