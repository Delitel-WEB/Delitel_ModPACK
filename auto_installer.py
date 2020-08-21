import os
import shutil

os.system("clear")
print("Начинаем установку Delitel ModPACK!")
os.system("clear")
os.system("cd /storage/emulated/0/BombSquad")
os.system("pkg update")
os.system("pkg install git")
os.system("clear")
os.system("git clone https://github.com/Delitel-WEB/Delitel_ModPACK.git")
os.system("clear")
shutil.move("/storage/emulated/0/BombSquad/Delitel_ModPACK/sys", "/storage/emulated/0/BombSquad/sys")
shutil.move("/storage/emulated/0/BombSquad/Delitel_ModPACK/about_modpack.json", "/storage/emulated/0/BombSquad/about_modpack.json")
shutil.move("/storage/emulated/0/BombSquad/Delitel_ModPACK/menuMusic.ogg", "/storage/emulated/0/BombSquad/menuMusic.ogg")
shutil.move("/storage/emulated/0/BombSquad/Delitel_ModPACK/announceFive.ogg", "/storage/emulated/0/BombSquad/announceFive.ogg")
shutil.move("/storage/emulated/0/BombSquad/Delitel_ModPACK/victoryMusic.ogg", "/storage/emulated/0/BombSquad/victoryMusic.ogg")
os.system("clear")
os.remove("auto_installer.py")




print("Готово!")
