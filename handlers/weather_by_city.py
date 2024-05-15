from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.common_keyboards import main_keyboard
from states.common_states import UserStates
# import aiohttp  # request this modul can't do async then aiohttp
import requests


router = Router()

@router.message(F.text == "Погода", UserStates.userChooseButton)
async def get_city_name(message: Message, state: FSMContext):
    await message.answer(
        text = "Введите название города: ",
        reply_markup = ReplyKeyboardRemove()
    )

    await state.set_state(UserStates.userChooseCity)

@router.message(F.text, UserStates.userChooseCity)
async def get_city_weather(message: Message, state: FSMContext):
    city = message.text
    urlWithCity = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8def4781f2e941565e4ddf3a381bb60b&units=metric&lang=ru"

    weather_data = requests.get(url=urlWithCity).json()
    await message.answer(
        text=f"Описание: {weather_data['weather'][0]['description']};\n"
             f"температура: {weather_data['main']['temp']};\n"
    )

    # async with aiohttp.ClientSession as session:
    #     urlWithCity = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8def4781f2e941565e4ddf3a381bb60b&units=metric"
    #     async with session.get(url=urlWithCity) as response:
    #         weather_data = await response.text()
    #         print(weather_data)
