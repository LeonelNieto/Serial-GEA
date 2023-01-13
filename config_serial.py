import serial

def ConfiguracionSerial(Puerto):
    Puerto = str(Puerto)
    ser = serial.Serial(baudrate=230400, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE)  
    ser.port = Puerto
    ser.stopbits = serial.STOPBITS_ONE 
    ser.xonxoff = False 
    ser.rtscts = False  
    ser.dsrdtr = False  

    return ser