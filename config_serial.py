import serial
import serial.tools.list_ports

                               #Para W10 seleccionar el puerto de la placa

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


ser = None

def connect_serial():
    while True:
        # Leer los datos que llegan al puerto serial
        data = ser.read(ser.in_waiting)
        # Buscar el bit de inicio "E2"
        start = data.find(b'\xE2')
        if start != -1:
            # Encontró el bit de inicio, buscar el bit de paro "E3"
            stop = data.find(b'\xE3', start)
            if stop != -1:
                # Encontró la trama completa, procesar los datos
                trama = data[start:stop + 1]
                break
    return trama
