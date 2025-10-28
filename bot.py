import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Тoкeн из переменных oкpужeния (бeзoпacнee)
BOT_TOKEN = os.getenv('BOT_TOKEN', '8372653742:AAFQiExCnPS81Dv_mm154XvvpYIkG60-oPs')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        f"👋 Привет, {user.mention_html()}!\n"
        "🤖 Я бот для автоматической выдачи Telegram Stars\n\n"
        "📦 Для получения заказа:\n"
        "1. Скопируйте номер заказа с FunPay\n" 
        "2. Отправьте его мне в формате: #123456789\n"
        "3. Получите автоматическую выдачу Stars\n\n"
        "⚡ Быстро • Надежно • Автоматически"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    if text.startswith('#'):
        order_id = text[1:]
        await update.message.reply_text(
            f"✅ Заказ #{order_id} принят в обработку!\n"
            "🔄 Проверяем оплату в системе...\n"
            "⏳ Обычно это занимает 1-2 минуты\n\n"
            "💰 После подтверждения оплаты Stars будут отправлены автоматически!"
        )
    else:
        await update.message.reply_text(
            "❌ Неверный формат заказа!\n"
            "📋 Отправьте номер заказа в формате: #123456789\n"
            "🔗 Номер заказа можно скопировать из уведомления FunPay"
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Помощь по боту:\n\n"
        "/start - запустить бота\n"
        "/help - показать эту справку\n\n"
        "💡 Как использовать:\n"
        "1. Купите Stars на FunPay\n"
        "2. Скопируйте номер заказа\n"
        "3. Отправьте боту в формате #123456789"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    logging.info("Бот запускается...")
    app.run_polling()

if __name__ == "__main__":
    main()
