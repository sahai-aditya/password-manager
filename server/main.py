from utils import connection
from utils.log import log, get_current_time
import config


server_socket = connection.init()
if not server_socket: # means socket creation/binding failed and exiting
    log(2)
    exit()

log(1) # socket creation succesful

server_socket.listen()
log(3, {"address": server_socket.getsockname()}) # server has started listening

try:
    while True:
        client_socket, client_addr = server_socket.accept()
        log(5, {"address": client_addr})
        client_socket.close()
        log(6, {"address": client_addr})

except KeyboardInterrupt:
    print(f"[{get_current_time()}] KEYBOARD INTERRUPT DETECTED")

server_socket.close()
log(4) # server socket closed