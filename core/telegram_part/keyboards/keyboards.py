from aiogram.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup

main = [
    [KeyboardButton(text="Профиль")],
    [KeyboardButton(text="Выбор игрока")],
    [KeyboardButton(text="Рейтинг")],
    [KeyboardButton(text="Запись на турнир")],
    [KeyboardButton(text="КОФНТ")]
]

common = [
        [KeyboardButton(text="Архив")],
        [KeyboardButton(text="Управление")],
        [KeyboardButton(text="Общая статистика")],
        [KeyboardButton(text="На главную")]
    ]

wb = [
    [KeyboardButton(text="Результаты соревнований")],
    [KeyboardButton(text="Документы федерации")],
    [KeyboardButton(text="На главную")]
]

direct = [
    [KeyboardButton(text="Последние матчи")],
    [KeyboardButton(text="Лучшие матчи")],
    [KeyboardButton(text="Против кого играю")],
    [KeyboardButton(text="На главную")]
]

other_player = [
        [KeyboardButton(text="Его матчи")],
        [KeyboardButton(text="Топ 10")],
        [KeyboardButton(text="Против кого он играет")],
        [KeyboardButton(text="На главную")]
    ]

back = [
    [KeyboardButton(text="На главную")]
]

admin_buttons = [
    [InlineKeyboardButton(
        text="Подтвердить",
        callback_data="admin_accept")],
    [InlineKeyboardButton(
        text="Изменить имя",
        callback_data="admin_changeName"),
        InlineKeyboardButton(
            text="Изменить номер",
            callback_data="admin_changePhoneNum")],
    [InlineKeyboardButton(
        text="Написать",
        callback_data="admin_toWrite")],
    [InlineKeyboardButton(
        text="Отклонить",
        callback_data="admin_cancel")],
]

keyboard_back = ReplyKeyboardMarkup(
        keyboard=back,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )

keyboard_common = ReplyKeyboardMarkup(
        keyboard=common,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )

keyboard_main = ReplyKeyboardMarkup(
        keyboard=main,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )

keyboard_wb = ReplyKeyboardMarkup(
        keyboard=wb,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )

keyboard_direct = ReplyKeyboardMarkup(
        keyboard=direct,
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню:"
    )