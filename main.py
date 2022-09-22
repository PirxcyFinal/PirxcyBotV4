import os
print('\033[94m[+] Packages Installing')
os.system("pip install --upgrade pip >/dev/null 2>&1")
print("[+] Packager Installed")
os.system("python3 -m poetry add LobbyBot >/dev/null 2>&1")
print("[+] Packages Installed, Installing With PIP")
os.system("pip install Lobbybot >/dev/null 2>&1")
print("[+] All Done, Loading PirxcyBot!")

import LobbyBot
print("Shit Boutta get real")
LobbyBot.run(ip="0.0.0.0",port=1942)
