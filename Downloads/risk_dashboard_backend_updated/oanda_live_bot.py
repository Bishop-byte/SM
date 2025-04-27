import time
from oanda_fetch import insert_live_trade

def run_live_bot(interval_seconds=60):
    print("🚀 Starting Live Trading Bot...")

    try:
        while True:
            insert_live_trade("EUR_USD", stop_loss_pips=20, target_pips=40, risk_per_trade=1.0)
            print(f"✅ Trade inserted. Waiting {interval_seconds} seconds...")
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped manually.")

if __name__ == "__main__":
    run_live_bot(interval_seconds=60)