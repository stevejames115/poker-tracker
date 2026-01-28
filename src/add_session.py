import csv
from datetime import datetime

# File path
FILE = "data/sessions.csv"

print("=== Poker Session Logger ===")

date = datetime.now().strftime("%Y-%m-%d")
game = input("Game (e.g. NLH, PLO): ")
stakes = input("Stakes (e.g. 0.01/0.02 or 1/2): ")
minutes = input("Minutes played: ")
buyin = float(input("Total buy-in: "))
cashout = float(input("Cash out: "))
notes = input("Notes: ")

profit = cashout - buyin

with open(FILE, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([date, game, stakes, minutes, buyin, cashout, profit, notes])

print("\nSession saved!")
print(f"Profit: ${profit:.2f}")
