from src.utils import ADMIN_ID

from aiogram.filters import BaseFilter
from aiogram.types import Message

class AdminFilter(BaseFilter):
    async def __call__(self, msg: Message):
        return msg.from_user.id == ADMIN_ID