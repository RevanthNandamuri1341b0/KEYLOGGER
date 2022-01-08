import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text("Hi!")


def help(update, context):
    update.message.reply_text("Help!")


def echo(update, context):
    if update.message.text == "bossprotocol":
        pass
    else:
        print(update.message.text)
        update.message.reply_text(update.message.text)


def bossprotocol():
    pass
    


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater(
        "5027710057:AAGBz3kPPzovjenBTiB2_-shOutLMg0NBmI", use_context=True
    )

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    dp.add_error_handler(error)
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
