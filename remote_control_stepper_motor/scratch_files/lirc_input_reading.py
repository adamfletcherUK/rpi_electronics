import socket
import lirc

# client = lirc.Client(
#   connection=lirc.LircdConnection(
#     address="/var/run/lirc/lircd",
#     socket=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM),
#     timeout = 5.0
#   )
# )


client = lirc.Client()

print(client.version())