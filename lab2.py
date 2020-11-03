"""
Once parsed, we can run analytics on the portfolio. A simple metric is
how well the portfolio performs versus a benchmark. These can be other
portfolios, index funds, or fixed income instruments such as bonds.
For our benchmark we'll use the S&P 500 and calculate the portfolio's
adjusted returns compared to the benchmark.

get_historical_price(symbol, priceDate) will return the price for a security at a given date

"""

from portfolio import Portfolio, Holding, get_price, get_historical_price
from lab1 import portfolio_value
from datetime import date

def portfolio_returns(portfolio: Portfolio):
  # Calculate the value for the potfolio at its open date
  opening_value = 1

  # Calculate the value for the portfolio today
  todays_value = 0

  # calculate the percentage change since opening
  return round((todays_value / opening_value - 1) * 100,2)

def benchmark_returns(open_date: date):
  benchmark_symbol = "^GSPC" # S&P 500
  benchmark_returns = 0
  # Calculate the returns for S&P 500 since the portfolio's open date
  
  
  return benchmark_returns

def adjusted_returns(portfolio_returns, benchmark_returns):
  # Find the percent return for the portfolio vs the benchmark
  adjusted_returns = 0

  return adjusted_returns