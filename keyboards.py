from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

WEBAPP_URL = "https://seabattle-11cb.onrender.com"


start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Открыть игру",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )],
        [InlineKeyboardButton(text="📖 Правила игры", callback_data="rules")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="main_menu")],
    ]
)

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Открыть игру",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )],
        [InlineKeyboardButton(text="📖 Правила игры", callback_data="rules")],
        [InlineKeyboardButton(text="💡 Советы", callback_data="tips")],
    ]
)

rules_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Открыть игру",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_menu")],
    ]
)

tips_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Открыть игру",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )],
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="back_to_menu")],
    ]
)