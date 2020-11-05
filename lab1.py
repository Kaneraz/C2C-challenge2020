"""
At FactSet the first step of the portfolio lifecycle involves parsing, (or
reading-in) clients' holdings into our portfolio databases. In this lab you are
given an input file as comma separated values and must calculate the
portfolio's value. Each line of the input file has a symbol and number of
shares.

portfolio.py contains documentation for the portfolio object
portfolio.csv is the input file that's being parsed
https://www.w3schools.com/python/ref_string_split.asp
"""

from portfolio import Portfolio, Holding, get_price
from datetime import date

filepath = 'portfolio.csv'

def username():
  # Return your name for the leaderboard here
  return "username"

# STEP 1: create a Portfolio and fill it with Holdings from the input file
def parse_portfolio():
  portfolio = Portfolio(date(2020,1,2))
  with open(filepath) as fp:
    lines = fp.readlines()
    #for line in lines:
      # Split each line to separate the symbol and the number of shares

      # Place the values into a new Holding object

      # Add the holding to a Portfolio.

  return portfolio

# STEP 2: calculate the value of the portfolio
def portfolio_value(portfolio: Portfolio):
  total = 0
  # Loop through each holding in the portfolio

    # Calculate the value of the holding using the get_price helper method

    # Add the value to the total

  return total
