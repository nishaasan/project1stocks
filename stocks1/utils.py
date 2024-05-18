import requests
from django.conf import settings

def get_stock_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={settings.ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if 'Time Series (1min)' in data:
        latest_timestamp = next(iter(data['Time Series (1min)']))
        latest_data = data['Time Series (1min)'][latest_timestamp]
        return latest_data, latest_timestamp
    return None, None
