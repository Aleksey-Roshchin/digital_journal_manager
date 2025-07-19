import os, time, shutil
from datetime import datetime as dt

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JOURNALS_PATH = BASE_PATH + r"/journals"
MENU_PATH = BASE_PATH + r"/menu/"
NAVIGATION_INSTRACTION = MENU_PATH + r"navigation_instraction.txt"
USER_INPUT_FORM = "\n\n>>> "

def finish(x=0):
    if x == 0:
        clear()
        with open(MENU_PATH + r"finished.txt") as f:
            print(f.read())
            wait(1)
        exit()

def clear():
    os.system("clear")

def print_centered(text):
    width = shutil.get_terminal_size().columns
    padding = (width - len(text)) // 2
    print(" " * max(padding, 0) + text)

def print_menu(menu):
    clear()
    with open(MENU_PATH + menu + ".txt", 'r') as f1, open(NAVIGATION_INSTRACTION, 'r') as f2:
        print(f1.read() + "\n")
        print(f2.read() + "\n")

def return_to_main_menu():
    print("\nReturning to the Main Menu...")
    wait(2)
    return None

def return_to_current_menu():
    pass

def wait(wait_time):
    #print(f"Returning to the Main Menu after {wait_time} seconds\n")
    time.sleep(wait_time)

def press_to_continue():
    input('Press Enter to continue')


