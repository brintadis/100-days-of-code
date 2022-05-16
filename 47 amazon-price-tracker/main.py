import lxml
import requests
import smtplib
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com/dp/B085296FLT"
TARGET_PRICE_DROP = 175
MAIL_PROVIDER_SMTP_ADDRESS = "YOUR EMAIL PROVIDER SMTP ADDRESS"
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# Getting html of the product url
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}
response = requests.get(url=PRODUCT_URL, headers=header)

# Parsing price and name of the product
soup = BeautifulSoup(response.text, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
product_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip()

# Sending an email notification if price < target price drop
if price <= TARGET_PRICE_DROP:
    with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587, timeout=120) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: AMAZON PRICE ALERT!\n\n{product_name} is now ${price}\n{PRODUCT_URL}"
        )