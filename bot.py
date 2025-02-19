from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import os
import logging

# Enable logging for debugging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Get bot token from Railway environment variables

def auto_reply(update: Update, context: CallbackContext):
    """Replies only in direct messages (DMs) when the admin is offline."""
    if update.message.chat.type == "private":  # Only reply in private chats
        user = update.message.from_user
        logging.info(f"Received message from {user.first_name} (@{user.username}): {update.message.text}")
        
        reply_text = "🚀 *Admin is currently offline!* \n\n💬 *Kindly drop your message, and they will respond soon!*"
        update.message.reply_text(reply_text, parse_mode="Markdown")

def main():
    """Starts the bot and listens for messages."""
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Handle text messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, auto_reply))

    # Start the bot
    updater.start_polling()
    logging.info("Bot is now running...")
    updater.idle()

if __name__ == "__main__":
    main()
