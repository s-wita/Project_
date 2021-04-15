email = input("Enter your Email: ").strip()

usernam = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {usernam} and your domain is {domain}")