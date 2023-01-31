import serial
import serial.tools.list_ports

def ConfiguracionSerial():                                 #Para W10 seleccionar el puerto de la placa
    global ser
    ser = serial.Serial()
    ser.baudrate = 230400
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.xonxoff = False 
    ser.rtscts = False  
    ser.dsrdtr = False  

    return ser

def AbrirPuerto(board):
    com_ports = list(serial.tools.list_ports.comports())
    ser.port = com_ports[board].device
    ser.open()
 
escritura = ConfiguracionSerial()
AbrirPuerto(0)
dato = "E2C00DE4A200F03901018D6EE3"
dataWrite = bytearray.fromhex(dato)
escritura.write(dataWrite)