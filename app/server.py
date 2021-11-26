from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config import BotConfig

bot = Bot(token=BotConfig.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# dp.middleware.setup(middleware=AccessMiddleware(BotConfig.ACCESS_ID))


@dp.message_handler(commands=['start', 'help', 'menu'])
async def send_welcome(message: types.Message):
    await message.answer('hello')


@dp.message_handler(commands=['pdf'])
async def send_welcome(message: types.Message):
    await message.answer('send your files:')


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    photo = message.photo.pop()
    await photo.download(photo['file_id'], destination='images')
    # rez = []
    # i = 0
    # for item in message.photo:
    #     temp = f'{random.uniform(1, 100000)}'
    #     # item.download(temp, destination='images')
    #     i += 1
    #     print(i, item)
    #     rez.append(item['file_id'])

    # await message.answer(i)
