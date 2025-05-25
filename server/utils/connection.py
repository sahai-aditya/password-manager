# This module has functions related to sockets to avoid redundancy

import socket
import asyncio

import config


def init():
    """
    Returns a TCP socket which uses IPv4 address if socket created successfully,
    otherwise returns error.
    """
    try:
        server_socket = socket.socket(
            family=socket.AF_INET, # means IPv4 address used
            type=socket.SOCK_STREAM, # means TCP socket created
        )
        server_socket.bind((config.SERVER_IP, config.SERVER_PORT))
    
    except socket.error as err:
        print(err)
        return False

    return server_socket

async def handle_client(client_socket, client_addr):
    """

    """