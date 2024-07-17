from os import getenv

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
load_dotenv('.env')
TOKEN = getenv('token', '')
# ADMIN_ID = getenv('admin_id')
assert TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
