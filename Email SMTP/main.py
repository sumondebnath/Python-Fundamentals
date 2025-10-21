import smtplib
import datetime as dt
import random
from pathlib import Path

file_Path = Path(__file__).parent / "quotes.txt"
# print(file_Path)

now = dt.datetime.now()
# print(now)
weekday = now.weekday()
# print(weekday)

my_email = "nath.debsumon@gmail.com"
password = ""

if weekday == 0:
    with open(file_Path) as file:
        all_quote = file.readlines()
        quote = random.choice(all_quote)
    # print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:This is the subject\n\n{quote}")