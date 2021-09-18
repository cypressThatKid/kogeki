from colorama import Fore
import sys

filename = input(Fore.YELLOW + "Bruted list" + Fore.RED + ": ")


with open(filename, "r") as f:
	data = f.read()

data = data.replace(' ', '~').replace(':', '~').strip('DUP~').strip('~DUP')

if ":23" in data:
  print("Sorry! Kogeki doesn't allow telnet bots!")
  sys.exit()

with open('kogitte.kogeki', 'a') as file:
  file.write(data)
  
print("Data appended to kogitte.kogeki!")
