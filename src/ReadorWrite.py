"""
Módulo que forma la trama de datos para
la escritura, lectura de ERDs y el 
envío de mensajes para el bootloader.
"""
import Crc16ccitt

def BuildFrameToReadErd(ERD:str, dst:str) -> bytes:
    """
    Función que construye la trama de datos a enviar
    para el request de la lectura de ERDs
    
    Args:
        ERD (str): ERD que se desea consultar
        dst (str): Dirección de la tarjeta que se quiere consultar
        
    return:
        bytes: Trama de datos completa a enviar por serial
    """
    BIT_INIT = "E2"
    BIT_STOP = "E3"
    SRC = "E4"
    CMD = "F001"
    longitud = int(((len(BIT_INIT + dst + SRC + CMD + ERD + BIT_STOP)) + 6) / 2)
    lenght = "{:02x}".format(longitud)
    FrameToCalculateCrc = dst + lenght + SRC + CMD + ERD
    crc = Crc16ccitt.crc16_ccitt(FrameToCalculateCrc)
    frame = BIT_INIT + FrameToCalculateCrc + crc + BIT_STOP 
    if ERD in ["20BE", "2F0A"]:
        frame = (BIT_INIT + FrameToCalculateCrc + crc + "E0" + BIT_STOP).upper()
    print("Fame a escribir: " + frame)
    data = bytes.fromhex(frame)                                                                    
    return data

print(BuildFrameToReadErd("2F0A", "23"))
    
def BuildFrameToWriteErd(ERD:str, dato:str, dst:str) -> bytes:
    """
    Función que construye la trama de datos a enviar
    para el request de la escritura de ERDs
    
    Args:
        ERD  (str): ERD que se desea consultar
        dato (str): Dato a escribir al ERD
        dst  (str): Dirección de la tarjeta que se quiere consultar
        
    return:
        bytes: Trama de datos completa a enviar por serial
    """
    BIT_INIT = "E2"                                                                                   
    BIT_ESC = "E0"                                                                                     
    BIT_STOP = "E3"                                                                                    
    SRC = "E4"                                                                                     
    CMD = "F101"                                                                                        
    Erd_data_size = int((len(dato)) / 2)                                                                
    Erd_data_size = "{:02x}".format(Erd_data_size)                                                    
    longitud = int(((len(BIT_INIT + dst + SRC + CMD + ERD + Erd_data_size + dato + BIT_STOP)) + 6) / 2)   
    lenght = "{:02x}".format(longitud)                                                               
    FrameToCalculateCrc = dst + lenght + SRC + CMD + ERD + Erd_data_size + dato                   
    crc = Crc16ccitt.crc16_ccitt(FrameToCalculateCrc)                                                                                                                            
    if ERD not in ["0032", "F097", "2F0A"]:                                                                             
        frame = BIT_INIT + FrameToCalculateCrc + crc + BIT_STOP                                   
    else:                                                                                        
        frame = BIT_INIT + FrameToCalculateCrc + BIT_ESC + crc + BIT_STOP                                   
    dataWrite = bytearray.fromhex(frame)                                                              
    return dataWrite                                                                                    


def BuildFrameToBootloader(dst, cmd, msg):
    """
    Función que construye la trama de datos a enviar
    para el envío de mensajes al bootloader
    
    Args:
        dst (str): Dirección de la tarjeta que se quiere consultar
        cmd (str): Comando para el bootloader
        msg (str): Mensaje a enviar al bootloader
        
    return:
        bytes: Trama de datos completa a enviar por serial
    """
    BIT_INIT = "E2"                                                                               
    SRC = "E4"                                                                             
    BIT_STOP = "E3"                                                                          
    longitud = int(((len(BIT_INIT + dst + SRC + cmd + msg + BIT_STOP)) + 6) / 2)                       
    lenght = "{:02x}".format(longitud)                                                             
    FrameToCalculateCrc = dst + lenght + SRC + cmd + msg                                            
    crc = Crc16ccitt.crc16_ccitt(FrameToCalculateCrc)                                                     
    frame = BIT_INIT + FrameToCalculateCrc + crc + BIT_STOP                                            
    data = bytes.fromhex(frame)                                                                         
    return data                                                                                         

################################### TRAMA DE DATOS LECTURA ###############################################

### Bit Inicio ### dst ### length ### src ###    cmd    ###   ERD    ###   CRC    ### Bit Stop ###
#       E2          C0       XX        E4       XX XX        XX XX        XX XX          E3    ###
