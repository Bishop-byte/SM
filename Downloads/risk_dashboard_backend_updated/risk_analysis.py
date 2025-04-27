import psycopg2
from config import DB_SETTINGS
from email_alerts import send_alert_email
import datetime

def log_message(message):
    with open("risk_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - {message}\n")

def analyze_trade_risk():
    conn = psycopg2.connect(**DB_SETTINGS)
    cursor = conn.cursor()

    cursor.execute("SELECT id, entry_price, stop_loss, target_price FROM trades;")
    trades = cursor.fetchall()

    for trade in trades:
        trade_id, entry_price, stop_loss, target_price = trade
        rr_ratio = (target_price - entry_price) / (entry_price - stop_loss)
        log_message(f"Trade ID {trade_id} - Entry: {entry_price}, RR Ratio: {rr_ratio:.2f}")

        if rr_ratio < 1.5:
            alert_text = f"Low Risk-Reward Trade Detected! Trade ID {trade_id}, RR Ratio: {rr_ratio:.2f}"
            send_alert_email("⚠️ Low Risk-Reward Alert", alert_text)
            log_message(alert_text)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    analyze_trade_risk()