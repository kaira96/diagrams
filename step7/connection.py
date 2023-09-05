import serial
import requests
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from flask import Flask, request

API_TOKEN = 'YOUR_BOT_TOKEN'

# Инициализация Flask
app = Flask(__name__)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# Здесь задайте значение символа ACK, который ожидается от устройства
ACK = b'\x06'  # Пример: ASCII-символ ACK имеет код 0x06

# Определение состояний
class YourStateName1(StatesGroup):
    waiting_for_data = State()  # Пример состояния

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я готов к работе. Используйте команды /open, /read, /close и /senddata.")

@dp.message_handler(commands=['open'])
async def open_port(message: types.Message, state: FSMContext):
    # Здесь выполните открытие COM-порта и другие действия
    user_id = message.from_user.id
    # Сохраняем объект serial.Serial в состояние FSM
    # Вам нужно добавить код для открытия COM-порта и сохранения его в состояние FSM
    await message.reply("COM-порт открыт.", reply=False)
    await YourStateName1.waiting_for_data.set()

# Добавьте обработчики для остальных команд /read, /close, /senddata

# Реализация Flask-маршрута для приема данных от устройства
@app.route('/read_data', methods=['POST'])
def read_data():
    data = request.form['data']
    # Здесь можно выполнить необходимые действия с данными
    # Например, считать данные с COM-порта и отправить ответ
    # Замените этот код на вашу логику
    response_data = "Received data: " + data
    return response_data

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
    app.run(host='0.0.0.0', port=8000)
