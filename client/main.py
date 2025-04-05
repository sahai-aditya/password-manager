from utils import interface, connection

"""
Will implement socket feature later.
Code will go here that will look for the server and connect to it.
"""

print("\nEnter 'q' at any time to quit.")
print("\n1. Sign In")
print("2. Sign Up")
signin_signup = input("\nEnter option number\n>>> ").strip()

# sign in
if signin_signup == "1":
    username, password = interface.get_signin_info()

# sign up
elif signin_signup == "2":
    username, password = interface.get_signup_info()

# quit
elif signin_signup.lower() == "q":
    connection.close()

# invalid input
else:
    print("\nCould not understand, please try again!")
    connection.close()

# if code makes it here means user exists
# implement logging in
# implement chatbot loop