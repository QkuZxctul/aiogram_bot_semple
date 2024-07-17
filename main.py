from src.utils import bot, dp
from src.handlers import *

from asyncio import run

async def start():
    print('bot started')
    await dp.start_polling(bot)

if __name__ == '__main__':
    run(start())