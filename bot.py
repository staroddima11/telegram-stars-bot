import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ВСТAВЬТE НOВЫЙ ТOКEН OТ @BotFather
BOT_TOKEN = "8339305305:AAGIOrLV3yQnUTVzhFJ7w8CQb8OMJ9vJ0jY"

logging.basicConfig(level=logging.INFO)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Бот работает! Отправьте номер заказа #123456789")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.startswith('#'):
        await update.message.reply_text(f"✅ Заказ {text} принят в обработку!")
    else:
        await update.message.reply_text("❌ Отправьте номер заказа как #123456789")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Бот запущен и готов к работе!")
    app.run_polling()

if __name__ == "__main__":
    main()
