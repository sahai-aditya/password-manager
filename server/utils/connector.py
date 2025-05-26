# This module has functions related to sockets to avoid redundancy

import socket
import asyncio
from struct import unpack

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

async def receive_data(client_socket):
    """
    Receives data from a particular client.
    Returns None if client disconnects without sending any data.
    """
    length = await asyncio.get_running_loop().sock_recv(client_socket, 4)

    if not length:
        return None

    length = unpack("!I", length)[0]
    data = b""

    while len(data) < length:
        packet = await asyncio.get_running_loop().sock_recv(client_socket, length - len(data))
        data += packet

    return data.decode("UTF-8")

async def handle_client(client_socket, active_clients):
    """
    Calls the necessary functions from data_manager to manipulate data.
    """
    client_addr = client_socket.getpeername()
    try:
        data = await receive_data(client_socket)
        print(f"'{data}'")

    finally:
        client_socket.close()
        active_clients.remove(client_socket)
        log(6, {"address": client_addr})

    return client_socket