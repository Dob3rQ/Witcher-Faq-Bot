from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from database import get_answer
from config import TOKEN

async def start(update: Update):
    await update.message.reply_text("Привет! Я FAQ-бот по Ведьмаку. Задай мне вопрос!")

async def handle_question(update: Update):
    user_question = update.message.text.strip()
    answer = get_answer(user_question)

    if answer:
        await update.message.reply_text(answer)
    else:
        await update.message.reply_text("Я пока на стадии зародыша и не знаю всех ответов, но я учусь."
                                        "Пожалуйста, прости меня и задай другой вопрос.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question))

    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
