from time import sleep
from colorama import Fore
from util.common import *


def main():
    clear()
    setTitle("Password Generator | MENU")
    print(f'''
    
    {Fore.LIGHTMAGENTA_EX}Welcome to Cookies password generator{Fore.RESET}. . .
    
    {Fore.RESET}[{Fore.CYAN}1{Fore.RESET}] {Fore.CYAN}Generate Password
    {Fore.RESET}[{Fore.CYAN}2{Fore.RESET}] {Fore.CYAN}View Generated Passwords
    {Fore.RESET}[{Fore.CYAN}420{Fore.RESET}] {Fore.RED}Exit
    {Fore.RESET}''')
    choice = str(input(f'{Fore.CYAN}Choice {Fore.YELLOW}>> {Fore.RESET}'))

    if choice == '1':
        clear()
        setTitle("Setting Password Options")
        name = str(input(f'{Fore.CYAN}Enter a name for the password to remember it {Fore.YELLOW}>> {Fore.RESET}'))
        letters = bool(input(f'{Fore.CYAN}Do u want to use {Fore.WHITE}Letters? {Fore.RESET}({Fore.CYAN}leave empty for no{Fore.RESET}) {Fore.YELLOW}>> {Fore.RESET}'))
        punctuation = bool(input(f'{Fore.CYAN}Do u want to use {Fore.WHITE}Punctuation? ({Fore.CYAN}leave empty for no{Fore.RESET}) {Fore.YELLOW}>> {Fore.RESET}'))
        digits = bool(input(f'{Fore.CYAN}Do u want to use {Fore.WHITE}Digits? ({Fore.CYAN}leave empty for no{Fore.RESET}) {Fore.YELLOW}>> {Fore.RESET}'))
        length = int(input(f'{Fore.CYAN}Enter desired password length {Fore.YELLOW}>> {Fore.RESET}'))
        if length < 8:
            clear()
            setTitle("Oh no")
            print(f'{Fore.LIGHTRED_EX}Please choose a length over 8 characters! {Fore.RESET}({Fore.CYAN}for saftey reasons{Fore.RESET})')
            sleep(3)
            main()
        elif length > 250:
            clear()
            setTitle("Oh no")
            print(f'{Fore.LIGHTRED_EX}Please choose a length under 250 characters! {Fore.RESET}')
            sleep(3)
            main()
        elif letters == False and punctuation == False and digits == False:
            clear()
            setTitle("Oh no")
            print(f'{Fore.LIGHTRED_EX}Please choose at least one character! {Fore.RESET}')
            sleep(3)
            main()
        type = check(letters, punctuation, digits)
        passwordd = generator(type, length)
        clear()
        setTitle("Generating Password. . .")
        loading()
        clear()
        write_password(passwordd, name)
        setTitle("Password Generated!")
        print(f'{Fore.LIGHTGREEN_EX}Generated password into txt file!{Fore.RESET}')
        input(f'\n{Fore.LIGHTYELLOW_EX}Press enter to continue. . .{Fore.RESET}')
        main()
    
    elif choice == '2':
        clear()
        print(f'{Fore.RESET}')
        setTitle("Viewing Generated Passwords")
        view_passwords()
        print(f'{Fore.RESET}')
        input(f'\n\n{Fore.LIGHTRED_EX}Press enter to continue. . .{Fore.RESET}')
        main()

    elif choice == '420':
        clear()
        setTitle("Exiting")
        print(f'{Fore.LIGHTRED_EX}Exiting password generator. . .{Fore.RESET}')
        sleep(3)
        exit()
    
    else:
        setTitle("Oh no")
        print(f'{Fore.LIGHTRED_EX}Please choose a valid choice! {Fore.RESET}({Fore.CYAN}1{Fore.RESET}, {Fore.CYAN}2{Fore.RESET}or {Fore.CYAN}420{Fore.RESET})')
        sleep(3)
        main()


if __name__ == '__main__':
    loading2()
    main()