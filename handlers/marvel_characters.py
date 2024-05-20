from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.common_keyboards import main_keyboard
from states.common_states import UserStates
import web_scraping
import json


try:
    with open("../json_data_files/marvel_character_data.json", "r", encoding="utf-8") as json_file:
        characters_data = json.load(json_file)
except:
    web_scraping.get_marvel_characters()
    with open("../json_data_files/marvel_character_data.json", "r", encoding="utf-8") as json_file:
        characters_data = json.load(json_file)

