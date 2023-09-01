import serial
import requests
# Импортируем модуль для работы с Telegram API
import telegram

ACK = b'\x06'  # Пример: ASCII-символ ACK имеет код 0x06


def send_and_receive_data(yourport, mindray_ip, mindray_port, mindray_server, base, app, pacient_id, bot_token,
                          chat_id):
    ser = serial.Serial(yourport)
    try:
        ser.open()
    except Exception as e:
        print('Error opening serial port:', str(e))
        return 'N'

    if ser.is_open:
        try:
            data = ser.read(ser.in_waiting)
            ser.close()

            # Отправка данных на сервер
            payload = {'base': base, 'app': app, 'pacient_id': pacient_id, 'data': data.decode('iso-8859-1')}
            response = requests.post(mindray_server, data=payload)

            # Отправка данных в телеграм
            bot = telegram.Bot(token=bot_token)
            message = f"Received data: {data.decode('iso-8859-1')}\nResponse from server: {response.text}"
            bot.send_message(chat_id=chat_id, text=message)

            return response.text
        except Exception as e1:
            print('Communication error:', str(e1))
            return 'N'
    else:
        return 'N'


# Пример использования
yourport = "COM1"  # Замените на свой COM порт
mindray_ip = '192.168.0.100'
mindray_port = 5155
mindray_server = "http://217.29.26.60/med_aparats/parser.php"
base = 'your_base'
app = 'your_app'
pacient_id = 'your_pacient_id'

bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'  # ID чата или пользователя, кому будут отправляться сообщения

response = send_and_receive_data(yourport, mindray_ip, mindray_port, mindray_server, base, app, pacient_id, bot_token,
                                 chat_id)
print('Response from server:', response)
