from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F, Bot
from aiogram.utils.keyboard import InlineKeyboardBuilder
from redis.asyncio import Redis, ConnectionPool
import redis

from core.telegram_part.keyboards.keyboards import admin_buttons
from core.telegram_part.utils.Users import User, Admin, StatusRegistration
from core.telegram_part.utils.settings import settings


class Registration(StatesGroup):
    writingName = State()
    writingPhoneNum = State()


async def registration(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Зарегистрироваться",
        callback_data="reg")
    )
    await message.answer(
        "Вы не зарегистрированы,\nесли вы являетесь спортсменом федерации зарегистрируйтесь,\n"
        "иначе выберите игрока интересующего спортсмена",
        reply_markup=builder.as_markup()
    )


async def beginning(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Напишите свое ФИО через пробел")
    await state.set_state(Registration.writingName)


async def getUserName(message: Message, state: FSMContext):
    if User.checkFullName(message.text):
        await state.set_data({'name': message.text})
        await message.answer('Напишите ваш номер телефона: ')
        await state.set_state(Registration.writingPhoneNum)
    else:
        await message.answer("Некорректное имя. Напишите свое ФИО через пробел снова:")


async def getUserPhone(message: Message, state: FSMContext, user: User, bot: Bot, db: Redis):
    num = str(message.text)
    data = await state.get_data()
    if User.checkPhoneNumber(num):
        await user.signIn(message.from_user.id, data['name'], num, db=db)
        await sendAdmins(message, bot, db)
        await state.clear()
        await message.answer("Ваши данные находятся на рассмотрении.\nВам придет уведомление об состоянии заявления =)")
    else:
        await message.answer("Некорректный номер. Напишите снова:")


async def sendAdmins(message: Message, bot: Bot, db: Redis):
    text = await Admin.getApplicationToReg(message.from_user.id, db)  # message.from_user.id test
    admins = settings.bots.admin_id  # test
    for tid in admins:
        markup = InlineKeyboardMarkup(inline_keyboard=admin_buttons)
        await bot.send_message(tid, text, reply_markup=markup)
