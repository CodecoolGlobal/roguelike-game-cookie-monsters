import data_manager
from termcolor import colored

BOARD_WIDTH = 100
BOARD_HEIGHT = 30

file_nicknames = "data_nickname.txt"
file_results = "results.txt"

label_results = ["Nickname", "Time", "Points", "Life"]

def start_descriptions():
    print(colored("Hello and welcome to our cookie game! \n", "yellow"))
    print(colored("Maybe you want to play some game:D? \n", "yellow"))
    print(colored("So, first you have to give me some informations about You or who You want to be in our Magic World :) \n", "yellow"))

def print_result(label, result):
    table_results = []
    table_results.insert(0,label)
    for line in result:
        table_results.append(line)

    i = 1
    for elem in table_results:
        print(i, ". ", elem)
        i += 1 
    


def print_menu(list_options):
    i = 1
    for key in list_options:
        if key != 0:
            print("(",i,")", list_options[key])
            i += 1 
    print("( 0 )", list_options[0])


def print_table(data):
    i = 0
    print("-" * BOARD_WIDTH)
    for key in data.keys():
        if i == 0:
            print(colored(key.rjust(int(BOARD_WIDTH/2)),"cyan"),":",colored(data[key], "cyan"))
        else:
            print("|","." * (BOARD_WIDTH - 4),"|")
            print(colored(key.rjust(int(BOARD_WIDTH/2)), "cyan"),":",colored(data[key], "cyan"))
        i += 1       
    print("-" * BOARD_WIDTH) 

def print_instruction():
    i = 0
    while i == 0:
        print("Hello now I'm empty but in the future....")
        i += 1

def exit_message():
    print('Goodbay, See you soon!')


