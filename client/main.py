from utils import interface, connection


client_socket = connection.init()
if not connection.is_connected(client_socket):
    print("Sorry, couldn't connect to server. Please try again later.")
    connection.close(client_socket)

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
    connection.close(client_socket)

# invalid input
else:
    print("\nCould not understand, please try again!")
    connection.close(client_socket)

# if code makes it here means user exists
# implement logging in
# implement chatbot loop