def read_entry(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
    press_to_continue()


def read_all_entries(file_path):
    journal_name = resource_name(file_path)
    print(f'There is a content of all entries of the "{journal_name}" journal:\n')
    files = os.listdir(file_path)
    for file in files:
        with open(file_path + "/" + file, 'r') as f:
            print(f.read())
    press_to_continue()

def is_option(choice, files, file_path):
    while True:
        try:
            choice = int(choice) - 1
            file = files[choice]
            print(f'You chose the file {file}')
            return file_path + "/" + file
        except Exception:
            print('\nNot an option!\nPlease choose the option from the list.')
            wait(1)
            choice = input(f'\nChoose the available one:{USER_INPUT_FORM}')
            # clear()

def choose(file_path):
    files = list_journals(file_path)
    for i in range(len(files)):
        print(f'{i+1}. {files[i]}')
    choice = input(f'\nChoose the available one:{USER_INPUT_FORM}')
    if choice.lower() in ('main menu', '"main menu"', 'main_menu', '"main_menu"'):
        return_to_main_menu()
    elif choice.lower() in ('0', 'exit', '"exit"', 'esc', 'escape'):
        finish()
    else:
        return is_option(choice, files, file_path)


def list_journals(file_path):
    journals = os.listdir(file_path)
    return journals

def create_new_journal(file_path):
    new_journal = input('Enter the new journal name: ')
    os.mkdir(file_path + '/' + new_journal)
    print(f'The journal "{new_journal} has been created')
    return file_path + '/' + new_journal

def resource_name(file_path):
    return file_path.split("/")[-1]

def create_new_entry(file_path):
    new_entrie = input(f'Enter the new entry name:{USER_INPUT_FORM}') + '.txt'
    with open(file_path + "/" + new_entrie, 'w') as f:
        pass
    print(f'The entry "{new_entrie}" has been created\n')
    return file_path + "/" + new_entrie

def edit_entry(file_path, edit_mode):
    with open(file_path, edit_mode) as f:
        user_input = input('What are you want to add to the entry?\n')
        f.write(dt.now().strftime("%d/%m/%Y %H:%M:%S"))
        f.write("\n" + user_input + "\n\n")

##### All Menus #####

def read_menu():
    print_menu("read_menu")
    # choose a journal
    journals = list_journals(JOURNALS_PATH)
    if journals:
        print("The following journals are available:")
        journal = choose(JOURNALS_PATH)
        if journal is None:
            return None
        journal_name = resource_name(journal)
        print_menu("read_menu")
        print(f'You chose {journal_name}')
        entries = list_journals(journal)
        print('This journal have the following entries:')
        for i in range(len(entries)):
            print(f'{i + 1}. {entries[i]}')
        read_all = input(f'\nDo you want to read one entire or all of them?\n1. One entry\n2. All entries\n3. Return to choosing a journal\n\n{USER_INPUT_FORM}')
        if read_all == "1":
            print_menu("read_menu")
            print(f"What entry you want to open?")
            entry = choose(journal)
            if entry is None:
                return None
            read_entry(entry)
            read_menu()
        elif read_all == "2":
            print_menu("read_menu")
            read_all_entries(journal)
            read_menu()
        elif read_all.lower() in ("3", "back"):
            read_menu()
        else:
            print("Not an option")          
    else:
        print("There are no journals yet. Please, create the journal first.")
        return_to_main_menu()


def create_menu():
    print_menu("create_menu")
    # choose a journal or create new
    choice = input(f"\nWhat do you want to do?\n1. Create new entry\n2. Create new journal\nAny other key - Return to the Main Menu{USER_INPUT_FORM}")
    match choice:
        case "1":
            journals = list_journals(JOURNALS_PATH)
            if journals:
                print_menu("creating_entry")
                print("The following journals are available:")
                journal = choose(JOURNALS_PATH)
                journal_name = resource_name(journal)
                print_menu("creating_entry")
                print(f"You are in {journal_name}")
                new_entry = create_new_entry(journal)
                # get user input for the new entry
                choice = input(f'Do you want to add something to the {new_entry} entry?\n1. Yes\n2. No (Return to the Main Menu)\n\n')
                match choice:
                    case "1":
                        edit_entry(new_entry, 'w')
                    case "2":
                        return_to_main_menu()
            else:
                print_menu("creating_entry")
                print("There are no journals available. You should create one first.")
                new_journal = create_new_journal(JOURNALS_PATH)
                new_entry = create_new_entry(new_journal)
        case "2":
            journals = list_journals(JOURNALS_PATH)
            create_new_entry(JOURNALS_PATH)
        case _:
            return_to_main_menu()


def edit_menu():
    print_menu("edit_menu")
    journals = list_journals(JOURNALS_PATH)
    if journals:
        journal = choose(JOURNALS_PATH)
        entry = choose(journal)
        print(f"{resource_name(entry)} has the following information:\n")
        read_entry(entry)
        choice = input(f"\nWhat do you want to do with the entry?\n1. Add content\n2. Replace content\n3. Return to the Edit Menu\nAny other key - Return to the Main Menu\n\n{USER_INPUT_FORM}")
        match choice:
            case "1":
                edit_entry(entry, 'a')
            case "2":
                edit_entry(entry, 'w')
            case "3":
                edit_menu()
            case _:
                return_to_main_menu()
                

def delete_menu():
    print_menu("delete_menu")
    # choose a journal
    print("Please select the journal")
    journal = choose(JOURNALS_PATH)
    # choose an entry or whole
    choice = input('\nDo you want to delete one file or entire journal?\n1. One file\n2. Entire journal\n\n')
    # deleting
    match choice:
        case "1":
            entry = choose(journal)
            os.remove(entry)
            print(f"The entry {entry} has been deleted\n")
            press_to_continue()
        case "2":
            shutil.rmtree(journal)
            print(f"The journal {journal} has been deleted\n")
            press_to_continue()



    

# def choose(path):
#     if not (os.path.exists(path)):
#         raise FileNotFoundError
#     file_list = os.listdir(path)
#     if file_list:
#         print('There are available journals and files:')
#         for i in range(len(file_list)):
#             print(f'{i+1}. {file_list[i]}')
#         choice = int(input("\nEnter the number in the list: "))
#         return file_list[choice - 1]
#         # new_path = os.path.join(path, file_list[choice-1])
#         # if not (os.path.exists(new_path)):
#         #     return choose(path)
#         # return new_path

# def read_entry(path):
#     with open(path, "rb") as f:
#         data = f.read().decode()
#         print(data)
        
