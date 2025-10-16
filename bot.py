from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello Sundaram! I’m your Telegram bot — ready to chat!")

if __name__ == '__main__':
    app = ApplicationBuilder().token("8169226337:AAESC4LMqCKNx3L3SsHHnO9ixkFZm4mjoq8").build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot is running...")
    app.run_polling()
