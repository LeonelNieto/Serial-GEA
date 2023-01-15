import serial
import serial.tools.list_ports

def ConfiguracionSerial():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        print(port.device)
    ser = serial.Serial(ports[0].device)
    ser.baudrate = 230400
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.xonxoff = False 
    ser.rtscts = False  
    ser.dsrdtr = False  

    return ser

