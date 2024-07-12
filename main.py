import asyncio
import logging

import os

from telegram_part.config import TOKEN
from telegram_part.Users import Admin, Player, User, Referee, Trainer, PlaceInRating, UserRating, Competition
from telegram_part.Users import auntendefication
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command, Message
from aiogram import F
from aiogram.types import ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.utils.markdown import hide_link
from aiogram.types import FSInputFile, Message

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
    user = auntendefication(message.from_user.id)
    kb = [
        [types.KeyboardButton(text="Профиль")],
        [types.KeyboardButton(text="Запись на турнир")],
        [types.KeyboardButton(text="КОФНТ")]
    ]
    if user.__class__ != User:
        kb.insert(2, [types.KeyboardButton(text="Рейтинг")])
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )
    await message.answer("Привет! Я бот Калининградской областной федерации настольного тенниса,"
                         "могу выполнять различные функции, которые помогут вашей спортивной карьере!\nВыберете пункт из"
                         "предоставленных, чтобы получить нужную для вас информацию.❗\n", reply_markup=keyboard)


@dp.message(F.text.lower() == "на главную")
async def cmd_start(message: types.Message):
    user = auntendefication(message.from_user.id)
    kb = [
        [types.KeyboardButton(text="Профиль")],
        [types.KeyboardButton(text="Запись на турнир")],
        [types.KeyboardButton(text="КОФНТ")]
    ]
    if user.__class__ != User:
        kb.insert(2, [types.KeyboardButton(text="Рейтинг")])
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )
    await message.answer("Главные функции:", reply_markup=keyboard)


# КОФНТ
@dp.message(F.text.lower() == "кофнт")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="Архив")],
        [types.KeyboardButton(text="Управление")],
        [types.KeyboardButton(text="Общая статистика")],
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )
    await message.answer("В это разделе вы можете получить подробную информацию о КОФНТ.", reply_markup=keyboard)


@dp.message(F.text.lower() == "архив")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="Результаты соревнований")],
        [types.KeyboardButton(text="Документы федерации")],
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )
    await message.answer("Выберите:", reply_markup=keyboard)


@dp.message(F.text.lower() == "управление")
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
        input_field_placeholder="Выберите пункт меню:"
    )
    await message.answer(text, reply_markup=keyboard)


@dp.message(F.text.lower() == "общая статистика")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )
    data = Admin.getCommonData()

    await message.answer(f"Статистика КОФНТ за 2024-й год:\n"
                         f"Всего было сыграно {data.comps} соревнований\n"
                         f"На них игроки разыграли:\n"
                         f"{data.matches} матчей, {data.sets} партий, {data.points} очков", reply_markup=keyboard)


@dp.callback_query(F.data == "result")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Подождите немного, файл грузится...")
    count = 0
    for i in os.listdir("data/КОФНТ/Архив/Результаты соревнований/2024"):
        if count < 3:
            await callback.message.answer_document(document=FSInputFile(
                f"data/КОФНТ/Архив/Результаты соревнований/2024/{i}"))


@dp.message(F.text.lower() == "результаты соревнований")
async def cmd_start(message: types.Message):
    user = auntendefication(message.from_user.id)
    builder = InlineKeyboardBuilder()
    if user.__class__ is Admin:
        builder.add(types.InlineKeyboardButton(
            text="Залить файлы",
            callback_data="result")
        )
    builder.add(types.InlineKeyboardButton(
        text="Получить результаты",
        callback_data="result")
    )
    await message.answer(
        "Результаты соревнования",
        reply_markup=builder.as_markup()
    )
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выберите пункт меню:"
    )


@dp.callback_query(F.data == "docs")
async def send_random_value(callback: types.CallbackQuery):
    for i in os.listdir("data/КОФНТ/Архив/Документы федерации"):
        await callback.message.answer_document(document=FSInputFile(
            f"data/КОФНТ/Архив/Документы федерации/{i}"))


@dp.message(F.text.lower() == "документы федерации")
async def cmd_start(message: types.Message):
    user = auntendefication(message.from_user.id)
    builder = InlineKeyboardBuilder()
    if user.__class__ is Admin:
        builder.add(types.InlineKeyboardButton(
            text="Залить файлы",
            callback_data="docs")
        )
    builder.add(types.InlineKeyboardButton(
        text="Получить документы",
        callback_data="docs")
    )
    await message.answer(
        "Документы федерации",
        reply_markup=builder.as_markup()
    )
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )

    # await message.answer("все официально", reply_markup=keyboard)


# @dp.message(F.data == "профиль")
# def ApplyToRegistraition(message: types.Message):

# @dp.message(F.text.lower() == "профиль")
#
# @dp.callback_query(F.data == "reg")
# async def send_random_value(callback: types.CallbackQuery):
#     user = User(callback.message.from_user.id)
#
#     await callback.message.answer("напишите свою имя фамилию и номер телефона через пробел")

@dp.message(F.text.lower() == "лучшие матчи")
async def cmd_start(message: types.Message):
    user = auntendefication(message.from_user.id)  # message.from_user.id
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выберите пункт меню:"
    )

    if user.__class__ in (Player, Admin):
        matches = user.getbestWins()
        text = f"Лучшие матчи {user.surname + ' ' + user.name}:\n\n"
        for i in matches:
            text += (f"{i.name}\n"
                     f"{i.player_1} {i.rating_1} {i.score} {i.rating_2} {i.player_2} {i.result_parties}\n\n")
        await message.answer(text, reply_markup=keyboard)
    else:
        await message.answer("У вас нема доступа Ж(", reply_markup=keyboard)


