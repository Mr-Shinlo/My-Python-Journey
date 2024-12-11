degree = float(input("How hot is it: "))
unit = input("What is your unit? F or C ")

if unit.upper() == "F":
    celcius = round( (degree - 32) *5/9 ,2)
    print(celcius)
elif unit.upper() == "C":
    farinhiet = round( degree * (9/5) + 32 ,2)
    print(farinhiet)
else:
    print(f"{unit} is not a valid unit")