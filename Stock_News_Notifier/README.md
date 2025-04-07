## Stock News Notifier

A simple Python automation script that monitors Tesla stock price (or any other stock you wish) using the Alpha Vantage API. If the stock price changes by 5% or more (either up or down) compared to the previous trading day, it sends an email alert with the latest relevant news headlines pulled from the NewsAPI.

### Features

- Automatically checks TSLA stock price daily at 08:00
- Fetches recent news articles about Tesla when price fluctuations exceed 5%
- Sends an email notification with the headline and a brief snippet

### Requirements

- Python 3.x
- `requests`
- `python-dotenv`
- `smtplib` (built-in)
- `schedule`

### Setup

1. **Clone the repo**
2. **Install dependencies**: pip install -r requirements.txt
3. **Create a `.env` file** in the same directory with the following:

   ```env
   STOCK_API=your_alpha_vantage_api_key
   NEWS_API=your_newsapi_key
   ```

4. **Configure your email credentials** in the `send_email()` function:
   - Replace `example_email_sender@gmail.com` with your sender email.
   - Replace `sender_app_password` with your email app password.
   - Replace `me@gmail.com` with the recipient email.

### Usage

Run the script. It uses `schedule` to check for stock updates every day at 08:00 AM.
