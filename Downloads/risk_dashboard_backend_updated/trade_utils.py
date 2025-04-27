import psycopg2
from config import DB_SETTINGS

def insert_trade(entry_price, stop_loss, target_price, risk_per_trade):
    conn = psycopg2.connect(**DB_SETTINGS)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO trades (entry_price, stop_loss, target_price, risk_per_trade)
        VALUES (%s, %s, %s, %s);
    ''', (entry_price, stop_loss, target_price, risk_per_trade))

    conn.commit()
    cursor.close()
    conn.close()