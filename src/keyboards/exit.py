from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

from src.static import EXIT_TEXT


class Exit(ReplyKeyboardBuilder):
    def __init__(self):
        super().__init__()

    def get_buttons(self):
        return KeyboardButton(text=EXIT_TEXT)
    
    def get_kb(self):
        self.add(self.get_buttons())
        
        return self.as_markup(resize_keyboard=True)