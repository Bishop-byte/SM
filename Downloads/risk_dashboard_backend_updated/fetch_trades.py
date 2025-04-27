import psycopg2
from config import DB_SETTINGS

def fetch_trades():
    conn = psycopg2.connect(**DB_SETTINGS)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trades;")
    trades = cursor.fetchall()

    cursor.close()
    conn.close()

    return trades