import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Бот работает! Отправьте номер заказа #123456789")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if text.startswith('#'):
        logger.info(f"Обработка заказа: {text}")
        await update.message.reply_text(f"✅ Заказ {text} принят в обработку!")
    else:
        await update.message.reply_text("📋 Отправьте номер заказа в формате #123456789")

if __name__ == "__main__":
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN не установлен")
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🚀 Бот запускается в polling режиме...")
    app.run_polling()
