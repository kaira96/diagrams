import serial
import time
import requests

# Здесь задайте значение символа ACK, который ожидается от устройства
ACK = b'\x06'  # Пример: ASCII-символ ACK имеет код 0x06


def sendserial(sendstring, yourport, mindray_ip, mindray_port, mindray_server, base, app, pacient_id):
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

            # Отправка данных на сервер
            payload = {'base': base, 'app': app, 'pacient_id': pacient_id, 'data': response}
            response = requests.post(mindray_server, data=payload)

            return response.text
        except Exception as e1:
            print('Communication error:', str(e1))
            return 'N'
    else:
        return 'N'


# Пример использования
yourport = input('Введите подключаемый порт COM1 или /dev/ttyUSB0 и тп: ')
sendstring = input('Введите данные, которые вы хотите отправить: ')
mindray_ip = '192.168.0.100'
mindray_port = 5155
mindray_server = "http://217.29.26.60/med_aparats/parser.php"
base = 'your_base'
app = 'your_app'
pacient_id = 'your_pacient_id'
response = sendserial(sendstring, yourport, mindray_ip, mindray_port, mindray_server, base, app, pacient_id)
print('Response from server:', response)
