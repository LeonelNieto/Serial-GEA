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
    com_ports = list(serial.tools.list_ports.comports())
    ser.port = com_ports[0].device
    ser.open()

import serial
import time

ser = None

def connect_serial(n):
    global ser
    # Obtener una lista de todos los puertos COM disponibles
    com_ports = list(serial.tools.list_ports.comports())

    # Verificar si hay algún puerto disponible
    if com_ports:
        # Configurar la conexión serial con el primer puerto disponible
        if not ser:
            ser = serial.Serial()
            ser.baudrate = 9600
            ser.port = com_ports[0].device
        # Abrir la conexión
        ser.open()
        print("Se ha conectado al puerto:", ser.port)
        
        # Contador de tramas
        trama_count = 0
        # Bucle de lectura
        start_time = time.time()
        while trama_count < n and time.time() - start_time < 0.1:
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
                    print("Trama recibida:", trama)
                    trama_count += 1
        # Cerrar la conexión
        ser.close()
    else:
        # No hay puertos disponibles
        print("No se ha encontrado ningún puerto COM disponible.")

# Llamar a la función para conectarse y leer 10 tramas
connect_serial(10)