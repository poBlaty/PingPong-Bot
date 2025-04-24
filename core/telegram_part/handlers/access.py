from aiogram.types import Message


async def access_denied(message: Message):
    await message.answer("У вас нема доступа Ж(")


async def in_process(message: Message):
    await message.answer("Вы уже подали заявление ожидайте!")

async def banned(message: Message):
    await message.answer("Нэ, ты забанен крыса")
