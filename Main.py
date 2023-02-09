import ReadorWrite
import verifylength as vrlen
import serial
import serial.tools.list_ports
import time

ser = serial.Serial()
ser.baudrate = 230400
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.xonxoff = False 
ser.rtscts = False  
ser.dsrdtr = False
com_ports = list(serial.tools.list_ports.comports())
ser.port = com_ports[1].device
ser.open()

def ReadButton(dst, ERD):
    complete_frame = ""
    longitud_ERD = vrlen.longitudERD(ERD)
    if longitud_ERD == "Fallo":
        complete_frame = "Error"
    else:
        lectura = ReadorWrite.ReadErd(longitud_ERD, dst) 
        ser.write(lectura)
        reading = ser.read(1)
        if reading != b'\xE2':
            complete_frame = "Error"
        else:
            while True:
                reading = ser.read(1)
                concatenate = reading.hex()
                complete_frame += concatenate
                if reading == b'\xE3':
                    break
                if reading == b'':
                    break
    return complete_frame

# print(ReadButton("C0", "F039"))

def connect_serial(dst, ERD):
    longitud_ERD = vrlen.longitudERD(ERD)
    lectura = ReadorWrite.ReadErd(longitud_ERD, dst) 
    ser.write(lectura)
    while True:
        data = ser.read(ser.in_waiting)
        # Buscar el bit de inicio "E2"
        start = data.find(b'\xE2')
        if start != -1:
            # Encontró el bit de inicio, buscar el bit de paro "E3"
            stop = data.find(b'\xE3', start)
            if stop != -1:
                # Encontró la trama completa, procesar los datos
                trama = data[start:stop + 1]
                break
    return trama

# print(connect_serial("C0","F039"))

# while True:
#     print(ReadButton("C0", "F039"))
#     print(ReadButton("C0", "2000"))
#     print(ReadButton("C0", "209E"))
#     print(ReadButton("C0", "209F"))
#     print(ReadButton("C0", "f01b"))

def WriteButton(dst, ERD, dato):
    complete_frame = ""
    dato = dato.replace(" ", "")
    longitudERD = vrlen.longitudERD(ERD)
    if longitudERD == "Fallo":
        complete_frame = "Error"
    else:
        escritura = ReadorWrite.WriteErd(longitudERD, dato, dst)
        ser.write(escritura)
        reading = (ser.read())
        if reading != b'\xE2':
            complete_frame = "Error"
        else:  
            while True:
                reading = ser.read(1)
                concatenate = reading.hex()
                complete_frame += concatenate
                if reading == b'\xE3':
                    break
                if reading == b'':
                    break
    return complete_frame

def WriteBoatloader(dst, command, message):
    CompleteFrame = "" 
    dst = str(dst)
    command = str(command)
    message = str(message)
    board = int(board)
    lectura = ReadorWrite.Boatloader(dst, command, message)                                                                   # Función para abrir puerto con la configuración serial
    ser.write(lectura)                                                                                          # Escribe al puerto serial
    reading = (ser.read()).hex()                                                                                # Lee el primer byte de datos convertido a hexadecimal
    if reading != "e2":                                                                                         # Si el primer byte es el byte de inicio
        CompleteFrame = "Error"
    else:                                                                                                       # Si no detecta el bit de inicio muestra mensaje de error
        while (1):
            reading = (ser.read()).hex()                                                                        # Se lee byte por byte
            CompleteFrame += reading                                                                            # Concatenación de bytes
            if reading == "":                                                                                   # Si no lee nada sale del ciclo
                break
            elif reading == "e3":                                                                               # Si detecta el byte de paro sale del ciclo
                break 
    Mensaje = CompleteFrame.upper()
    return Mensaje

