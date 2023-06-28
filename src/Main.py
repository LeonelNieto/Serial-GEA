# /***********************************************************************/
# /*                                                                     */
# /*  FILE          : Main.py                                            */
# /*  DATE          : 17/02/2023                                         */
# /*  DESCRIPTION   : Serial GEA3                                        */
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

import ReadorWrite
import verifylength as vrlen
import serial
import serial.tools.list_ports
import time

# /************************************************************************
#  Name:          SetBoard()    
#  Parameters:    Board
#  Returns:       N/A
#  Called by:     N/A
#  Calls:         N/A
#  Description:   Configure serial GEA2 port, conecting to serial com
#                 with the board through LabVIEW, and define global ser  
#                 to use to write and read frames.
#               
# ************************************************************************/
def SetBoard(board):                                                                    # Función para configurar el puerto COM
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

# /************************************************************************
#  Name:          ReadButton( )    
#  Parameters:    Destination, ERD
#  Returns:       Frame read
#  Called by:     LabVIEW
#  Calls:         verifylength.longitudERD( )
#                 ReadorWrite.ReadErd( )
#  Description:   Write a frame to read a serial, and return a complete
#                 frame read.
#               
# ************************************************************************/
def ReadErd(dst, ERD):                                                           # Función para leer ERD's donde se le pasan los argumentos de Destinatio y ERD
    longitud_ERD = vrlen.longitudERD(ERD)                                           # Verifica la longitud del ERD y agrega 0s si es menor a 4 si es mayor retorna error
    ERD = longitud_ERD.upper()
    if longitud_ERD == "Fallo":                                                     # Si la longitud es mayor a 5 envía Fallo
        return "Longitud de ERD incorrecta"                                         # Retorna el mensaje de error.
    else:
        lectura = ReadorWrite.ReadErd(longitud_ERD, dst)                            # Completa la trama con el ERD y destination dado por LabVIEW
        while True:
            ser.write(lectura) 
            while True:
                reading = ser.read(1)                                                   # Se lee el primer byte
                if reading == b'\xE3':
                    complete_frame = "" 
                    while True:
                        reading = ser.read(1)
                        concatenate = reading.hex()                                     # Se convierte a hexadecimal la lectura serial
                        complete_frame += concatenate                                   # Se concatena byte por byte
                        if reading == b'\xE3' or (reading == b''):
                            break
                    complete_frame = (complete_frame.upper())
                    # print(complete_frame)
                    Dato = complete_frame
                    Byte_OK = complete_frame[12:14]
                    # print("BYTE OK: " + Byte_OK)
                    Byte_ERD = complete_frame[14:18]
                    # print("BYTE ERD: " + Byte_ERD)
                    if (Byte_ERD == ERD) and (Byte_OK == "01"):
                        Longitud_Dato_hex = complete_frame[18:20]
                        Longitud_Dato_int = int(Longitud_Dato_hex, 16) * 2
                        Dato = complete_frame[20:(20 + Longitud_Dato_int)]
                        break     
                    ser.write(lectura)       
            return Dato, complete_frame[2: ]

def ReadMultipleErds(dst, *ERDS):                                                           # Función para leer ERD's donde se le pasan los argumentos de Destinatio y ERD
    Total_Erds = ""
    for Erd in ERDS:
        Total_Erds += vrlen.longitudERD(Erd)       
    if Total_Erds == "Fallo":                                                     # Si la longitud es mayor a 5 envía Fallo
        return "Longitud de ERD incorrecta"                                         # Retorna el mensaje de error.
    else:
        lectura = ReadorWrite.ReadErd(Total_Erds, dst)                            # Completa la trama con el ERD y destination dado por LabVIEW
        while True:
            ser.write(lectura) 
            while True:
                reading = ser.read(1)                                                   # Se lee el primer byte
                if reading == b'\xE3':
                    complete_frame = "" 
                    while True:
                        reading = ser.read(1)
                        concatenate = reading.hex()                                     # Se convierte a hexadecimal la lectura serial
                        complete_frame += concatenate                                   # Se concatena byte por byte
                        if reading == b'\xE3' or (reading == b''):
                            break
                    complete_frame = (complete_frame.upper())
                    # print(complete_frame)
                    Dato = complete_frame
                    Byte_OK = complete_frame[12:14]
                    # print("BYTE OK: " + Byte_OK)
                    Byte_ERD = complete_frame[14:18]
                    # print("BYTE ERD: " + Byte_ERD)
                    print("Lectura Multiple: " + complete_frame)
                    if (Byte_ERD == Total_Erds) and (Byte_OK == "01"):
                        Longitud_Dato_hex = complete_frame[18:20]
                        Longitud_Dato_int = int(Longitud_Dato_hex, 16) * 2
                        Dato = complete_frame[20:(20 + Longitud_Dato_int)]
                        break     
                    # ser.write(lectura)       
            return Dato, complete_frame[2: ]
