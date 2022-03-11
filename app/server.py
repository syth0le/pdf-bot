import os
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app import constants
from app.config import BotConfig
from app.middleware import AccessMiddleware
from app.pdf import get_pdf

bot = Bot(token=BotConfig.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(middleware=AccessMiddleware(BotConfig.ACCESS_ID))


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(constants.WELCOME)


@dp.message_handler(commands=['help'])
async def send_help_information(message: types.Message):
    await message.answer(constants.HELP_INFORMATION)


@dp.message_handler(commands=['commands'])
async def send_commands(message: types.Message):
    await message.answer(constants.COMMANDS)


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    if photo := message.photo.pop():
        time_for_image = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        chat_id = message.chat.id
        destination_file = os.getcwd() + f"/static/images/{chat_id}/{chat_id}-{time_for_image}-{photo.file_unique_id}.jpg"
        print(destination_file)
        await photo.download(destination_file=destination_file)
        # with open(f"static/images/{chat_id}/{chat_id}-{time_for_image}-{photo.file_unique_id}.jpg", 'wb') as file:
        #     file.write(b'')
        #     file.close()


@dp.message_handler(commands=['conv2pdf'])
async def send_pdf(message: types.Message):
    name = get_pdf(chat_id=message.chat.id)
    try:
        await bot.send_document(message.chat.id, open(name, 'rb'))
        os.remove(name)
    except FileNotFoundError:
        await bot.send_message(message.chat.id, name)
