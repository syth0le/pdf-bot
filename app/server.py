from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config import BotConfig
from app.middleware import AccessMiddleware
from app.pdf import pdf_main

bot = Bot(token=BotConfig.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(middleware=AccessMiddleware(BotConfig.ACCESS_ID))


@dp.message_handler(commands=['start', 'help', 'menu'])
async def send_welcome(message: types.Message):
    await message.answer('hello')


@dp.message_handler(commands=['pdf'])
async def get_request_for_pdf(message: types.Message):
    await message.answer('send your files:')


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    photo = message.photo.pop()
    custom_path = f"static/images/{photo['file_id'][:30]}.jpg"  # use timestamp
    await photo.download(custom_path)


@dp.message_handler(commands=['test'])
async def send_pdf(message: types.Message):
    name = pdf_main()
    try:
        await bot.send_document(message.chat.id, open(name, 'rb'))
    except FileNotFoundError:
        await bot.send_message(message.chat.id, name)
