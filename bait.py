from tkinter import *

f = Tk()
f.title("Gmail Gui")
send_email = StringVar()
send_pass = StringVar()
recv_email = StringVar()
msg_body = None


def layout():
    menuBar = Menu(f)
    menuBar.add_command(label="Instructions")
    menuBar.add_command(label="About")
    f.config(menu=menuBar)

    sender_email = Label(f, text="Sender Gmail ID: ")
    sender_entry = Entry(f, textvariable=send_email, bd=3)
    sender_pass = Label(f, text="Sender Gmail Pass: ")
    sender_passentry = Entry(f, show="*", textvariable=send_pass, bd=3)

    receiver_email = Label(f, text="Receiver Email: ")
    receiver_entry = Entry(f, textvariable=recv_email, bd=3)

    msg_label = Label(f, text="Message")
    global msg_body
    msg_body = Text(f, height=5, width=15, bd=3)

    send = Button(f, text="Send", width=15, bd=3)
    cancel = Button(f, text="Cancel", width=15, bd=3)

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
    f.mainloop()

layout()


