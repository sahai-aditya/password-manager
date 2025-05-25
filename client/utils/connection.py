# This module has functions related to sockets to avoid redundancy

import socket
from time import sleep

import config


def init():
    """
    Returns client socket, tries to connect to server 10 times.
    """
    client_socket = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
    )

    for _ in range(10):
        try:
            client_socket.connect((config.SERVER_IP, config.SERVER_PORT))

        except ConnectionRefusedError:
            print("Couldn't connect to server. Trying again ...")
            sleep(1)

        finally:
            if is_connected(client_socket):
                break

    return client_socket

def is_connected(client_socket):
    """
    Returns true if client is connected to server socket, otherwise false.
    """
    try:
        server_ip, server_port = client_socket.getpeername()

    except OSError:
        return False

    if server_ip == config.SERVER_IP and server_port == config.SERVER_PORT:
        return True

    return False

def close(client_socket):
    """
    Takes in the socket object and closes it cleanly.
    (To be implemented later)
    """
    client_socket.close()
    exit()