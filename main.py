# name: @firstNameOOkbot
from aiogram import Bot, Dispatcher
import asyncio
from handlers import other_handlers, weather_by_city


async def main():
    bot = Bot(token="6733151814:AAGf5aFXhfelVk8fOF37jNoy0En9QCDTzGg")
    dp = Dispatcher()
    dp.include_routers(other_handlers.router, weather_by_city.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
