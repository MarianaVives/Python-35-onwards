import requests
import datetime as dt
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = " "
NEWS_API_KEY = " "

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}
news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS).json()
articles = news_response["articles"]

# --- Get yesterday's closing price ---
stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS).json()
data = stock_response["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]
# --- Get day before yesterday closing price ---
day_before_yesteday_data = data_list[1]
day_before_yesteday_closing_price = day_before_yesteday_data["4. close"]
# --- Get the difference between yesterday's closing price and day before ystrd price ---
difference = float(yesterdays_closing_price) - float(day_before_yesteday_closing_price)
up_down= None
if difference > 0:
    up_down="🔺"
else:
    up_down="🔻"
# --- Workoout the percentage difference in price between btwn closing price yesterday and day before yesterday
difference_percent = (abs(difference) / float(yesterdays_closing_price)) *100
# --- If % > 5 , print get news
if difference_percent > 0:
    print("Get notification")
    # --- Use News api to get articles from Company using python slice operator to get the first 3 articles
    three_articles = articles[:3]
    # --- Create list that contains 3 first articles headlines
    formatted_articles_list = [f"{STOCK_NAME}{up_down}{round(difference_percent,2)}: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    print(formatted_articles_list)
    # --- send Twilio to send a separte msg
    account_sid =  ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    for fa in formatted_articles_list:
        message = client.messages.create(
            body=fa,
            from_="+123",
            to = "+123"
        )
