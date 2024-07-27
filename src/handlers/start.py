from src.utils import *
from src.keyboards import Exit
from src.static import START_MESSAGE

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


@dp.message(Command("start", ignore_mention=False))
async def start_command(msg: Message, state: FSMContext):
    await msg.answer(START_MESSAGE, reply_markup=Exit().get_kb())