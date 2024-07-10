import asyncio
import logging

import redis
from aiogram.fsm.state import StatesGroup, State

from telegram_part.config import TOKEN
from telegram_part.Users import Admin, Player, User, Referee, Trainer
from telegram_part.Users import auntendefication
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command, Message
from aiogram import F
from aiogram.types import ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.utils.markdown import hide_link
from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types import InputFile

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start

# СТАРТ


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="профиль")],
        [types.KeyboardButton(text="Рейтинг")],
        [types.KeyboardButton(text="Запись на турнир")],
        [types.KeyboardButton(text="КОФНТ")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("Привет! Я бот Калининградской областной федерации настольного тенниса,\
     могу выполнять различные функции, которые помогут вашей спортивной карьере!\nВыберете пункт из\
      предоставленных, чтобы получить нужную для вас информацию.\n❗ Я ругаюсь матом! Если тебя это не\
       устраивает – не пользуйся ботом", reply_markup=keyboard)


# КОФНТ
@dp.message(F.text.lower() == "кофнт")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="Архив")],
        [types.KeyboardButton(text="судейский корпус")],
        [types.KeyboardButton(text="Уважаемые люди")],
        [types.KeyboardButton(text="Общая стата")],
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("в это разделе вы можете получить подробную информацию о Калининградской \
    областной федерации настольного тенниса.", reply_markup=keyboard)


@dp.message(F.text.lower() == "архив")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="результаты")],
        [types.KeyboardButton(text="документы федерации")],
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("конкретику пж", reply_markup=keyboard)


@dp.message(F.text.lower() == "результаты")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("BlueLock 4 - 3 U20", reply_markup=keyboard)


@dp.message(F.text.lower() == "документы федерации")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("все официально", reply_markup=keyboard)


@dp.message(F.text.lower() == "уважаемые люди")
async def cmd_start(message: types.Message):
    text = (f"Президент РФСОО КОФТН — Георгий Рубинштейн\n\n"
            f"Исполнительный директор  — Олеся Скаленко\n\n"
            f"Направления деятельности:\n\n"
            f"МАУ ДO СШ №7 — Татьяна Земецкене\n"
            f"ДЮСШ «Янтарь» — Юлия Иванищева\n"
            f"Ответственный за новый зал — Олег Пешко\n"
            f"Учебно-методическая деятельность (тренеры КОФНТ) —  Олег Пешко, Василий Скаленко\n"
            f"Детский спорт в г. Калининград — Ольга Тесля\n"
            f"Детский спорт в Калининградской области  — Валерий Акимов\n"
            f"Ветеранский спорт — Лев Анисимов\n"
            f"Любительский спорт  — Олег Пасичник\n"
            f"Настольный теннис «Восток» Калининградской области  — Леонид Воронцов\n"
            f"Маркетинговые коммуникации, реклама — Сергей Рябков\n"
            f"IT- поддержка и инфраструктура  — Вадим Гнатюк\n"
            f"Судейский корпус   — Владимир Крапивин")
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer(text, reply_markup=keyboard)


@dp.message(F.text.lower() == "общая стата")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("все проигрываем в нулину", reply_markup=keyboard)


@dp.message(F.text.lower() == "судейский корпус")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("судей на мыло", reply_markup=keyboard)




# @dp.message(F.data == "профиль")
# def ApplyToRegistraition(message: types.Message):

# @dp.message(F.text.lower() == "профиль")
#
# @dp.callback_query(F.data == "reg")
# async def send_random_value(callback: types.CallbackQuery):
#     user = User(callback.message.from_user.id)
#
#     await callback.message.answer("напишите свою имя фамилию и номер телефона через пробел")


@dp.message(F.text.lower() == "профиль")
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()

    user = auntendefication(message.from_user.id)
    ApplyToRegistraition = user.isUserSignIn()

    if ApplyToRegistraition is False:
        builder.add(types.InlineKeyboardButton(
            text="зарегистрироваться",
            callback_data="reg")
        )
        builder.add(types.InlineKeyboardButton(
            text="выбор игрока",
            callback_data="random_value2")
        )
        await message.answer(
            "Вы не зарегистрированы \nВыберете пункт меню",
            reply_markup=builder.as_markup()
        )
    if ApplyToRegistraition is True:
        procfile = user.getProcfile()
        builder.add(types.InlineKeyboardButton(
            text="Мои матчи",
            callback_data="random_value3")
        )
        builder.add(types.InlineKeyboardButton(
            text="выбор игрока",
            callback_data="random_value2")
        )
        await message.answer(
            f"Здравствуйте! {user.surname} {user.name}\n"
            f"Год рождения: {procfile.year}\n"
            f"Пол: {procfile.gender}\n"
            f"KOFNT: {procfile.rateKOFNT}\n"
            f"FNTR: {procfile.rateFNTR}\n"
            f"Категория: {procfile.category}",
            reply_markup=builder.as_markup()
        )

