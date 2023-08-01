"""Módulo de lectura, escritura y bootloader ERDS.
Este modulo tiene la función para configurar
el serial y las funciones para la lectura
y escritura de ERDS, así como la función para 
enviar mensaje al bootloader."""

import ReadorWrite
import verifylength as vrlen
import serial
import serial.tools.list_ports

def SetBoard(board: int) -> None:                                                                    # Función para configurar el puerto COM
    """
    Función para configurar el puerto serial  GEA2
    
    Args:
        board (int): Numero de puerto de la lista
        
    Returns:
        None
    """
    global ser
    ser = serial.Serial()
    ser.baudrate = 19200                                                                # Baudrate para GEA2
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE 
    ser.STOPBITS = None                                                         
    ser.timeout = 0.5                                                                   # Timeout 500 ms si no responde
    com_ports = list(serial.tools.list_ports.comports())                                # Crea una lista para los puertos disponibles
    ser.port = com_ports[board].device                                                  # Se define el puerto a través de LabVIEW
    ser.open()                                                                          # Abre puerto COM

def ReadErd(dst:str, ERD:str) -> str:                                                   # Función para leer ERD's donde se le pasan los argumentos de Destinatio y ERD
    """
    Función que permite la lectura de ERDS a través
    del envío de la trama de datos por serial.
    
    Args:
        dst (str): Dirección de la tarjeta que se quiere comunicar
        ERD (str): ERD que se quiere consultar
        
    Returns:
        (str): Dato del ERD consultado 
    """
    Erd = vrlen.longitudERD(ERD).upper()                                                # Verifica la longitud del ERD y agrega 0s si es menor a 4 si es mayor retorna error
    if Erd == "Fallo":                                                                  # Si la longitud es mayor a 5 envía Fallo
        return "Longitud de ERD incorrecta"                                             # Retorna el mensaje de error.
    else:
        lectura = ReadorWrite.BuildFrameToReadErd(Erd, dst)                             # Completa la trama con el ERD y destination dado por LabVIEW
        while True:
            ser.write(lectura) 
            while True:
                reading = ser.read(1)                                                   # Se lee el primer byte
                if reading == b'\xe3':
                    complete_frame = "" 
                    while True:
                        reading = ser.read(1)
                        concatenate = reading.hex()                                     # Se convierte a hexadecimal la lectura serial
                        complete_frame += concatenate                                   # Se concatena byte por byte
                        if reading == b'\xe3' or (reading == b''):
                            break
                    complete_frame = (complete_frame.upper())
                    Dato = complete_frame
                    if complete_frame[0:6] == "E1E2E4":
                        Byte_OK = complete_frame[12:14]
                        Byte_ERD = complete_frame[14:18]
                        Longitud_Dato_hex = complete_frame[18:20]
                        Longitud_Dato_int = int(Longitud_Dato_hex, 16) * 2
                        if (complete_frame[(20 + Longitud_Dato_int):20 + Longitud_Dato_int + 2]) == "E0":
                            Len_Is_Correct = Longitud_Dato_int + 8 == len(complete_frame[20: ])
                        else:
                            Len_Is_Correct = Longitud_Dato_int + 6 == len(complete_frame[20: ])
                        if complete_frame[-6:-2] == "E0E1":
                            Len_Is_Correct = Longitud_Dato_int + 8 == len(complete_frame[20: ])
                        if (Byte_ERD == ERD) and (Byte_OK == "01") and Len_Is_Correct:
                            Dato = complete_frame[20:(20 + Longitud_Dato_int)]
                            return Dato
                    if complete_frame[0:4] == "E2E4":
                        Byte_OK = complete_frame[10:12]
                        Byte_ERD = complete_frame[12:16]
                        Longitud_Dato_hex = complete_frame[16:18]
                        Longitud_Dato_int = int(Longitud_Dato_hex, 16) * 2
                        if (Byte_ERD == ERD) and (Byte_OK == "01") and (Longitud_Dato_int + 6 == len(complete_frame[18: ])):
                            Dato = complete_frame[18:(18 + Longitud_Dato_int)]
                            return Dato   
                    break     

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
        dato = dato.replace(" ", "")                                                    # Se eliminan espacios en el argumento dato
        Erd = vrlen.longitudERD(ERD)                                                    # Verifica la longitud del ERD y agrega 0s si es menor a 4 si es mayor retorna error
        escritura = ReadorWrite.BuildFrameToWriteErd(Erd, dato, dst)                    # Completa la trama con el ERD, Destination y dato a escribir dado por LabVIEW
        ser.write(escritura)                                                            # Se escribe la trama por serial

def WriteBoatloader(dst, command, message):                                             # Función para escribir mensajes con lo argumentos Destination, Comando y Mensaje.
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
    lectura = ReadorWrite.BuildFrameToBootloader(dst, command, message)                 # Concatenación de la trama completa a escribir
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
