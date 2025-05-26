import asyncio

from utils import connector
from utils.logger import log, get_current_time
import config


async def main():
    try:
        while True:
            client_socket, client_addr = await asyncio.get_running_loop().sock_accept(server_socket)
            log(5, {"address": client_addr})
            asyncio.create_task(connector.handle_client(client_socket, client_addr))

    except asyncio.CancelledError:
        print(f"[{get_current_time()}] KEYBOARD INTERRUPT DETECTED")

server_socket = connector.init()
if not server_socket: # means socket creation/binding failed and exiting
    log(2)
    exit()

log(1) # socket creation succesful

server_socket.listen()
log(3, {"address": server_socket.getsockname()}) # server has started listening

asyncio.run(main())

server_socket.close()
log(4) # server socket closed