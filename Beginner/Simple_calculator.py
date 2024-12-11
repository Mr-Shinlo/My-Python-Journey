first_num = float(input("Enter your first number: "))
second_num = float(input("Enter your second number: "))
op = input("Enter your operator (+,-,*,/): ")

if op == "+":
    print(first_num + second_num)
elif op == "-":
    print(first_num - second_num)
elif op == "*":
    print(first_num * second_num)
elif op == "/":
    print(first_num / second_num)
else:
    print("Invalid input, try again")