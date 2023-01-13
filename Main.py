"""
The goal of this proyect is make a serial communication usign GEA3 protocol with a TTL-USB serial.

@author: Leonel Nieto Lara
@company: Mabe TyP
@Date: 13/01/2022

source:
* https://geappliances.atlassian.net/wiki/spaces/SDAED/pages/3298000900/GEA3+Communication?preview=/3298000900/3297935398/image2022-8-19_16-35-51.png
* https://github.com/geappliances/applcommon.next-gen-specs/blob/master/erd-api.md#public
* https://github.com/geappliances/documentation.gea-communication/blob/master/MessageFormat.md
* http://www.sunshine2k.de/coding/javascript/crc/crc_js.html

"""
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


