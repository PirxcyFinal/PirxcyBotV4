import os
from importlib.metadata import version

print('\033[94m[+] Packager Installing')
os.system("pip install --upgrade pip >/dev/null 2>&1")
print("[+] Packager Installed, Installing PirxcyBot")
os.system("python3 -m poetry add LobbyBot")
os.system("python3 -m poetry add LobbyBot@latest")
print("[+] Packages Installed, Installing With PIP")
os.system("pip install Lobbybot >/dev/null 2>&1")
os.system("pip install --upgrade Lobbybot >/dev/null 2>&1")
os.system("python3 -m pip install --upgrade Lobbybot >/dev/null 2>&1")
os.system("python3 -m pip install Lobbybot >/dev/null 2>&1")
print("[+] All Done, Loading PirxcyBot!")

import LobbyBot

currentVersion =  version("LobbyBot")
print(f"\033[94m[+] Installed v{currentVersion} of PirxcyBot!\033[0m")
print("Shit Boutta get real")

LobbyBot.run(
  ip="0.0.0.0",
  port=1942
)
