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
ser.open()

packet = Frame.ErdRead("F039")
print(packet)

ser.write(packet)
print((ser.read(14)).hex())

    # print(ser.read())

