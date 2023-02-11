from email.mime.text import MIMEText
import random
import smtplib


def generate6DigitOTP():
    return random.randint(100000, 999999)


def sendOTP(email):
    ran = generate6DigitOTP()
    appPass = "cfqfvtdgoilkfmnz"
    sender = 'bazaartourr@gmail.com'
    msg = MIMEText(
        f'Your OTP for BazaarTour is: {ran}. Please do not share this with anyone.')
    msg['Subject'] = 'BaraarTour OTP'
    msg['From'] = sender
    tolist = email
    msg['To'] = tolist

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login(sender, appPass)
    server.sendmail(sender, tolist, msg.as_string())
    server.quit()
    return ran
