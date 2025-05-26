from datetime import datetime
from pytz import timezone


def get_current_time():
    """
    Returns current time in required string format
    """
    current_time = datetime.now(timezone("Asia/Kolkata"))
    current_time = current_time.strftime("%H:%M:%S")
    return current_time

def log(msg_type, data=None):
    """
    1 -> server socket created succesfully
    2 -> server socket creation failed
    3 -> server socket starts listening : {"address": (IPv4, port)}
    4 -> server socket closed
    5 -> client connected : {"address": (client IPv4, client port)}
    6 -> client disconnected : {"address": (client IPv4, client port)}
    """
    current_time = get_current_time()
    message = ""

    if msg_type == 1:
        message = "SERVER SOCKET CREATED SUCCESSFULLY"

    elif msg_type == 2:
        message = "SERVER CREATION FAILED"

    elif msg_type == 3:
        message = f"SERVER LISTENING AT {data['address']} (PRESS CTRL+C TO CLOSE IT)"

    elif msg_type == 4:
        message = "SERVER SOCKET CLOSED"

    elif msg_type == 5:
        message = f"CLIENT CONNECTED FROM {data['address']}"

    elif msg_type == 6:
            message = f"CLIENT DISCONNECTED FROM {data['address']}"
    
    if message:
        print(f"[{current_time}] {message}")