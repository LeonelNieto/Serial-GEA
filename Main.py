import config_serial
import ReadorWrite
import verifylength as vrlen

def ReadButton(dst, ERD):
    complete_frame = []
    longitud_ERD = vrlen.longitudERD(ERD)
    if longitud_ERD == "Fallo":
        return "Error"
    else:
        lectura = ReadorWrite.ReadErd(longitud_ERD, dst) 
        ser = config_serial.ConfiguracionSerial()
        ser.write(lectura)
        reading = (ser.read(1)).hex()
        if reading != "e2":
            return "Error"
        else:
            while True:
                reading = (ser.read(1)).hex()
                complete_frame.append(reading)
                if reading == "e3":
                    break
            return ''.join(complete_frame)
        
def WriteButton(dst, ERD, dato):
    CompleteFrame = ""
    dato = dato.replace(" ", "")
    longitudERD = vrlen.longitudERD(ERD)
    if longitudERD == "Fallo":
        CompleteFrame = "Error"
    else:
        escritura = ReadorWrite.WriteErd(longitudERD, dato, dst)
        ser = config_serial.ConfiguracionSerial()
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

def WriteBoatloader(dst, command, message, board):
    CompleteFrame = "" 
    dst = str(dst)
    command = str(command)
    message = str(message)
    board = int(board)
    lectura = ReadorWrite.Boatloader(dst, command, message) 
    ser = config_serial.ConfiguracionSerial(board)                                                                   # Función para abrir puerto con la configuración serial
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

