import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
mail_my = "your@vitap.ac.in"
s.starttls()
s.login(mail_my, "Pass")
message = "Message_you_need_to_send"
s.sendmail(mail_my, mail_my, message)
s.quit()
