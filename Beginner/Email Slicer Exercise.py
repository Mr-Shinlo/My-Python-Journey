#1234shinlo@gmail.com

email = input("Enter your email: ")

indexing = email.index("@")
username = email[0:indexing]
domain = email[indexing + 1:]

print(f"Your username is {username} and your domain is {domain}.")