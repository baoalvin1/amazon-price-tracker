import requests
from bs4 import BeautifulSoup
import smtplib
url = "https://www.amazon.com/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4/ref=sr_1_1_sspa?crid=2I2AY5N1T2SUS&keywords=apple+airpods+pro&qid=1578847945&sprefix=ap%2Caps%2C150&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTEdTWENVT1E1VFVGJmVuY3J5cHRlZElkPUEwODU5Njg0UEFLWTdSQzVVSzFZJmVuY3J5cHRlZEFkSWQ9QTAwMDU0MTQzUkVZU1c4M0hVWkIzJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}


def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    if converted_price < converted_price*.85:
        send_mail()

    print(converted_price)
    print(title.strip())

    if converted_price > converted_price*.85:
        send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('baoalvin1@gmail.com', 'lqajjmyrlvskvhfk')

    subject = "Price dropped!"
    body = "Check the Amazon link https://www.amazon.com/Apple-MWP22AM-A-AirPods-Pro/dp/B07ZPC9QD4/ref=sr_1_1_sspa?crid=2I2AY5N1T2SUS&keywords=apple+airpods+pro&qid=1578847945&sprefix=ap%2Caps%2C150&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTEdTWENVT1E1VFVGJmVuY3J5cHRlZElkPUEwODU5Njg0UEFLWTdSQzVVSzFZJmVuY3J5cHRlZEFkSWQ9QTAwMDU0MTQzUkVZU1c4M0hVWkIzJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
    'baoalvin123@gmail.com',
    'baoalvin1@gmail.com',
    msg
    )
    print("HEY EMAIL HAS BEEN SENT!")

    server.quit()

check_price()
