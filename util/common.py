import string
import os
import time
import sys
import ctypes
from time import sleep
from random import *
from colorama import Fore
from datetime import datetime

now = datetime.now().time().strftime("%H:%M:%S") 
date = datetime.now().strftime("%Y-%m-%d")


def setTitle(_str):
    ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | CookiesKush420")


def view_passwords():
    if os.path.isfile("Genned_Password.txt"):
        f = open("Genned_Password.txt")
        lines = f.readlines()
        for line in lines:
            print(line)
    else:
        clear()
        print(f'\n{Fore.LIGHTRED_EX}No generated passwords found! {Fore.RESET}')
        sleep(3)
        

def loading2():
    clear()
    setTitle(f"Welcome {os.getlogin()}")
    print(f"{Fore.LIGHTGREEN_EX}Booting up password generator{Fore.RESET}. . .")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")


def loading():
    clear()
    print(f"{Fore.LIGHTGREEN_EX}Generating very secure password{Fore.RESET}:")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")


def clear():
    os.system("cls")


def write_password(passwordd, name):
    with open ('Genned_Password.txt', 'a+') as f:
        f.writelines(f'\n---------------------COOKIESSERVICES.XYZ------------------------------\n\nDate: {date} | Time: {now}\nPassword name: {name}\nGenerated password: {passwordd}\n\n---------------------COOKIESSERVICES.XYZ------------------------------\n')
    f.close


def check(letters, punctuation, digits):
    if letters == True and punctuation == False and digits == False:
        characters = string.ascii_letters
    elif punctuation == True and digits == False and letters == False:
        characters = string.punctuation
    elif digits == True and punctuation == False and letters == False:
        characters = string.digits
    elif letters == True and punctuation == True and digits == False:
        characters = string.ascii_letters + string.punctuation
    elif letters == True and digits == True and punctuation == False:
        characters = string.ascii_letters + string.digits
    elif punctuation == True and digits == True and letters == False:
        characters = string.punctuation + string.digits
    elif letters == True and digits == True and punctuation == True:
        characters = string.ascii_letters + string.punctuation  + string.digits
    return characters


def generator(type, length):
    characterss = type
    lengths = length
    password =  "".join(choice(characterss) for x in range(lengths))
    return password