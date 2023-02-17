# /***********************************************************************/
# /*                                                                     */
# /*  FILE          : ReadorWrite.py                                     */
# /*  DATE          : 17/02/2023                                         */
# /*  DESCRIPTION   : Concatenate data frame                             */
# /*                                                                     */
# /*  AUTHOR        : Leonel Nieto Lara                                  */
# /*                                                                     */
# /*  PROJECT       : GEA3 Tool                                          */
# /*  IDE           : Visual Studio Code                                 */
# /*  Python Version: 3.9.13                                             */
# */                                                                     */
# /*  Copyright 2012-2023 Mabe TyP                                       */
# /*  All rights reserved                                                */
# /*                                                                     */
# /***********************************************************************/

import Crc

def ReadErd(ERD, dst):
    bitInit = "E2"
    src = "E4"
    cmd = "A000"
    bitStop = "E3"
    longitud = int(((len(bitInit + dst + src + cmd + ERD + bitStop)) + 6) / 2)
    lenght = "{:02x}".format(longitud) 
    FrameToCalculateCrc = dst + lenght + src + cmd + ERD
    crc = Crc.crc16_ccitt(FrameToCalculateCrc)
    crc = crc[2: ]
    frame = bitInit + FrameToCalculateCrc + crc + bitStop
    data = bytes.fromhex(frame)
    return data  

def WriteErd(strERD, dato, strdst):
    bitInit = "E2"
    dst = str(strdst)
    src = "E4"
    cmd = "A200"
    count = int((len(dato)) / 2)
    count = "0x{:02x}".format(count)
    count = count[2: ]
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
    dataWrite = bytearray.fromhex(frame)
    
    return dataWrite

def Boatloader(Dst, command, message):
    bitInit = "E2"
    dst = str(Dst)
    src = "E4"
    cmd = str(command)
    msg = str(message)
    bitStop = "E3"
    longitud = int(((len(bitInit + dst + src + cmd + msg + bitStop)) + 6) / 2)
    lenght = "0x{:02x}".format(longitud)
    lenght = str(lenght[2: ])   
    FrameToCalculateCrc = dst + lenght + src + cmd + msg
    crc = Crc.crc16_ccitt(FrameToCalculateCrc)
    crc = crc[2: ]
    frame = bitInit + FrameToCalculateCrc + crc + bitStop
    data = bytes.fromhex(frame)

    return data

################################### TRAMA DE DATOS LECTURA ###############################################

### Bit Inicio ### dst ### length ### src ###    cmd    ###   ERD    ###   CRC    ### Bit Stop ###
#       E2          C0       XX        E4       XX XX        XX XX        XX XX          E3    ###
