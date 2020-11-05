from datetime import date, timedelta
import yfinance as yf

class Holding:
  """
  Represents a security and the number of shares held of that security in
  portfolio.

  Example:
  my_apple_holdings = Holding("AAPL", 100)
  """
  def __init__(self, symbol: str, shares: str):
    self.symbol:str = symbol
    self.shares:int = int(shares.strip())

  def __str__(self):
    return self.symbol.ljust(8, " ")  + str(self.shares) + "\n"


class Portfolio:
  """
  Represents a portfolio of several securities. It contains multiple holdings
  and the date that the portfolio should start trading.

  Example:
  my_tech_portfolio = Portfolio(date.today())
  my_tech_portfolio.add_holding(Holding("FB", 100))
  my_tech_portfolio.add_holding(Holding("AAPL", 100))
  my_tech_portfolio.add_holding(Holding("NFLX", 200))
  """
  holdings: list
  openDate: date

  def __init__(self, openDate: date = date.today()):
    self.holdings = list()
    self.openDate = openDate

  def add_holding(self, holding: Holding):
    self.holdings.append(holding)

  def __str__(self):
    string = "Portfolio:\n"
    string += "Opened: " + self.openDate.strftime("%d-%b-%Y") + "\n"
    for holding in self.holdings:
      string += str(holding)
    return string


def get_price(symbol):
  priceDate = date.today() - timedelta(days=10)
  ticker = yf.Ticker(symbol)
  history = ticker.history(start=priceDate)
  return round(history[-1:]["Close"][0],2)
