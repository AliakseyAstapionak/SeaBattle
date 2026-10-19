from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import start_keyboard, main_menu, rules_keyboard, tips_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    """Обработчик команды /start - показывает стартовое меню"""
    await state.clear()
    await message.answer(
        "⚓️ Добро пожаловать в <b>Морской бой</b>!\n\n"
        "Выберите действие:",
        reply_markup=start_keyboard
    )

@router.callback_query(F.data == "rules")
async def show_rules(callback: CallbackQuery, state: FSMContext):
    """Показывает правила игры"""
    await state.clear()
    await callback.message.edit_text(
        "📖 <b>Правила игры «Морской бой»</b>\n\n"
        "1. 🎯 Игровое поле — 10×10 клеток.\n"
        "2. 🚢 У каждого игрока по 10 кораблей:\n"
        "   • 1 корабль — 4 палубы\n"
        "   • 2 корабля — 3 палубы\n"
        "   • 3 корабля — 2 палубы\n"
        "   • 4 корабля — 1 палуба\n"
        "3. 🚫 Корабли не могут касаться друг друга.\n"
        "4. 🔫 Нажимайте на клетки поля противника.\n"
        "5. 💥 Попадание даёт дополнительный ход.\n"
        "6. ❌ Промах — ход переходит к противнику.\n"
        "7. 🏆 Побеждает тот, кто первым потопит все корабли!\n\n"
        "⬇️ Нажмите кнопку ниже, чтобы начать игру:",
        reply_markup=rules_keyboard
    )
    await callback.answer()

@router.callback_query(F.data == "main_menu")
async def show_main_menu(callback: CallbackQuery, state: FSMContext):
    """Показывает главное меню с советами"""
    await state.clear()
    await callback.message.edit_text(
        "🏠 <b>Главное меню</b>\n\n"
        "Здесь вы можете:\n"
        "• Начать новую игру\n"
        "• Изучить правила\n"
        "• Получить полезные советы\n\n"
        "Выберите действие:",
        reply_markup=main_menu
    )
    await callback.answer()

@router.callback_query(F.data == "tips")
async def show_tips(callback: CallbackQuery, state: FSMContext):
    """Показывает советы по игре"""
    await state.clear()
    await callback.message.edit_text(
        "💡 <b>Советы по игре «Морской бой»</b>\n\n"
        "🎯 <b>Стратегия стрельбы:</b>\n"
        "• Стреляйте в шахматном порядке — это увеличивает шансы найти корабль\n"
        "• После попадания бейте по соседним клеткам, чтобы добить корабль\n"
        "• Запоминайте промахи, чтобы не стрелять туда дважды\n\n"
        "🚢 <b>Расстановка кораблей:</b>\n"
        "• Не ставьте корабли на границы поля — их легче найти\n"
        "• Размещайте корабли в разных частях поля\n"
        "• Крупные корабли лучше прятать в центре\n\n"
        "🧠 <b>Психология:</b>\n"
        "• Следите за паттернами стрельбы противника\n"
        "• Меняйте свою стратегию, если она не работает\n"
        "• Не торопитесь — думайте перед каждым ходом\n\n"
        "⬇️ Нажмите кнопку ниже, чтобы начать игру:",
        reply_markup=tips_keyboard
    )
    await callback.answer()

@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    """Возвращает в главное меню"""
    await state.clear()
    await callback.message.edit_text(
        "🏠 <b>Главное меню</b>\n\n"
        "Выберите действие:",
        reply_markup=main_menu
    )
    await callback.answer()

@router.message()
async def echo(message: Message):
    """Обработчик всех остальных сообщений"""
    await message.answer(
        "❓ Используйте кнопки меню для навигации.",
        reply_markup=main_menu
    )