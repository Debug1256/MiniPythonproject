#Scenario: Stock Data Entry and Analysis Tool

#Objective: Create a Python script that will involve taking manual input for stock prices over a week and will calculate the average price. It should also demonstrate variable declaration, user input, and basic arithmetic using Python types.

# variable declaration: Stock prices for each day of the week
stock_prices = []

# User input: asking the user to enter stock prices for 7 days
print("Please enter the stock prices for 7 days:")

# Loop to collect stock prices for each day
for i in range(1,8):
    price = float(input(stock_prices))
    stock_prices.append(price)
    
#Basic arithmetic: calculating the sum and  average of the stock prices
total_price = sum(stock_prices)
average_price = total_price / 7

# Output: displaying the total and average stock price
print("\nStock Prices Entered:", stock_prices)
print(f"Total Price for the week: {total_price}")
print(f"Average Stock Price for the week: {average_price:.2f}")