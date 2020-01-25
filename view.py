import data_manager
from termcolor import colored
import time

BOARD_WIDTH = 100
BOARD_HEIGHT = 30

file_nicknames = "data_nickname.txt"
file_results = "results.txt"

label_results = ["Nickname", "Time", "Points"]

def start_descriptions():
    print(colored("Welcome to our cookie game! \n", "yellow"))
    print(colored("Maybe you want to play some game:D? \n", "yellow"))
    print(colored("So, first I suggest you read instruction about our Magic World :) \n", "yellow"))
    print(colored("About this Sotry:\n",'cyan', attrs=['bold', 'underline']))
    print(colored("""Which TV show reminds you of your childhood? 
        Do you remember your childhood mornings - drinking milk, eating cookies and watching cartoons? 
        Talking about cookies …Do you know what starts with letter C? 
        Good enough for me, not only for me and you but for this main character also! 
        What are we talking about? Cookie starts with C! Are you already recognizing this song?""", 'cyan'))
    time.sleep(15.0)
    print(colored("""        Cookie Monster is a Muppet on the long-running children's television show Sesame Street.\n""", 'cyan'))
    time.sleep(5.0)

def bubble_sort(table):
    """function which sort all records in our table"""

    for i in range(len(table)):
        j = len(table)-1
        while j > i:
            if int(table[j][2]) > int(table[j-1][2]):
                temp = table[j-1]
                table[j-1] = table[j]
                table[j] = temp
            j-=1 
    return table  

def print_result(label, results):
    table_results = []
    table_results.insert(0,label)
    for line in results:
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

def print_Hall_of_fame(results):
    i = 1
    print(colored("\n***** The best 5 players *****\n", 'green'))
    for line in results[0:5]:
        print(i, ". ", " : ".join(line))
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
            print(colored(key.rjust(int(BOARD_WIDTH/2)), "cyan"),":",colored(data[key], "cyan"))
        i += 1       
    print("-" * BOARD_WIDTH) 

def print_instruction():
    
    print(colored("Start? :\n",'cyan', attrs=['bold', 'underline']))
    print('\n')
    print("First, please enter your Nickname and decide which character you want to play. You may choose: CookieMan, he is the most powerful.")
    print("CookieMum she has rolling pin, which gives her additional points during fights.")
    print("CookieBaby has more life points than other characters.")
    print('\n')

    print("Play")
    print('\n')
    print("Use A to go up")
    print("Use S to go down")
    print("Use D to go right")
    print("Use A to go left")
    print('\n')

    print("Story")
    print('\n')

    print("You had been locked in secret maze, you are just trying to get out of here! Make sure to find as many items, as it is possible. They will be useful at the very end.")
    print('\n')
    

def print_images(images):
    for line in images:
        print(colored("".join(line), "blue"))



def exit_message():
    print('Goodbay, See you soon!')

