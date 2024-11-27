from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def find_job(query):
    keyboard = [
        [InlineKeyboardButton("Онлайн", callback_data="job_online")],
        [InlineKeyboardButton("Офлайн", callback_data="job_offline")],
        [InlineKeyboardButton("Назад в главное меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Выберите тип работы:", reply_markup=reply_markup)

async def categories(query):
    keyboard = [
        [InlineKeyboardButton("IT и разработка", callback_data="cat_IT")],
        [InlineKeyboardButton("Маркетинг и реклама", callback_data="cat_Marketing")],
        [InlineKeyboardButton("Продажи", callback_data="cat_Sales")],
        [InlineKeyboardButton("Дизайн и UX/UI", callback_data="cat_Design")],
        [InlineKeyboardButton("Назад в главное меню", callback_data="main_menu")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Выберите категорию вакансий:", reply_markup=reply_markup)

async def show_vacancies(query, category):
    vacancies = {
        "IT": ["Python Developer", "Full Stack Developer", "Data Scientist"],
        "Marketing": ["SMM Manager", "Content Manager", "SEO Specialist"],
        "Sales": ["Sales Manager", "Account Executive", "Retail Salesperson"],
        "Design": ["UX/UI Designer", "Graphic Designer", "Motion Designer"],
    }
    vacancy_list = vacancies.get(category, [])
    text = f"Вакансии в категории {category}:\n"
    for vacancy in vacancy_list:
        text += f"- {vacancy}\n"
    keyboard = [[InlineKeyboardButton("Назад к категориям", callback_data="categories")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup)

async def handle_job_type(query, job_type):
    text = "Вы выбрали: Онлайн" if job_type == "online" else "Вы выбрали: Офлайн"
    text += ". Выберите категорию:"
    keyboard = [
        [InlineKeyboardButton("IT и разработка", callback_data="cat_IT")],
        [InlineKeyboardButton("Маркетинг и реклама", callback_data="cat_Marketing")],
        [InlineKeyboardButton("Продажи", callback_data="cat_Sales")],
        [InlineKeyboardButton("Дизайн и UX/UI", callback_data="cat_Design")],
        [InlineKeyboardButton("Назад", callback_data="find_job")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text, reply_markup=reply_markup)
