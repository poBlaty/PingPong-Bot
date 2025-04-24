from aiogram import types

from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.telegram_part.utils.Users import StatusRegistration, User, Competition, Player, Admin
from core.telegram_part.keyboards.keyboards import main, common, wb, back, keyboard_back, keyboard_common, \
    keyboard_main, keyboard_wb, keyboard_direct


async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я бот Калининградской областной федерации настольного тенниса,"
        "могу выполнять различные функции, которые помогут вашей спортивной карьере!\n"
        "Выберете пункт из предоставленных, чтобы получить нужную для вас информацию.❗\n",
        reply_markup=keyboard_main)


async def to_main(message: types.Message):
    await message.answer("Главные функции:", reply_markup=keyboard_main)


# КОФНТ
async def to_KOFNT(message: types.Message):
    await message.answer("В это разделе вы можете получить подробную информацию о КОФНТ.", reply_markup=keyboard_common)


async def archive(message: types.Message):
    await message.answer("Выберите:", reply_markup=keyboard_wb)


async def management(message: types.Message):
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

    await message.answer(text, reply_markup=keyboard_back)


# async def general_statistics(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=back,
#         resize_keyboard=True,
#         input_field_placeholder="Выберите пункт меню:"
#     )
#     data = Admin.getCommonData()
#
#     await message.answer(f"Статистика КОФНТ за 2024-й год:\n"
#                          f"Всего было сыграно {data.comps} соревнований\n"
#                          f"На них игроки разыграли:\n"
#                          f"{data.matches} матчей, {data.sets} партий, {data.points} очков", reply_markup=keyboard)
#
#
# async def results_of_competitions(message: types.Message, user: User = None):
#     builder = InlineKeyboardBuilder()
#     if user.__class__ is Admin:
#         builder.add(types.InlineKeyboardButton(
#             text="Залить файлы",
#             callback_data="result")
#         )
#     builder.add(types.InlineKeyboardButton(
#         text="Получить результаты",
#         callback_data="result")
#     )
#     await message.answer(
#         "Результаты соревнования",
#         reply_markup=builder.as_markup()
#     )
#
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=back,
#         resize_keyboard=True,
#         input_field_placeholder="выберите пункт меню:"
#     )


# async def documents(message: types.Message):
#     user = auntendefication(message.from_user.id)
#     builder = InlineKeyboardBuilder()
#     if user.__class__ is Admin:
#         builder.add(types.InlineKeyboardButton(
#             text="Залить файлы",
#             callback_data="docs")
#         )
#     builder.add(types.InlineKeyboardButton(
#         text="Получить документы",
#         callback_data="docs")
#     )
#     await message.answer(
#         "Документы федерации",
#         reply_markup=builder.as_markup()
#     )
#
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=back,
#         resize_keyboard=True,
#         input_field_placeholder="Выберите пункт меню:"
#     )


# async def best_matches(message: types.Message):
#     user = auntendefication(message.from_user.id)  # message.from_user.id
#
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=back,
#         resize_keyboard=True,
#         input_field_placeholder="выберите пункт меню:"
#     )
#
#     if user.__class__ in (Player, Admin):
#         matches = user.getbestWins()
#         text = f"Лучшие матчи {user.surname + ' ' + user.name}:\n\n"
#         for i in matches:
#             text += (f"{i.name}\n"
#                      f"{i.player_1} {i.rating_1} {i.score} {i.rating_2} {i.player_2} {i.result_parties}\n\n")
#         await message.answer(text, reply_markup=keyboard)
#     else:
#         await message.answer("У вас нема доступа Ж(", reply_markup=keyboard)


# async def last_matches(message: types.Message, user: User):
#     if user.__class__ in (Player, Admin):
#         comp: Competition = user.getLastMatches()
#         text = (f'Последние матчи {user.surname + " " + user.name}:\n\n'
#                 f'{comp.name} \n\n')
#         for i in comp.plays:
#             text += f"{i.player_1} {i.score} {i.player_2} {i.result_parties}\n"
#         await message.answer(text, reply_markup=keyboard)
#     else:
#         await message.answer("У вас нема доступа Ж(", reply_markup=keyboard)


async def profile(message: types.Message, user: User):  # 400063942
    procfile = user.getProcfile()
    await message.answer("Что вы хотите узнать о себе", reply_markup=keyboard_direct)
    await message.answer(
        f"ФИ: {user.surname} {user.name}\n"
        f"Дата рождения: {procfile.year}\n"
        f"Пол: {procfile.gender}\n"
        f"КОФНТ: {procfile.rateKOFNT} ({procfile.place})\n"
        f"ФНТР: {procfile.rateFNTR}\n"
        f"Категория: {procfile.category} разряд"
    )

# async def against(message: types.Message):  # против кого он играет
#
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=back,
#         resize_keyboard=True,
#         input_field_placeholder="выберите пункт меню:"
#     )
#     await message.answer("играет против баранова", reply_markup=keyboard)

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


# @dp.message(F.text.lower() == "его матчи")
# async def cmd_start(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=back,
#         resize_keyboard=True,
#         input_field_placeholder="Выберите пункт меню:"
#     )
#     await message.answer("матчи были улет", reply_markup=keyboard)
#
#


async def getRating(message: types.Message, user: User): # 1134175573
    rating_list = user.getRating()
    print(rating_list)
    if len(rating_list) == 0:
        await message.answer("У вас рейтинга нема Ж(")
    else:
        await message.answer(f"Рейтинг игрока {user.surname} {user.name} за последние 12 месяцев:",
                             reply_markup=keyboard_back)
        for data in rating_list:
            await message.answer(
                f"{data.mouth_year}, Рейтинг: {data.listRaiting.raiting}, Место: {data.listRaiting.place}")

#
# # Запись на турнир
# @dp.message(F.text.lower() == "запись на турнир")
# async def cmd_random(message: types.Message):
#     builder = InlineKeyboardBuilder()
#     builder.add(types.InlineKeyboardButton(
#         text="Переход на гугл форму",
#         url='https://docs.google.com/forms/d/1UiUhwl51Ci4BRPoYXwXxwwWHarH-nI5qYwMj7bBUZg8/closedform')
#     )
#     await message.answer(
#         "Выберите соревнования для регистрации ниже:",
#         reply_markup=builder.as_markup()
#     )
