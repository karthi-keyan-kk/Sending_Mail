import smtplib

E_MAIL = "YOUR_MAIL"
PASSWORD = "YOUR_PASSWORD"

# Subject: if you write subject, it will not consider as spam otherwise it will.

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=E_MAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=E_MAIL,
        to_addrs="TO_MAIL_ADDRESS",
        msg="Subject:Type Subject\nHere Type Your Message"
    )
