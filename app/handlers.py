from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

#@router.message(CommandStart())
#async def cmd_start(message: Message):
#    await message.answer("Привет!") 

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',
                        reply_markup=kb.main)    

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Это команда /help!") 


@router.message(F.text == "как дела?")
async def how_are_you(message: Message):
    await message.answer("Ok!")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')

@router.message(Command("get_photo"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAOfZm1m8hsHwai828RvQpYaKZ1jMSAAArfXMRvT_WhL6A3ZiU0wC8ABAAMCAANtAAM1BA",
                               caption = "РОООССИИИЯЯЯЯЯЯЯЯ!")

@router.message(Command("photo"))
async def photo(message: Message):
    await message.answer_photo(photo="https://img.freepik.com/free-photo/cyberpunk-warrior-looking-city_23-2150712594.jpg?t=st=1718447316~exp=1718450916~hmac=47a803e94a815b458b1f1dbf6eecec16dfc309e753800d782c4490dbb41a2998&w=360",
                               caption = "РОООССИИИЯЯЯЯЯЯЯЯ!")

@router.message(Command("get_photo2"))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAPHZm2HzNTEy4HnhLFG_J2dAAEac3f1AAJj2DEb0_1oS_6GcX1v5C34AQADAgADbQADNQQ",
                               caption = "Сдавайтесь, КОЖАНЫЕ!!!!")