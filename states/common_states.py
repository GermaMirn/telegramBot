from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    userChooseButton = State()
    userChooseCity = State()