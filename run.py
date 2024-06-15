import aiogram
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token = TOKEN)

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!") 

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Это команда /help!") 


@dp.message(F.text == "как дела?")
async def how_are_you(message: Message):
    await message.answer("Ok!")

@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

@dp.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAOfZm1m8hsHwai828RvQpYaKZ1jMSAAArfXMRvT_WhL6A3ZiU0wC8ABAAMCAANtAAM1BA",
                               caption = "РОООССИИИЯЯЯЯЯЯЯЯ!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")