from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from openai import OpenAI

# 🔑 TOKENLAR
BOT_TOKEN = "8594176537:AAELj8oGyHHtbZHl1O5YondYzpDc7mkVzvg"
OPENAI_API_KEY = "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"

# OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salom!\nMen ChatGPT botman.\nSavolingni yoz 👇"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_text}
        ]
    )

    answer = response.choices[0].message.content
    await update.message.reply_text(answer)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if name == "main":
    main()
