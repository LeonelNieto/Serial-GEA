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
ser.port = com_ports[0].device
ser.open()

def ReadButton(dst, ERD):
    complete_frame = ""
    longitud_ERD = vrlen.longitudERD(ERD)
    if longitud_ERD == "Fallo":
        return "Error"
    else:
        lectura = ReadorWrite.ReadErd(longitud_ERD, dst) 
        ser.write(lectura)
        reading = (ser.read()).hex()
        if reading != "e2":
            return "Error"
        else:
            while True:
                reading = (ser.read()).hex()
                complete_frame += reading
                if reading == "e3":
                    break
    return complete_frame

def WriteButton(dst, ERD, dato):
    CompleteFrame = ""
    dato = dato.replace(" ", "")
    longitudERD = vrlen.longitudERD(ERD)
    if longitudERD == "Fallo":
        CompleteFrame = "Error"
    else:
        escritura = ReadorWrite.WriteErd(longitudERD, dato, dst)
        ser = ConfiguracionSerial()
        ser.write(escritura)
        reading = (ser.read()).hex()
        if reading == "e2":
            while (1):
                reading = (ser.read()).hex()
                CompleteFrame += reading
                if reading == "":
                    break
                elif reading == "e3":
                    break
        else:
            CompleteFrame = "Error"
        
    return CompleteFrame

def WriteBoatloader(dst, command, message):
    CompleteFrame = "" 
    dst = str(dst)
    command = str(command)
    message = str(message)
    board = int(board)
    lectura = ReadorWrite.Boatloader(dst, command, message)                                                                   # Función para abrir puerto con la configuración serial
    ser = ConfiguracionSerial()
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

