# This module has functions related to sockets to avoid redundancy

import socket
import asyncio

import config
from utils.logger import log


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

async def handle_client(client_socket, active_clients):
    """
    Calls the necessary functions from data_manager to manipulate data.
    """
    client_addr = client_socket.getpeername()
    try:
        print(f"Fetching data from {client_addr} ...")
        await asyncio.sleep(5) # mimics IO tasks
        print(f"Data fetching from {client_addr} complete!")

    finally:
        client_socket.close()
        active_clients.remove(client_socket)
        log(6, {"address": client_addr})

    return client_socket