import serial


# Leitura serial
def readserial(comport, baudrate):

    ser = serial.Serial(comport, baudrate, timeout=0.1)

    while True:
        data = ser.readline().decode('utf-8', errors='ignore').strip()
        if data:
            print(data)

if __name__ == '__main__':

    readserial('COM9', 9600)