import Crc

def ReadErd(strERD):
    bitInit = "E2"
    dst = "C0"
    src = "E4"
    cmd = "A000"
    ERD = str(strERD)
    bitStop = "E3"
    longitud = int(((len(bitInit + dst + src + cmd + ERD + bitStop)) + 6) / 2)
    lenght = "0x{:02x}".format(longitud)
    lenght = str(lenght[2: ])   
    FrameToCalculateCrc = dst + lenght + src + cmd + ERD
    crc = Crc.crc16_ccitt(FrameToCalculateCrc)
    crc = crc[2: ]
    frame = bitInit + FrameToCalculateCrc + crc + bitStop
    data = bytearray.fromhex(frame)
    return data

def WriteErd(strERD, dato):
    bitInit = "E2"
    dst = "C0"
    src = "E4"
    cmd = "A200"
    count = "01"
    ESC = "E0"
    ERD = str(strERD)
    dato = str(dato)
    bitStop = "E3"
    longitud = int(((len(bitInit + dst + src + cmd + ERD + count + dato + bitStop)) + 6) / 2)
    lenght = "0x{:02x}".format(longitud)
    lenght = str(lenght[2: ])   
    FrameToCalculateCrc = dst + lenght + src + cmd + ERD + count + dato
    crc = Crc.crc16_ccitt(FrameToCalculateCrc)
    crc = crc[2: ]
    if ERD != "0032":  
        frame = bitInit + FrameToCalculateCrc + crc + bitStop
    else:
        frame = bitInit + FrameToCalculateCrc + ESC + crc + bitStop
    print(frame)
    dataWrite = bytearray.fromhex(frame)
    return dataWrite

################################### TRAMA DE DATOS LECTURA ###############################################

### Bit Inicio ### dst ### length ### src ###    cmd    ###   ERD    ###   CRC    ### Bit Stop ###
#       E2          C0       XX        E4       XX XX        XX XX        XX XX          E3    ###
