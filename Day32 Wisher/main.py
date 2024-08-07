##################### Normal Starting Project ######################
import datetime as dt
import pandas as pa
import random
import smtplib

my_email = "ribacokmisa@gmail.com"
password = "zadi nfks ccqk lnuo"

now = (dt.datetime.now().month, dt.datetime.now().day)
data = pa.read_csv('birthdays.csv')
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if now in birthdays_dict:
    birthday_person = birthdays_dict[now]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as text_file:
        content = text_file.read()
        final_content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP('smtp.gmail.com', 587) as letter:
        letter.starttls()
        letter.login(my_email, password)
        letter.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday\n\n{final_content}")
