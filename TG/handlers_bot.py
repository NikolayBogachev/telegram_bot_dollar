
from aiogram import F, Router

from aiogram.filters import CommandStart, StateFilter

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ForceReply

from loguru import logger

from TG.bot import bot
from TG.funcs import get_usd_rate

router = Router()


# Обработчик нового чата с ботом
@router.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("Добрый день. Как вас зовут?")


@router.message()
async def get_name(message: Message):
    name = message.text
    usd_rate = get_usd_rate()  # Получаем курс доллара
    await message.answer(f"Рад знакомству, {name}! Курс доллара сегодня {usd_rate}р")
