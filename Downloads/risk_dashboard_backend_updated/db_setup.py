import psycopg2
from config import DB_SETTINGS

def create_trade_table():
    conn = psycopg2.connect(**DB_SETTINGS)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id SERIAL PRIMARY KEY,
            entry_price FLOAT NOT NULL,
            stop_loss FLOAT NOT NULL,
            target_price FLOAT NOT NULL,
            risk_per_trade FLOAT NOT NULL,
            trade_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            profit_loss FLOAT
        );
    ''')

    conn.commit()
    cursor.close()
    conn.close()