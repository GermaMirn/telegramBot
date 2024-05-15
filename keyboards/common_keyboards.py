from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import KeyboardButton, InlineKeyboardButton, ReplyKeyboardBuilder


def main_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Погода")
    kb.button(text="Население")
    kb.button(text="Часовой пояс")
    return kb.as_markup(resize_keyboard=True)
