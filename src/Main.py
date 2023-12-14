import ReadorWrite
import verifylength as vrlen
import serial
import time

def SetBoard() -> None:                                                                    # Función para configurar el puerto COM
    """
    Función para configurar el puerto serial  GEA2
    
    Args:
        board (int): Numero de puerto de la lista
        
    Returns:
        None
    """
    global ser
    ser = serial.Serial()
    ser.baudrate = 19200                                                               
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE 
    ser.STOPBITS = None                                                         
    ser.timeout = 0.02                                                                 
    ser.port = "COM14"                                                                  
    ser.open()                                                                         

def ReadErd(dst, ERD:str) -> str:                                                     
    """
    Función que permite la lectura de ERDS a través
    del envío de la trama de datos por serial.
    
    Args:
        dst (str): Dirección de la tarjeta que se quiere comunicar
        ERD (str): ERD que se quiere consultar
        
    Returns:
        (str): Dato del ERD consultado 
    """
    Erd = vrlen.longitudERD(ERD)             
    while True:
        complete_frame = ""  
        lectura = ReadorWrite.ReadErd(Erd, dst)        
        ser.write(lectura)                                       
        while True:
            reading = ser.read(1)                 
            concatenate = reading.hex()                                     
            complete_frame += concatenate                                        
            if reading == b'\xE3':                               
                break                   
            if reading == b'':   
                complete_frame = "Verifica conexiones"   
                return "None"
        complete_frame = complete_frame.upper()             
        Byte_ERD = complete_frame[14:18]
        Byte_OK = complete_frame[12:14]
        if (Byte_ERD == ERD) and (Byte_OK == "00"):
            Longitud_Dato_hex = complete_frame[18:20]
            Longitud_Dato_int = int(Longitud_Dato_hex, 16) * 2
            Dato = complete_frame[20:(20 + Longitud_Dato_int)]
            break
    return Dato      

SetBoard()
print(ReadErd("E2230BE4F0012F0A9FE0E0E3", "2F0A"))

def WriteButton(dst:str, ERD:str, dato:str) -> None:                                                    # Función para escirbir al ERD, con argumentos; Destination, ERD y dato                                                              # Se inicia el strign de la trama vacío
    """
    Función que permite la escritura de ERDS a través
    del envío de la trama de datos por serial.
    
    Args:
        dst (str): Dirección de la tarjeta que se quiere comunicar
        ERD (str): ERD que se quiere consultar
        dato(str): Dato que se le quiere escribir al ERD
        
    Returns:
        None
    """
    i = 0
    while i <= 1:
        i += 1
        dato = dato.replace(" ", "")                                            # Se eliminan espacios en el argumento dato
        Erd = vrlen.longitudERD(ERD)                                            # Verifica la longitud del ERD y agrega 0s si es menor a 4 si es mayor retorna error
        escritura = ReadorWrite.BuildFrameToWriteErd(Erd, dato, dst)            # Completa la trama con el ERD, Destination y dato a escribir dado por LabVIEW
        ser.write(escritura)                                                    # Se escribe la trama por serial

def WriteBoatloader(dst, command, message):                                     
    """
    Función que permite la el envío de mensajes 
    al bootloader a través de la trama de datos serial.
    
    Args:
        dst     (str): Dirección de la tarjeta que se quiere comunicar
        command (str): Comando del bootloader
        message (str): Mensaje que quieres consultar 
        
    Returns:
        (str): Trama de datos del bootloader
    """
    CompleteFrame = "" 
    dst = str(dst)
    command = str(command)
    message = str(message)
    lectura = ReadorWrite.BuildFrameToBootloader(dst, command, message)                             # Concatenación de la trama completa a escribir
    ser.write(lectura)                                                                  # Escribe la trama al puerto serial
    reading = (ser.read()).hex()                                                        # Lee el primer byte de datos y lo convierte a hexadecimal
    if reading != "e2":                                                                 # Si el primer byte no es el byte de inicio
        CompleteFrame = "Error"
    else:                                                                               # Si el primer byte leido es el de Inicio
        while (1):
            reading = (ser.read()).hex()                                                # Lee byte por byte y lo convierte a hexadecimal 
            CompleteFrame += reading                                                    # Concatenación de bytes
            if reading == "":                                                           # Si no lee nada sale del ciclo
                break
            elif reading == "e3":                                                       # Si detecta el byte de paro sale del ciclo
                break 
    Mensaje = CompleteFrame.upper()                                                     # Convierte la trama a Mayusculas
    return Mensaje                                                                      # Retorna la trama o mensaje de error
