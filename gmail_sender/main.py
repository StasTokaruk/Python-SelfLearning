import smtplib

my_email = 'pythont1605@gmail.com'
my_password = 'uhkj viho xgia zszf'
sender_email = ""
for i in range(3):
     connection = smtplib.SMTP('smtp.gmail.com', 587)
     connection.starttls()
     connection.login(my_email, my_password)
     connection.sendmail(my_email, sender_email, msg="Subject:Hello\n\nCho tak dovgo?????")
     connection.close()