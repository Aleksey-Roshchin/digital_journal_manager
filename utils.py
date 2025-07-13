import os, time, shutil
from datetime import datetime as dt

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
JOURNALS_PATH = BASE_PATH+r"/journals"

def return_to_main_menu():
    return None

def exit_the_program(x):
    if str(x).lower() in ("0", "exit", "quit"):
        print("Good bye!")
        exit()

def wait(wait_time):
    print(f"Returning to the Main Menu after {wait_time} seconds")
    time.sleep(wait_time)

def read_entry(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
    wait(5)


def read_all_entries(file_path):
    print('Reading entire journal')
    files = os.listdir(file_path)
    for file in files:
        with open(file_path + "/" + file, 'r') as f:
            print(f.read())
    wait(5)

def read_menu():
    print("\nThis is the Read Menu")
    # choose a journal
    journals = list_journals(JOURNALS_PATH)
    if journals:
        print("The following journals are available:")
        journal = choose(JOURNALS_PATH)
        entries = list_journals(journal)
        print('This journal have the following entries:')
        for i in range(len(entries)):
            print(f'{i + 1}. {entries[i]}')
        read_all = input('\nDo you want to read one entire or all of them?\n1. One entry\n2. All entries\n\n')
        if read_all == "1":
            entry = choose(journal)
            read_entry(entry)
        elif read_all == "2":
            read_all_entries(journal)
        else:
            print("Not an option")          
    else:
        print("There are no journals yet. Please, create the journal first.")
        return_to_main_menu()


# def choose(files):
#     for i in range(len(files)):
#         print(f'{i+1}. {files[i]}')
#     choice = int(input('\nChoose the available journal or file: ')) - 1
#     file = files[choice]
#     print(f'You chose {file}')
#     return JOURNALS_PATH + "/" + file

def choose(file_path):
    files = list_journals(file_path)
    for i in range(len(files)):
        print(f'{i+1}. {files[i]}')
    choice = int(input('\nChoose the available journal or file: ')) - 1
    file = files[choice]
    print(f'You chose {file}')
    return file_path + "/" + file

def list_journals(file_path):
    journals = os.listdir(file_path)
    return journals

def create_new_journal(file_path):
    new_journal = input('Enter the new journal name: ')
    os.mkdir(file_path + '/' + new_journal)
    print(f'The journal "{new_journal} has been created')
    return file_path + '/' + new_journal

def create_new_entry(file_path):
    new_entrie = input('Enter the new entry name: ') + '.txt'
    with open(file_path + "/" + new_entrie, 'w') as f:
        pass
    print(f'The entry "{new_entrie}" has been created\n')
    return file_path + "/" + new_entrie

def create_menu():
    print('\nThis is the Create Menu')
    # choose a journal or create new
    journals = list_journals(JOURNALS_PATH)
    if journals:
        journal = choose(JOURNALS_PATH)
        new_entry = create_new_entry(journal)
    else:
        print("There are no journals available. You should create one first.")
        new_journal = create_new_journal(JOURNALS_PATH)
        new_entry = create_new_entry(new_journal)
    
    # get user input for the new entry
    choice = input(f'Do you want to add something to the {new_entry} entry?\n1. Yes\n2. No (Return to the Main Menu)\n\n')
    match choice:
        case "1":
            edit_entry(new_entry)
        case "2":
            return_to_main_menu()

    # create new journal

def edit_entry(file_path):
    with open(file_path, 'w') as f:
        user_input = input('What are you want to add to the entry?\n')
        f.write(dt.now().strftime("%d/%m/%Y %H:%M:%S"))
        f.write("\n" + user_input + "\n\n")

def edit_menu():
    print("This is the Edit menu")
    # choose journal
    # choose entry 
    # print entry
    # get user input for the entry
    # append entry with the user input

def delete_menu():
    print("This is the Delete menu")
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
            wait(5)
        case "2":
            shutil.rmtree(journal)
            print(f"The journal {journal} has been deleted\n")
            wait(5)


    

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
        
