from os import getenv

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

load_dotenv('.env')

TOKEN = getenv('token', '')
ADMIN_ID = int(getenv('admin_id'))

assert TOKEN and ADMIN_ID

bot = Bot(token=TOKEN)
dp = Dispatcher()