@dp.message(F.text.lower() == "последние матчи")
async def cmd_start(message: types.Message):
    user = auntendefication(message.from_user.id)

    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )

    if user.__class__ in (Player, Admin):
        comp: Competition = user.getLastMatches()
        text = (f'Последние матчи {user.surname + " " + user.name}:\n\n'
                f'{comp.name} \n\n')
        for i in comp.plays:
            text += f"{i.player_1} {i.score} {i.player_2} {i.result_parties}\n"
        await message.answer(text, reply_markup=keyboard)
    else:
        await message.answer("У вас нема доступа Ж(", reply_markup=keyboard)


# @dp.callback_query(F.data == "my_matches")
# async def send_random_value(callback: types.CallbackQuery):
#     wb = [
#         [types.KeyboardButton(text="Последние матчи")],
#         [types.KeyboardButton(text="Топ 10")],
#         # [types.KeyboardButton(text="против кого играю")],
#         [types.KeyboardButton(text="На главную")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=wb,
#         resize_keyboard=True,
#         input_field_placeholder="Выберите пункт меню:"
#     )
#     await callback.message.answer("Что вы хотите узнать о себе", reply_markup=keyboard)


@dp.message(F.text.lower() == "профиль")
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()

    user = auntendefication(message.from_user.id)
    ApplyToRegistraition = user.isUserSignIn()
    print(ApplyToRegistraition)
    if ApplyToRegistraition is False:
        builder.add(types.InlineKeyboardButton(
            text="Зарегистрироваться",
            callback_data="reg")
        )
        # builder.add(types.InlineKeyboardButton(
        #     text="выбор игрока",
        #     callback_data="random_value2")
        # )
        await message.answer(
            "Вы не зарегистрированы \nВыберете пункт меню",
            reply_markup=builder.as_markup()
        )
    if ApplyToRegistraition is True:
        procfile = user.getProcfile()
        wb = [
            [types.KeyboardButton(text="Последние матчи")],
            [types.KeyboardButton(text="Лучшие матчи")],
            # [types.KeyboardButton(text="против кого играю")],
            [types.KeyboardButton(text="На главную")]
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=wb,
            resize_keyboard=True,
            input_field_placeholder="Выберите пункт меню:"
        )
        await message.answer("Что вы хотите узнать о себе", reply_markup=keyboard)
        # builder.add(types.InlineKeyboardButton(
        #     text="выбор игрока",
        #     callback_data="random_value2")
        # )
        await message.answer(
            f"ФИ: {user.surname} {user.name}\n"
            f"Дата рождения: {procfile.year}\n"
            f"Пол: {procfile.gender}\n"
            f"КОФНТ: {procfile.rateKOFNT} ({procfile.place})\n"
            f"ФНТР: {procfile.rateFNTR}\n"
            f"Категория: {procfile.category} разряд",
            reply_markup=builder.as_markup()
        )


# @dp.callback_query(F.data == "random_value2")
# async def send_random_value(callback: types.CallbackQuery):
#     wb = [
#         [types.KeyboardButton(text="Его матчи")],
#         [types.KeyboardButton(text="Топ 10")],
#         [types.KeyboardButton(text="Против кого он играет")],
#         [types.KeyboardButton(text="На главную")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=wb,
#         resize_keyboard=True,
#         input_field_placeholder="Выберите пункт меню:"
#     )
#     await callback.message.answer("Что вы хотите узнать о человеке", reply_markup=keyboard)


@dp.message(F.text.lower() == "против кого он играет")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выберите пункт меню:"
    )
    await message.answer("играет против баранова", reply_markup=keyboard)


# @dp.message(F.text.lower() == "против кого играю")
# async def cmd_start(message: types.Message):
#     wb = [
#         [types.KeyboardButton(text="На главную")]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=wb,
#         resize_keyboard=True,
#         input_field_placeholder="выберите пункт меню:"
#     )
#     await message.answer("играю против всех\n будет реализовано в следующем обновлении", reply_markup=keyboard)

@dp.message(F.text.lower() == "его матчи")
async def cmd_start(message: types.Message):
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )
    await message.answer("матчи были улет", reply_markup=keyboard)


# Рейтинг
@dp.message(F.text.lower() == "рейтинг")
async def cmd_start(message: types.Message):
    user = auntendefication(message.from_user.id)  # 1134175573
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )
    rating_list = user.getRating()
    if len(rating_list) == 0:
        await message.answer("У вас рейтинга нема Ж(")
    else:
        await message.answer(f"Рейтинг игрока {user.surname} {user.name} за последние 12 месяцев:",
                             reply_markup=keyboard)
        for data in rating_list:
            await message.answer(
                f"{data.mouth_year}, Рейтинг: {data.listRaiting.raiting}, Место: {data.listRaiting.place}")


@dp.callback_query(F.data == "fileToTour")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Подождите файл грузится...")
    await callback.message.answer_document(document=FSInputFile(
        "data/Список соревы/Чемп. КО.xlsm"))


# Запись на турнир
@dp.message(F.text.lower() == "запись на турнир")
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Переход на гугл форму",
        url='https://docs.google.com/forms/d/1UiUhwl51Ci4BRPoYXwXxwwWHarH-nI5qYwMj7bBUZg8/closedform')
    )
    await message.answer(
        "Выберите соревнования для регистрации ниже:",
        reply_markup=builder.as_markup()
    )


# на главную


@dp.callback_query(F.data == "Approve")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("Добре, давай админчик добавь его id в Excel ты справишься!X)")
    # надо подумать как сделать так чтобы после нажатия кнопки оно добавляло пользователя в ексель


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
