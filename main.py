import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def ask_command(update, context):
    # Check if the user provided any command arguments
    if context.args:
        # Extract the message from the command arguments
        message = ' '.join(context.args)
        # Do something with the extracted message, e.g., print it or respond to it
        print(message)
        await update.message.reply_text(f"Received message from command: \n\n {message}")
    else:
        # Handle the case where no message is provided in the command
        await update.message.reply_text("Please provide a message after the command.")



print("bot starting")

app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("ask", ask_command))


print("bot started")
app.run_polling()