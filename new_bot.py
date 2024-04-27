from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace the token with your bot's token
token = "6634282047:AAGjm1EiFFbWXplp-odtAA8HU9WGR6R42-E"

# Create the Application with the bot's token
application = Application.builder().token(token).build()

# Define the command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, welcome to emsapi")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
    /start -> Welcome to the channel
    /help -> This particular message
    /create_user -> Click to create a user
    /update_user_email -> Click to update your email
    /update_user_username -> Click to update your username
    /get_all_user -> Click to get all users
    /create_post -> Click to create a post
    /get_all_post -> Click to get all posts
    /delete_the_post -> Click to delete a post
    /vote -> Click to vote on a post
    """
    await update.message.reply_text(help_text)

async def create_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Link to create a user: https://ems-api-fastapi-2.onrender.com/create_user")

# Add the command handlers to the application
application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', help_command))
application.add_handler(CommandHandler('create_user', create_user))

# Run the application
application.run_polling()
