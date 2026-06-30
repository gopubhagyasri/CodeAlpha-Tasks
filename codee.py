# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400
}

total_investment = 0

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    stock = input("Enter stock name (AAPL, TSLA, GOOGL, MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"{stock}: ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_investment)

# Save result to text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("Result saved in portfolio.txt")