router = Router()
class WriteName(StatesGroup):
    writes_name = State()

@router.message
@dp.callback_query(F.data == "random_value2")
async def send_random_value(callback: types.CallbackQuery):

    wb = [
        [types.KeyboardButton(text="его матчи")],
        [types.KeyboardButton(text="топ 10")],
        [types.KeyboardButton(text="против кого он играет")],
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await callback.message.answer("что вы хотите узнать о человеке", reply_markup=keyboard)


@dp.message(F.text.lower() == "его матчи")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("матчи были улет", reply_markup=keyboard)


@dp.message(F.text.lower() == "против кого он играет")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("играет против баранова", reply_markup=keyboard)


@dp.callback_query(F.data == "random_value3")
async def send_random_value(callback: types.CallbackQuery):
    wb = [
        [types.KeyboardButton(text="мои матчи")],
        [types.KeyboardButton(text="топ 10")],
        [types.KeyboardButton(text="против кого играю")],
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await callback.message.answer("что вы хотите узнать о себе", reply_markup=keyboard)


@dp.message(F.text.lower() == "мои матчи")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("ты молодец", reply_markup=keyboard)


@dp.message(F.text.lower() == "против кого играю")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("играю против всех\n будет реализовано в следующем обновлении", reply_markup=keyboard)


@dp.callback_query(F.data == "random_value1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("напишите свою имя фамилию и номер телефона через пробел")


@dp.message(F.text.lower() == "топ 10")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("топ 1: атон аранов\n и тд", reply_markup=keyboard)



# Рейтинг
@dp.message(F.text.lower() == "рейтинг")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("топ 1: атон аранов\n и тд", reply_markup=keyboard)


# Запись на турнир
@dp.message(F.text.lower() == "запись на турнир")
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Подготовка файла к турниру",
        url='https://youtu.be/m4QO5jyEw2E?si=WIw64UEkKjZfHY_t',
        callback_data="random_value1")
    )
    builder.add(types.InlineKeyboardButton(
        text="Переход на гугл форму",
        url='https://www.youtube.com/watch?v=r0k5CxR0pys&t=337s&ab_channel=CoupleGuys',
        callback_data="random_value2")
    )
    await message.answer(
        "здесь реализуется запись на турнир!",
        reply_markup=builder.as_markup()
    )

# на главную
@dp.message(F.text.lower() == "на главную")
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="профиль")],
        [types.KeyboardButton(text="Рейтинг")],
        [types.KeyboardButton(text="Запись на турнир")],
        [types.KeyboardButton(text="КОФНТ")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("Я бот Калининградской областной федерации настольного тенниса,\
     могу выполнять различные функции, которые помогут вашей спортивной карьере!\nВыберете пункт из\
      предоставленных, чтобы получить нужную для вас информацию.\n❗ Я ругаюсь матом! Если тебя это не\
       устраивает – не пользуйся ботом", reply_markup=keyboard)


# id and username
@dp.message(Command("id"))
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.from_user.first_name)


# @dp.message(Command("username"))
# async def get_username(message: types.Message):
#     username = message.from_user.username
#     await message.answer(f"{username}")
#
#
# @dp.message(Command("userid"))
# async def getuserid(message: types.Message):
#     user_id = message.from_user.id
#     await message.answer(f"{user_id}")

@dp.callback_query(F.data == "Approve")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Добре, давай админчик добавь его id в Excel ты справишься!X)")
    #надо подумать как сделать так чтобы после нажатия кнопки оно добавляло пользователя в ексель

# async def applicationMessageToAdmin():
#     builder = InlineKeyboardBuilder()
#     tids, text =Admin.getApplicationToReg()
#     builder.add(types.InlineKeyboardButton(
#         text="Принять",
#         callback_data="Approve")
#     )
#     await bot.send_message(tid,
#         text=text,
#         reply_markup=builder.as_markup()
#     )
#
# async def sendToUser(tid, text):
#     await bot.send_message(tid, text)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
