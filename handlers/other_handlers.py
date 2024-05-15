from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.common_keyboards import main_keyboard
from states.common_states import UserStates


router = Router()


@router.message(Command("test"))
async def test_message(message: Message):
    await message.answer("Привет!!!")

@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(
        text="Узнайте информацию про любой город:",
        reply_markup=main_keyboard()
    )

    await state.set_state(UserStates.userChooseButton)
    # https://api.openweathermap.org/data/2.5/weather?q=Kaliningrad&appid=8def4781f2e941565e4ddf3a381bb60b&units=metric