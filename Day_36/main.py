import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VINTAGE_API_KEY = os.getenv("ALPHA_VINTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

alpha_vintage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VINTAGE_API_KEY
}

news_params = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API_KEY
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response_stock = requests.get(url=STOCK_ENDPOINT, params=alpha_vintage_params)
# print(response.status_code)
response_stock_data = response_stock.json()
data = response_stock_data["Time Series (Daily)"]
# print(data)

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)


# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_stock = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
# print(difference_stock)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference_stock / float(yesterday_closing_price)) * 100
# print(diff_percent)

# If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 1:
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response_news_data = response_news.json()
    articles_list = response_news_data['articles']

    # Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles_list[:3]

    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}\nDescription: {article['description']}" for article in
                          three_articles]
    # headlines = [article['title'] for article in three_articles]
    # descriptions = [description['description'] for description in three_articles]
    # print(f"Headline: {headlines} \n Description: {descriptions}")

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.
    for article in formatted_articles:
        # Send each article as a separate message via Twilio.
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body=article,
            from_="+14083200029",
            to="+918800753674"
        )
        print(message.sid)

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
