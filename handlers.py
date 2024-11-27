from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from functions import find_job, categories, show_vacancies, handle_job_type

# Главное меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Найти вакансию", callback_data="find_job")],
        [InlineKeyboardButton("Категории вакансий", callback_data="categories")],
        [InlineKeyboardButton("Настройки", callback_data="settings")],
        [InlineKeyboardButton("Помощь", callback_data="help")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text("Добро пожаловать в EmployMe! Выберите действие:", reply_markup=reply_markup)
    elif update.callback_query:
        query = update.callback_query
        await query.edit_message_text("Добро пожаловать в EmployMe! Выберите действие:", reply_markup=reply_markup)

# Обработчик callback'ов
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "find_job":
        await find_job(query)
    elif query.data == "categories":
        await categories(query)
    elif query.data == "settings":
        await settings(query)
    elif query.data == "help":
        await help_section(query)
    elif query.data.startswith("cat_"):
        category = query.data.split("_")[1]
        await show_vacancies(query, category)
    elif query.data == "job_online":
        await handle_job_type(query, "online")
    elif query.data == "job_offline":
        await handle_job_type(query, "offline")
    elif query.data == "main_menu":
        await start(update, context)
    elif query.data.startswith("set_"):
        await settings_option(query, query.data.split("_")[1])
    elif query.data.startswith("location_"):
        await location_selected(query, query.data.split("_")[1])
    elif query.data.startswith("salary_"):
        await salary_selected(query, query.data.split("_")[1])

# Настройки
async def settings(query):
    keyboard = [
        [InlineKeyboardButton("Изменить локацию", callback_data="set_location")],
        [InlineKeyboardButton("Установить зарплату", callback_data="set_salary")],
        [InlineKeyboardButton("Назад в главное меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Настройки поиска:", reply_markup=reply_markup)

# Действия для настройки
async def settings_option(query, option):
    if option == "location":
        regions = ["Чуй", "Ош", "Джалал-Абад", "Нарын", "Талас", "Баткен", "Иссык-Куль"]
        keyboard = [[InlineKeyboardButton(region, callback_data=f"location_{region.lower()}")] for region in regions]
        keyboard.append([InlineKeyboardButton("Назад", callback_data="settings")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите область:", reply_markup=reply_markup)
    elif option == "salary":
        salary_ranges = [
            ("10-20 тыс.", "10-20"),
            ("20-50 тыс.", "20-50"),
            ("50-100 тыс.", "50-100"),
        ]
        keyboard = [[InlineKeyboardButton(range_text, callback_data=f"salary_{range_value}")] for range_text, range_value in salary_ranges]
        keyboard.append([InlineKeyboardButton("Назад", callback_data="settings")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Выберите диапазон зарплаты:", reply_markup=reply_markup)
    else:
        await query.edit_message_text("Неизвестный параметр. Попробуйте снова.")

# Выбор области
async def location_selected(query, location):
    await query.edit_message_text(f"Вы выбрали область: {location.capitalize()}. Локация успешно изменена!")
    await query.message.reply_text("Настройка завершена. Вернитесь в главное меню или продолжите настройки.")

# Выбор диапазона зарплаты
async def salary_selected(query, salary_range):
    await query.edit_message_text(f"Вы выбрали диапазон зарплаты: {salary_range} тыс.")
    await query.message.reply_text("Настройка завершена. Вернитесь в главное меню или продолжите настройки.")

# Помощь
async def help_section(query):
    await query.message.reply_text("Свяжитесь с нашим модератором по номеру: +999 555555555")
    keyboard = [
        [InlineKeyboardButton("Назад в главное меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text("Выберите действие:", reply_markup=reply_markup)
