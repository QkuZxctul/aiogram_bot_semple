from src.utils import *
from src.utils.filters import AdminFilter
from src.keyboards import Exit
from src.static import ADMINS_START_MESSAGE

from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


@dp.message(Command("admin", ignore_mention=False), AdminFilter())
async def admins_start(msg: Message, state: FSMContext):
    await msg.answer(ADMINS_START_MESSAGE, reply_markup=Exit().get_kb())
