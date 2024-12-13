principle_value = 0
rate = 0
time = 0

while principle_value <= 0:
    principle_value = int(input("Enter your principle value: "))
    if principle_value <= 0:
        print("enter the valid amount")

while rate <= 0:
    rate = int(input("Enter your rate: "))
    if rate <= 0:
        print("enter the valid amount")

while time <= 0:
    time = int(input("Enter your rate: "))
    if time <= 0:
        print("enter the valid amount")

FinalAmount = principle_value * pow(1+rate/100, time)
print(f"Your compound interest is {FinalAmount:.2f}")