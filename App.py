Weight = float(input("Enter your weight: "))
Option = input("(P)ound or (K)ilogram: ")

#Kilo to pound
if Option.upper() == "K":
    Output = Weight * 2.20462
    print("It's " + str(Output) + (" Pounds"))
elif Option.upper() == "P":
    Output = Weight * 0.453592
    print("It's " + str(Output) + (" KG"))
else:
    print("Invalid input")
