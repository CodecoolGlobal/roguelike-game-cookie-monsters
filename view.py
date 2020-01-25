import data_manager
from termcolor import colored

BOARD_WIDTH = 100
BOARD_HEIGHT = 30

file_nicknames = "data_nickname.txt"
file_results = "results.txt"

label_results = ["Nickname", "Time", "Points"]

def start_descriptions():
<<<<<<< HEAD
    print(colored("Welcome to our cookie game! \n", "yellow"))
    print(colored("Maybe you want to play some game:D? \n", "yellow"))
    print(colored("So, first you have to give me some informations about You or who You want to be in our Magic World :) \n", "yellow"))
=======
    print(colored("\n Hello and welcome to our cookie game! \n", "yellow"))
    print(colored(" Maybe you want to play some game :D? \n", "yellow"))
    print(colored(" So, first you'll need to give me some informations about You and who You want to be in our Magic World :) \n", "yellow"))
>>>>>>> 4bff7847b7fca9f21c7d57c7cd99784a5fda9979

def bubble_sort(table):
    """function which sort all records in our table"""

    sort_table = table
    for i in range(len(sort_table)):
        j = len(sort_table)-1
        while j > i:
            if sort_table[j][2]< sort_table[j-1][2]:
                temp = sort_table[j]
                sort_table[j] = sort_table[j-1] 
                sort_table[j-1] = temp
            j-=1
    return sort_table  

def print_result(label, result):
    table_results = []
    table_results.insert(0,label)
    for line in result:
        table_results.append(line)
    widths = [max(map(len,col)) for col in zip(*table_results)]   
    i = 1
    table_new = []
    for record in table_results:
        record = "".join("|"+word.ljust(width) for word, width in zip(record, widths))+"|"
        table_new.append(record)
        i += 1


    floor = "|" + "-"*(len(record)-2) +"|"
    print("/","-"*(len(record)-4),"\\")
    
    i = 1
    for elem in table_new:
        print(elem, sep = "\n")
        if i < len(table_new):
            print(floor)
        i += 1    

    print("\\","-"*(len(record)-4),"/")    




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
        print("""Which TV show reminds you of your childhood? 
        Do you remember your childhood mornings - drinking milk, eating cookies and watching cartoons? 
        Talking about cookies …Do you know what starts with letter C? 
        Good enough for me, not only for me and you but for this main character also! 
        What are we talking about? Cookie starts with C! Are you already recognizing this song? 
        Moreover, do you know who likes it more than anything in this world? 
        We are talking about the blue, chubby, furry character we all watched when we were kids 
        (and sometimes nowadays too, right?).
        Cookie Monster is a Muppet on the long-running children's television show Sesame Street.""")
        i += 1

def exit_message():
    print('Goodbay, See you soon!')

