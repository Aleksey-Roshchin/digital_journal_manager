import os
from utils import read_menu, create_menu, edit_menu, delete_menu


# Consts
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JOURNALS_PATH = BASE_PATH+r"/journals"
MAIN_MENU_PATH = BASE_PATH+r"/main_menu.txt"

def print_menu():
    with open(MAIN_MENU_PATH, 'r') as file:
        print(file.read() + "\n")

def check_journals():
    if not os.path.exists(JOURNALS_PATH):
        os.mkdir(JOURNALS_PATH)


def main():
    check_journals()
    while(True):
        print_menu()
        choice = input("Please choose your action: ")
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
                print("Not an option!")
                continue
    print("Finished, bye!")
    
if __name__ == "__main__":
    main()