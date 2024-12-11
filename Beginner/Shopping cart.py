item_name = input("What item would you like to buy: ")
amount = int(input("Please enter the amount: "))
price = float(input("Please enter the price in USD: "))

total = price * amount

print(f"The item you are buying is {item_name} and amount is {amount}/s")
print(f"Your total come out as {total}$")