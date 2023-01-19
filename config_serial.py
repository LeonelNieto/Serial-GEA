import serial
import serial.tools.list_ports

def ConfiguracionSerial(board):
    ports = list(serial.tools.list_ports.comports())
    ser = serial.Serial(ports[board].device)
    ser.baudrate = 230400
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.xonxoff = False 
    ser.rtscts = False  
    ser.dsrdtr = False  

    return ser

