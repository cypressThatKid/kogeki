# Kogeki | The Futurisitc Botnet
![Botnet Image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftruxgoservers.com%2Fblog%2Fwp-content%2Fuploads%2F2021%2F04%2Fbotnet.png&f=1&nofb=1 "KOGEKI")
### The first-ever malware-less botnet that can send DDoS Attacks, Mass Mail, Run Reverse Shells and MORE!

# Disclaimer
By downloading this software, you agree that I am held harmless for any damages, losses, etc.. that is caused by this software. This was made for educational purposes and is not meant to cause harm to any computer/network.

The login feature is just a feature and is not intended to provide security. To ensure security, make sure you are using SSH keys or a strong password to make sure that a threat actor could not gain access to the server running Kogeki!

# Special Features
Kogeki is not like any other botnets, and it does not have a port that you connect through. Instead, the CNC can be ran from a Python script to prevent un-authorized access.

# How Are Bots Infected

Unlike other botnets, Kogeki does not plant malware on the zombie computers. Instead, it connects to the zombies each time the botnet is started (via SSH) to avoid leaving trails that could lead back to the CNC.

# Setup

In order to setup your Kogeki botnet, follow the simple step below:

1. Run "python3 setup/setup.py" to install dependencies and to set your login credentials

# Scanning Process

In order to scan bots to the botnet, follow these simple steps:

1. Collect the hosts that you have PERMISSION to infect in a list.
2. Brute force (or write) the login information to those hosts in this format: <username>:<password>:<host>
3. Save the brute force hosts with their login information to a file named "bruted.txt"
4. Run the "python3 scanning/bruted.py" and input the name of your bruted file
5. Run 'python3 scanning/compcheck.py kogitte.kogeki'. This will validate your bruted list to make sure that all the hosts are using SSH and not Telnet, commands can be ran and the login credentials work
6. Run the botnet (python3 botnet.py) and your bots will load on startup.

# Functions
Kogeki has many functions that can be listed by typing "help" in the command prompt (when Kogeki is running).

# Screenshots
  
![](images/kogeki1)
![](images/kogeki2)
![](images/kogeki3)
![](images/kogeki4)

