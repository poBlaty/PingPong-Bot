import asyncio
import logging
from telegram_part.config import TOKEN
from telegram_part.Users import Admin, Player, User, Referee, Trainer
from telegram_part.Users import signIn, auth
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, Message
from aiogram import F
from aiogram.types import ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.utils.markdown import hide_link
from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start

# СТАРТ

@auth
@dp.message(Command("start"))
async def cmd_start(message: types.Message, user: User = None):
    print(user.__class__)

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
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer("всех ненавидим", reply_markup=keyboard)


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


# профиль
# попытался сделать что просил леша со словарем
dict = {
    '1134175573': 'егорчик топчик',
    '848311771': 'полинка боева',
    '858380684': 'коля ты дэбил'
}


@dp.message(F.data == "профиль")
def ApplyToRegistraition(message: types.Message):
    user_id = str(message.from_user.id)
    dict_id = dict.keys()
    if user_id not in dict_id:
        return False
    else:
        return True


# я не смог это реализовать
"""def TextRegistraition(message: types.Message):
    user_id = str(message.from_user.id)
    file = str(open('registration.txt'))
    if user_id not in file:
        return False
    else:
        return True"""


@dp.message(F.text.lower() == "профиль")
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    # if signIn(message.from_user.id):

    if ((ApplyToRegistraition(message) == False)):
        builder.add(types.InlineKeyboardButton(
            text="зарегистрироваться",
            callback_data="random_value1")
        )
        builder.add(types.InlineKeyboardButton(
            text="выбор игрока",
            callback_data="random_value2")
        )
        await message.answer(
            "Вы не зарегистрированы \nВыберете пункт меню",
            reply_markup=builder.as_markup()
        )
    if ((ApplyToRegistraition(message) == True)):
        builder.add(types.InlineKeyboardButton(
            text="мой профиль",
            callback_data="random_value3")
        )
        builder.add(types.InlineKeyboardButton(
            text="выбор игрока",
            callback_data="random_value2")
        )
        await message.answer(
            "Что вы хотите узнать о себе?",
            reply_markup=builder.as_markup()
        )


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
    await message.answer("играю против всех", reply_markup=keyboard)


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


"""@dp.message(F.text.lower() == "имя")
async def cmd_start(message: types.Message):
    name = dict.get(str(message.from_user.id))
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await message.answer(str(name), reply_markup=keyboard)"""
""""@dp.message(F.text.lower() == 'внешность')
async def send_photo(message: types.Message):
    photo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4ggL9SDGrEWYe3uCxEF1ynQIjmTcbqxnONQ&s'
    wb = [
        [types.KeyboardButton(text="На главную")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="выбирите пункт меню:"
    )
    await bot.send_photo(message.chat.id, photo, caption='какой красавчик!', reply_markup=keyboard)"""


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


"""@dp.callback_query(F.data == "random_value1")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("https://www.youtube.com/watch?v=r0k5CxR0pys&t=337s&ab_channel=CoupleGuys")

@dp.callback_query(F.data == "random_value2")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer("https://youtu.be/m4QO5jyEw2E?si=WIw64UEkKjZfHY_t")

@dp.message(F.text.lower() == "подготовка файла к турниру")
async def start(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Go to Website', url='https://www.example.com')
    keyboard_markup.add(button)
    await message.answer('Click the button to visit the website:', reply_markup=keyboard_markup)
"""


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


@dp.message(Command("username"))
async def get_username(message: types.Message):
    username = message.from_user.username
    await message.answer(f"{username}")


@dp.message(Command("userid"))
async def getuserid(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"{user_id}")


# @dp.message(F.text)
# async def echo(message: types.Message):
#     with open("registration.txt", "a") as file:
#         file.write(f"{message.from_user.username}: {message.text} {message.from_user.id}\n")
#     await message.answer("обрабатываем ваши данные")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
