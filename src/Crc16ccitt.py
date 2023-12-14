def crc16_ccitt(data_hex:str) -> str:
    """
    Realiza el cálculo del crc16 ccitt
    
    Args:
        data_hex (str): Trama a calcular el crc
        
    Returns:
        str: crc calculado
    """
    data = bytearray.fromhex(data_hex)
    poly = 0x1021
    seed = 0x1021
    for byte in data:
        for i in range(8):
            bit = (byte >> (7-i) & 1) == 1
            c15 = (seed >> 15 & 1) == 1
            seed <<= 1
            if c15 ^ bit:
                seed ^= poly
    seed &= 0xffff
    crcStr = "{:04x}".format(seed)
    
    return crcStr