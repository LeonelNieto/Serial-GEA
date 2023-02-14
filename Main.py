import ReadorWrite
import verifylength as vrlen
import serial
import serial.tools.list_ports

def SetBoard(board):
    global ser
    ser = serial.Serial()
    ser.baudrate = 230400
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.xonxoff = False 
    ser.rtscts = False  
    ser.dsrdtr = False
    ser.timeout = 0.5
    com_ports = list(serial.tools.list_ports.comports())
    ser.port = com_ports[board].device
    ser.open()
    
def Gea2Serial(board):
    global Gea2ser
    Gea2ser = serial.Serial()
    Gea2ser.baudrate = 19200
    Gea2ser.bytesize = serial.EIGHTBITS
    Gea2ser.parity = serial.PARITY_NONE
    Gea2ser.xonxoff = False 
    Gea2ser.rtscts = False  
    Gea2ser.dsrdtr = False
    Gea2ser.timeout = 0.5
    com_ports = list(serial.tools.list_ports.comports())
    Gea2ser.port = com_ports[board].device
    Gea2ser.open()

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

def ReadGEA2ERD(dst, ERD):
    complete_frame = ""
    longitud_ERD = vrlen.longitudERD(ERD)
    if longitud_ERD == "Fallo":
        complete_frame = "Error"
    else:
        lectura = ReadorWrite.GEA2ReadErd(longitud_ERD, dst) 
        Gea2ser.write(lectura)
        reading = Gea2ser.read(1)
        if reading != b'\xE2':
            complete_frame = "Error"
        else:
            while True:
                reading = Gea2ser.read(1)
                concatenate = reading.hex()
                complete_frame += concatenate
                if reading == b'\xE3':
                    break
                if reading == b'':
                    break
    return complete_frame

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
