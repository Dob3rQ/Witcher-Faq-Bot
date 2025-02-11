from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from wiki_scraper import find_best_wikipedia_article
from config import TOKEN
from telegram.constants import ChatAction

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я FAQ-бот. Спрашивай что угодно, и я найду ответ в Википедии!")

async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_question = update.message.text.strip()

    # Показываем анимацию "бот печатает..."
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)

    summary, url = find_best_wikipedia_article(user_question)

    if summary and url:
        await update.message.reply_text(f"{summary}\n\n[Читать дальше]({url})", parse_mode="Markdown")
    else:
        await update.message.reply_text("Я не смог найти точный ответ, попробуй переформулировать вопрос.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question))

    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
