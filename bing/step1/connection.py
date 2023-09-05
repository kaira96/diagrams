import serial
import time

# Подключение к устройству через COM-порт
ser = serial.Serial(
    port='COM1',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

# Отправка команды на получение данных
ser.write(b'get_data\r\n')
time.sleep(1)

# Чтение данных с устройства
data = ser.read(ser.inWaiting())
print(data)

# Отправка данных на удаленный сервер
import requests
url = 'https://yourserver.com/data'
requests.post(url, data=data)

# Закрытие соединения с устройством
ser.close()
