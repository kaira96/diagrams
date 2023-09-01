import serial
import time

# Здесь задайте значение символа ACK, который ожидается от устройства
ACK = b'\x06'  # Пример: ASCII-символ ACK имеет код 0x06

def sendserial(sendstring, yourport):
    ser = serial.Serial()
    ser.port = yourport
    try:
        ser.open()
    except Exception as e:
        print('Error opening serial port:', str(e))
        return 'N'
    if ser.is_open:
        try:
            ser.flushInput()
            ser.flushOutput()
            ser.write(sendstring.encode('iso-8859-1'))
            time.sleep(0.5)
            numOfLines = 0
            while True:
                response = ser.readline().decode()
                result = ord(response)
                if result == ord(ACK):
                    response = 'Y'
                else:
                    response = 'N'
                numOfLines = numOfLines + 1
                if numOfLines >= 1:
                    break
            ser.close()
            return response
        except Exception as e1:
            print('Communication error:', str(e1))
            return 'N'
    else:
        return 'N'

# Пример использования
# yourport = '/dev/ttyUSB0'  # Замените на соответствующий COM порт
yourport = 'COM1'  # Замените на соответствующий COM порт
sendstring = 'Hello, Mindray!'  # Замените на данные, которые вы хотите отправить
response = sendserial(sendstring, yourport)
print('Response:', response)
