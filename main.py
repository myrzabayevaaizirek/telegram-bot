from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from handlers import start, handle_callback

if __name__ == "__main__":
    # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
    application = ApplicationBuilder().token("7880612271:AAFJPGvn5AIh9cOytB7xy5Kf4F5qmPsBSA8").build()

    # Регистрация команд и обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_callback))

    print("EmployMe бот запущен!")
    application.run_polling()
