import os
from dotenv import load_dotenv
import requests
import smtplib
import schedule
import time

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
load_dotenv()
al_api = os.getenv("STOCK_API")
n_api = os.getenv("NEWS_API")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def get_prices(st):
    try:
        r = requests.get(STOCK_ENDPOINT + f"?function=TIME_SERIES_DAILY&symbol={st}&outputsize=full&apikey={al_api}")
        data = r.json()
        daily = data['Time Series (Daily)']
        daily_list = list(daily.items())
        _, today = daily_list[0]
        _, yesterday = daily_list[1]
        today_close = today['4. close']
        yesterday_close = yesterday['4. close']
        return float(today_close), float(yesterday_close)
    except (Exception, ConnectionRefusedError, ConnectionError) as e:
        print("Error getting the price: ", e)

def get_news(comp):
    try:
        r = requests.get(f"https://newsapi.org/v2/everything?q={comp.lower()}&sortBy=publishedAt&apiKey={n_api}")
        data = r.json()
        if data['status'] == "ok":
            articles = data['articles']
            n_ar = []
            for i in range(3):
                n_ar.append(articles[i])
            return n_ar
    except(Exception, ConnectionRefusedError, ConnectionError) as e:
        print("Error getting the news: ", e)

def send_email(article, stock, df):
    try:
        sender = "example_email_sender@gmail.com"
        app_password = "sender_app_password" #generate in email provider
        subject = f"Check at the news! {stock}: {df}"
        host = "smtp.gmail.com" #whatever email provider
        email_text = f"{article}"
        reciver_ = "me@gmail.com"
        
        with smtplib.SMTP(host) as connection: 
            connection.starttls()
            connection.login(user= sender, password=app_password)
            connection.sendmail(from_addr=sender, to_addrs=reciver_,
                                msg=f"Subject:{subject}\n\n{email_text}")
    except Exception as e:
        print("Error sending email: ", e)


def notification(stock, company):
    try:
        today_close, yesterday_close = get_prices(stock)
        i_d = ((today_close - yesterday_close) * 100)/today_close
        if abs(i_d) >= 5:
            articles = get_news(company)
            for art in articles:
                head = art["title"]
                cont = art["content"]
                content = f"Headline: {head}\nBrief:{cont}"
                send_email(content, stock, i_d)
    except Exception as e:
        print("Error feedback: ", e)

schedule.every().day.at("08:00").do(lambda: notification(STOCK, COMPANY_NAME))
while True:
    schedule.run_pending()
    time.sleep(60) # check the scedule every minute


"""Example notification"""
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

