from db_setup import create_trade_table
from trade_utils import insert_trade
from fetch_trades import fetch_trades

create_trade_table()
insert_trade(120, 115, 130, 2.5)

trades = fetch_trades()
print(trades)