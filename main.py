import os
from utils import read_menu, finish, create_menu, edit_menu, delete_menu, print_centered, wait, clear, print_menu


# Consts
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JOURNALS_PATH = BASE_PATH+r"/journals"
MAIN_MENU_PATH = BASE_PATH+r"/main_menu.txt"
LOGO = BASE_PATH + r"/logo.txt"

def print_logo():
    with open(LOGO, 'r') as f:
        for line in f:
            print_centered(line.rstrip("\n"))
            wait(0.1)
        wait(0.5)
        print()
        print_centered("Welcome to the enties editor!")
        print()
        wait(0.5)


def check_journals():
    if not os.path.exists(JOURNALS_PATH):
        os.mkdir(JOURNALS_PATH)


def main():
    clear()
    check_journals()
    print_logo()
    while(True):
        print_menu("main_menu")
        choice = input("Please choose your action:\n\n>>> ")
        match choice:
            case "1":
                read_menu()
            case "2":
                create_menu()
            case "3":
                edit_menu()
            case "4":
                delete_menu()
            case "0" | "exit":
                break
            case _:
                print("\nNot an option!")
                wait(3)
                clear()
                continue
    finish()
    
if __name__ == "__main__":
    main()
