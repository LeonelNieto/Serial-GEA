import serial
import Frame

ser = serial.Serial(baudrate=230400, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE)  
ser.port = "COM9"
ser.stopbits = serial.STOPBITS_ONE 
ser.xonxoff = False 
ser.rtscts = False  
ser.dsrdtr = False  
print("connected to: " + ser.portstr)

ERD = str(input("Ingresa el ERD a leer: "))

ser.open()
packet = Frame.ReadErd(ERD)
ser.write(packet)

while (1):
    reading = (ser.read()).hex()

    if reading != "e3":
        print(reading)
    else:
        break


#e4 c0 00 f0 01 38 e3
#e2 e4 0e c0 a1 00 00 f0 39 01 01
