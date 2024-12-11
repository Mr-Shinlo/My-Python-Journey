#Critrea
#Username length must be less than 12
#Username must not contain spaces
#Username must not contain digits

username = input("Enter your username: ")
username.find(" ")
if len(username) > 12:
    print(f"the length of your username is {len(username)} words long. It must be lower than 12")
elif not username.find(" ") == -1:
    print("You cannot contain space in your username")
elif not username.isalpha() == -1:
    print("Your username contains digits")
else: print(f"Welcome {username}")