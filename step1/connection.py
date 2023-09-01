import socket

def connect_to_mindray_bs200():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect(('192.168.0.150', 2000))
    client_socket.connect(('192.168.0.100', 5155))
    print('Connected to Mindray BS 200')

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        handle_mindray_data(data)

    client_socket.close()
    print('Connection closed')

def handle_mindray_data(data):
    print('Received data:', data.decode())
    # Здесь можно добавить логику для обработки полученных данных

if __name__ == "__main__":
    connect_to_mindray_bs200()

################################################# или ###########################################

# import serial
#
# def receive_data_from_device(yourport):
#     ser = serial.Serial(yourport)
#     try:
#         ser.open()
#     except Exception as e:
#         print('Error opening serial port:', str(e))
#         return 'N'
#
#     if ser.is_open:
#         try:
#             data = ser.read(ser.in_waiting)
#             ser.close()
#             return data.decode('iso-8859-1')
#         except Exception as e1:
#             print('Communication error:', str(e1))
#             return 'N'
#     else:
#         return 'N'
#
#
# # Пример использования
# yourport = "COM1"  # Замените на свой COM порт
# received_data = receive_data_from_device(yourport)
# print('Received data:', received_data)



########################### соединение и отправка данных ###########################################


# import serial
# import requests
#
# ACK = b'\x06'  # Пример: ASCII-символ ACK имеет код 0x06
#
# def send_and_receive_data(yourport, mindray_ip, mindray_port, mindray_server, base, app, pacient_id):
#     ser = serial.Serial(yourport)
#     try:
#         ser.open()
#     except Exception as e:
#         print('Error opening serial port:', str(e))
#         return 'N'
#
#     if ser.is_open:
#         try:
#             data = ser.read(ser.in_waiting)
#             ser.close()
#
#             # Отправка данных на сервер
#             payload = {'base': base, 'app': app, 'pacient_id': pacient_id, 'data': data.decode('iso-8859-1')}
#             response = requests.post(mindray_server, data=payload)
#
#             return response.text
#         except Exception as e1:
#             print('Communication error:', str(e1))
#             return 'N'
#     else:
#         return 'N'
#
#
# # Пример использования
# yourport = "COM1"  # Замените на свой COM порт
# mindray_ip = '192.168.0.100'
# mindray_port = 5155
# mindray_server = "http://217.29.26.60/med_aparats/parser.php"
# base = 'your_base'
# app = 'your_app'
# pacient_id = 'your_pacient_id'
#
# response = send_and_receive_data(yourport, mindray_ip, mindray_port, mindray_server, base, app, pacient_id)
# print('Response from server:', response)
