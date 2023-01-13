import Crc

def ErdRead(strERD):
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

print(ErdRead("F039"))

# InputERDLectura("F039")

################################### TRAMA DE DATOS ###############################################

### Bit Inicio ### dst ### length ### src ###    cmd    ###   ERD    ###   CRC    ### Bit Stop ###
#       E2          C0       XX        E4       XX XX        XX XX        XX XX          E3    ###
