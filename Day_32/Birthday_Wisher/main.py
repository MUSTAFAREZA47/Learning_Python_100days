import smtplib

my_email = "ahmedreza47@rediffmail.com"
password = "gu9zmmbz8igcwg8co8"

with smtplib.SMTP("smtp.rediffmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="mustafareza47@gmail.com",
        msg="Subject: Hello\n\nThis is ahmed from sasaram"
    )