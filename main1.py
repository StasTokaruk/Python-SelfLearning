import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
MY_EMAIL = "ribacokmisa@gmail.com"
PASSWORD = "zadi nfks ccqk lnuo"

if weekday == 0:
    with open("quotes.txt") as f:
        all_quotes = f.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL, to_addrs="makcim1999koval@gmail.com",
                            msg=f"Subject:Today motivation\n\n{quote}")






# import smtplib
#
#
# my_email = "ribacokmisa@gmail.com"
# password = "zadi nfks ccqk lnuo"
#
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="misar7363@gmail.com", msg="Hello")
#
#
# import datetime as dt
#
#
# now = dt.datetime.now()
# year = now.year





