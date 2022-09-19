import os
os.system("pip install --upgrade pip")
os.system("pip install Lobbybot")


import LobbyBot
LobbyBot.run(ip="0.0.0.0",port=1942)
