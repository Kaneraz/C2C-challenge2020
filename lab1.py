"""
At FactSet the first step of the portfolio lifecycle involves parsing 
clients' holdings into our portfolio databases. In this lab you are 
given an input file as comma separated values and calculating the 
portfolio's value. Each line has a symbol and number of shares.

portfolio.py contains documentation for the portfolio object
get_price(symbol) will return the latest closing price given a symbol
portfolio.csv is the input file that's being parsed
https://www.w3schools.com/python/ref_string_split.asp

"""

from portfolio import Portfolio, Holding, get_price
from datetime import date

def parse_portfolio(filepath):
  portfolio = Portfolio(date(2020,1,2))
  with open(filepath) as fp:
    lines = fp.readlines()
    for line in lines:
      portfolio.add_holding(Holding(*line.split(',')))
  return portfolio

def portfolio_value(portfolio: Portfolio):
  total = 0
  for holding in portfolio.holdings:
    total += int(holding.shares) * get_price(holding.symbol)
  return total
