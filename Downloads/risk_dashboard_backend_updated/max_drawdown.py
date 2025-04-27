import numpy as np

def calculate_max_drawdown(prices):
    peak = prices.cummax()
    drawdown = (prices - peak) / peak
    max_drawdown = drawdown.min()
    return max_drawdown