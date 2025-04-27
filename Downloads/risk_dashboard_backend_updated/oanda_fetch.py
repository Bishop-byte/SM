import requests
import psycopg2
from config import DB_SETTINGS

OANDA_API_URL = "https://api-fxpractice.oanda.com/v3/instruments/{instrument}/candles"
OANDA_API_KEY = ""  # Insert your OANDA API Key

def fetch_latest_price(instrument="EUR_USD"):
    headers = {
        "Authorization": f"Bearer {OANDA_API_KEY}"
    }
    params = {
        "count": 1,
        "granularity": "M1",
        "price": "M"
    }
    response = requests.get(OANDA_API_URL.format(instrument=instrument), headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        price = float(data["candles"][0]["mid"]["c"])
        return price
    else:
        print("Failed to fetch data:", response.text)
        return None

def insert_live_trade(instrument="EUR_USD", stop_loss_pips=20, target_pips=40, risk_per_trade=1.0):
    latest_price = fetch_latest_price(instrument)

    if latest_price:
        stop_loss = latest_price - (stop_loss_pips * 0.0001)
        target_price = latest_price + (target_pips * 0.0001)

        conn = psycopg2.connect(**DB_SETTINGS)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO trades (entry_price, stop_loss, target_price, risk_per_trade)
            VALUES (%s, %s, %s, %s);
        ''', (latest_price, stop_loss, target_price, risk_per_trade))

        conn.commit()
        cursor.close()
        conn.close()

        print(f"Inserted live trade: Entry={latest_price:.5f}, SL={stop_loss:.5f}, TP={target_price:.5f}")
    else:
        print("No trade inserted due to fetch failure.")