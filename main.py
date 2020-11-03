from lab1 import parse_portfolio
from lab3 import username, portfolio_name
from leaderboard import submit_custom_portfolio

if username() == "username":
  raise Exception("Fill in a username for our leaderboard.")

portfolio = parse_portfolio(portfolio_name())
submit_custom_portfolio(portfolio)


print("Visit http://leaderboard to view the leaderboard")
