import data_manager



BOARD_WIDTH = 100
BOARD_HEIGHT = 30

file_nicknames = "data_nickname.txt"
file_results = "results.txt"

label_results = ["Nickname", "Time", "Points", "Life"]

def start_descriptions():
    print("Hello in our cookie games \n")
    print("Maybe Do you want to play some game :D? \n")
    print("So, first you have to get me some informations about You :) \n")


def print_result(label, result):
    table_results = {}
    for elem in result:
        i = 0
        for key in label:
            table_results[key] = elem[i]
            i += 1    
    return table_results


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
            print(key.rjust(int(BOARD_WIDTH/2)),":",data[key])
        else:
            print("|","." * (BOARD_WIDTH - 4),"|")
            print(key.rjust(int(BOARD_WIDTH/2)),":",data[key])
        i += 1       
    print("-" * BOARD_WIDTH) 


def exit_message():
    print('Goodbay, See you soon!')