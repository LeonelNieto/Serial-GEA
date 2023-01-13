import serial, time

ser = serial.Serial(baudrate=230400, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_NONE)  
ser.port = "COM9"
ser.stopbits = serial.STOPBITS_ONE 
ser.xonxoff = False 
ser.rtscts = False  
ser.dsrdtr = False  
print("connected to: " + ser.portstr)
ser.open()

packet = bytearray()
packet.append(0xE2)
packet.append(0xC0)
packet.append(0x0D)
packet.append(0xE4)
packet.append(0xA2)
packet.append(0x00)
packet.append(0xF0)
packet.append(0x39)
packet.append(0x01)
packet.append(0x02)
packet.append(0xBD)
packet.append(0x0D)
packet.append(0xE3)


ser.write(packet)
print((ser.read(14)).hex())
    # print(ser.read())

