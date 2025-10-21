import smtplib

myEmail = "nath.debsumon@gmail.com"
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=myEmail, password=password)
    connection.sendmail(from_addr=myEmail, to_addrs="debnathsumon@gmail.com", msg="Subject:This is the Subject\n\n This is the email body.")
