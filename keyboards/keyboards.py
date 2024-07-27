"""директория для хранения клавиатур, которые бот будет отправлять пользователю"""

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU

# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU["yes_button"])
button_no = KeyboardButton(text=LEXICON_RU["no_button"])

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)


"""У клавиатуры yes_no_kb добавляем параметр one_time_keyboard=True, потому что эта клавиатура
должна сворачиваться после нажатия пользователя на кнопку с текстом "Не хочу!".
А если пользователь нажмет на кнопку "Давай!" - клавиатура yes_no_kb будет заменена на игровую клавиатуру. """
# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# 1. Создали кнопки
button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])

# 2. Создали билдер
game_kb_builder = ReplyKeyboardBuilder()

# 3. Добавили в билдер кнопки
game_kb_builder.row(button_1, button_2, button_3, width=3)

# 4. Создали клавиатуру из билдера и кнопок.
game_kb: ReplyKeyboardMarkup = game_kb_builder.as_markup(
    resize_keyboard=True
)