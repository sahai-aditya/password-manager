from utils import interface, connector


client_socket = connector.init()
if not connector.is_connected(client_socket):
    print("Sorry, couldn't connect to server. Please try again later.")
    connector.close(client_socket)

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
    connector.close(client_socket)

# invalid input
else:
    print("\nCould not understand, please try again!")
    connector.close(client_socket)

# if code makes it here means user exists
# implement logging in
# implement chatbot loop

connector.send_data(client_socket, username)
connector.close(client_socket)