# import serial
# import requests
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
# from aiogram.dispatcher import FSMContext
#
# API_TOKEN = 'YOUR_BOT_TOKEN'
#
# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
# logging.basicConfig(level=logging.INFO)
# dp.middleware.setup(LoggingMiddleware())
#
# # Здесь задайте значение символа ACK, который ожидается от устройства
# ACK = b'\x06'  # Пример: ASCII-символ ACK имеет код 0x06
#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.reply("Привет! Я готов к работе. Используйте команды /open, /read, /close и /senddata.")
#
# @dp.message_handler(commands=['open'])
# async def open_port(message: types.Message):
#     # Здесь выполните открытие COM-порта и другие действия
#     user_id = message.from_user.id
#     # Сохраняем объект serial.Serial в состояние FSM
#     await message.reply("COM-порт открыт.", reply=False)
#     await YourStateName.waiting_for_data.set()
#
# @dp.message_handler(commands=['read'])
# async def read_data(message: types.Message, state: FSMContext):
#     # Здесь выполните считывание данных с COM-порта и другие действия
#     user_id = message.from_user.id
#     data = # Ваш код для считывания данных
#     await message.reply(f"Считанные данные: {data}")
#
# @dp.message_handler(commands=['close'])
# async def close_port(message: types.Message, state: FSMContext):
#     # Здесь выполните закрытие COM-порта и другие действия
#     user_id = message.from_user.id
#     await message.reply("COM-порт закрыт.")
#
# @dp.message_handler(commands=['senddata'])
# async def send_data(message: types.Message, state: FSMContext):
#     # Здесь выполните отправку данных на сервер и другие действия
#     user_id = message.from_user.id
#     base, app, pacient_id = message.get_args().split()
#     data = # Ваш код для получения данных
#     mindray_server = "http://217.29.26.60/med_aparats/parser.php"
#     payload = {'base': base, 'app': app, 'pacient_id': pacient_id, 'data': data.decode('iso-8859-1')}
#     response = requests.post(mindray_server, data=payload)
#     await message.reply(f"Ответ от сервера: {response.text}")
#
# if __name__ == '__main__':
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)




import serial
import requests
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

API_TOKEN = 'YOUR_BOT_TOKEN'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())

# Определение состояний
class YourStateName1(State):
    """Описание состояния 1"""

class YourStateName2(State):
    """Описание состояния 2"""

# Здесь задайте значение символа ACK, который ожидается от устройства
ACK = b'\x06'  # Пример: ASCII-символ ACK имеет код 0x06

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я готов к работе. Используйте команды /open, /read, /close и /senddata.")

@dp.message_handler(commands=['open'])
async def open_port(message: types.Message, state: FSMContext):
    # Здесь выполните открытие COM-порта и другие действия
    user_id = message.from_user.id
    # Сохраняем объект serial.Serial в состояние FSM
    await message.reply("COM-порт открыт.", reply=False)
    await YourStateName1.waiting_for_data.set()

@dp.message_handler(commands=['read'])
async def read_data(message: types.Message, state: FSMContext):
    # Здесь выполните считывание данных с COM-порта и другие действия
    user_id = message.from_user.id
    # Вам нужно добавить код для считывания данных с COM-порта
    data = "Пример данных, считанных с COM-порта"
    await message.reply(f"Считанные данные: {data}")

@dp.message_handler(commands=['close'])
async def close_port(message: types.Message, state: FSMContext):
    # Здесь выполните закрытие COM-порта и другие действия
    user_id = message.from_user.id
    # Вам нужно добавить код для закрытия COM-порта
    await message.reply("COM-порт закрыт.")

@dp.message_handler(commands=['senddata'])
async def send_data(message: types.Message, state: FSMContext):
    # Здесь выполните отправку данных на сервер и другие действия
    user_id = message.from_user.id
    base, app, pacient_id = message.get_args().split()
    # Вам нужно добавить код для получения данных с COM-порта
    data = "Пример данных для отправки на сервер"
    mindray_server = "http://217.29.26.60/med_aparats/parser.php"
    payload = {'base': base, 'app': app, 'pacient_id': pacient_id, 'data': data}
    response = requests.post(mindray_server, data=payload)
    await message.reply(f"Ответ от сервера: {response.text}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
