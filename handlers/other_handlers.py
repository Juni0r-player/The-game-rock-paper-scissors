"""модуль для хранения хэндлера, который будет обрабатывать сообщения, не предусмотренные в рамках общения пользователя с ботом"""
from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router = Router()

# Хендлер для сообщений, которые не попали в другие хендлеры
@router.message()
async def send_acnswer_other_message(message: Message):
     await message.answer(text=LEXICON_RU['other_answer'])