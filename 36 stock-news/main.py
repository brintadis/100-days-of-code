import requests
from twilio.rest import Client

# https://www.alphavantage.co/support/#api-key to get stock api key
# https://newsapi.org/account to get stock news api key

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_price_api_key = "Your alphavantage api key"
news_api_key = "Your newsapi.org api key"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = "Your twilio phone number"
receiver_number = "Receiver number"

stock_url = f'https://www.alphavantage.co/query'
news_url = f"https://newsapi.org/v2/everything"

# Get yesterday's closing stock price
stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_price_api_key,
}

response = requests.get(stock_url, params=stock_api_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find the difference between 1 and 2
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Get the percentage difference
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

# If percentage is greater than 5 then program continuing
if abs(diff_percent) > 0:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
        "language": "en"
    }

    # Get stock news articles
    response = requests.get(news_url, params=news_params)
    articles = response.json()["articles"][:3]

    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_=twilio_phone_number,
            to=receiver_number,
        )
        print(message.status)
