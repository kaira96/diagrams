from flask import Flask, request, render_template
import serial
import time

app = Flask(__name__)

# Подключение к устройству через COM-порт
ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.form['command']
    ser.write(command.encode() + b'\r\n')
    time.sleep(1)
    data = ser.read(ser.inWaiting())
    return data

if __name__ == '__main__':
    app.run()