# /************************************************************************
#  Name:          WriteButton( )    
#  Parameters:    Destination, ERD, dato
#  Returns:       Frame read
#  Called by:     LabVIEW
#  Calls:         verifylength.longitudERD( )
#                 ReadorWrite.WriteErd( )
#  Description:   Write a frame to write a serial, and read the frame that 
#                 MC respond to return a complete frame read until 
#                 reach bit stop.
#               
# ************************************************************************/
def WriteButton(dst, ERD, dato):                                                    # Función para escirbir al ERD, con argumentos; Destination, ERD y dato 
    complete_frame = ""                                                             # Se inicia el strign de la trama vacío
    dato = dato.replace(" ", "")                                                    # Se eliminan espacios en el argumento dato
    longitudERD = vrlen.longitudERD(ERD)                                            # Verifica la longitud del ERD y agrega 0s si es menor a 4 si es mayor retorna error
    if longitudERD == "Fallo":                                                      # Si la longitud es mayor a 5 envía Fallo
        complete_frame = "Error"                                                    # Retorna Error
    else:
        escritura = ReadorWrite.WriteErd(longitudERD, dato, dst)                    # Completa la trama con el ERD, Destination y dato a escribir dado por LabVIEW
        ser.write(escritura)                                                        # Se escribe la trama por serial
        while True:
            reading = ser.read(1)                                                   # Se lee el primer byte
            concatenate = reading.hex()                                             # Se convierte a hexadecimal la lectura serial
            complete_frame += concatenate                                           # Se concatena byte por byte
            if reading == b'\xE3':                                                  # Si se lee el bit de Stop
                break                                                               # Sale del ciclo while
            if reading == b'':                                                      # Si no lee nada
                break                                                               # Sale del ciclo while
        BitInicio = complete_frame[0:2]                                             # Toma los dos primeros valores
        if BitInicio != "e2":                                                       # Verifica que no sea el bit de inio
            complete_frame = "Error"                                                # Si no es manda Error
        else:                                                                       # Si es el bit de inio
            complete_frame = complete_frame[2: ]                                    # Manda la trama de datos sin el bit de inicio
        return complete_frame                                                       # Retorna la trama

SetBoard(1)
print(ReadErd("C0", "700"))
time.sleep(0.2)
WriteButton("C0", "0032", "01")
time.sleep(3.1)
print(ReadErd("C0", "700"))
time.sleep(0.2)
print(ReadMultipleErds("C0", "700", "32", "F01B"))
# /************************************************************************
#  Name:          WriteBootloader( )    
#  Parameters:    Destination, command, message
#  Returns:       Frame read
#  Called by:     LabVIEW
#  Calls:         ReadorWrite.Boatloader( )
#  Description:   Write a frame to write a serial message, and read
#                 the frame that MC respond to return a complete frame 
#                 read until reach bit stop.
#               
# ************************************************************************/
def WriteBoatloader(dst, command, message):                                             # Función para escribir mensajes con lo argumentos Destination, Comando y Mensaje.
    CompleteFrame = "" 
    dst = str(dst)
    command = str(command)
    message = str(message)
    lectura = ReadorWrite.Boatloader(dst, command, message)                             # Concatenación de la trama completa a escribir
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
