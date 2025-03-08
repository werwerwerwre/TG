import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "8180295943:AAGZ1JjijnFz_52p59aE_oS6bEANEuRSGHg"  # Замініть на свій токен бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_text(message: Message):
    try:
        with open("Text.txt", "r", encoding="utf-8") as file:
            text = file.read()
        await message.answer(text)
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        await message.answer("Не вдалося прочитати файл.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
