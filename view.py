from termcolor import colored
import time

BOARD_WIDTH = 100
BOARD_HEIGHT = 30

file_nicknames = "data_nickname.txt"
file_results = "results.txt"

label_results = ["Nickname","Points"]

def start_descriptions():
    print(colored("Welcome to our cookie game!".center(100), "yellow"))
    print(colored("Maybe you want to play some game:D?".center(100), "yellow"))
    print(colored("So, first I suggest you read instruction about our Magic World :)".center(100), "yellow"))
    print("\n")
    print(colored("About this Story:".center(100),'cyan', attrs=['bold', 'underline']))
    print(colored("Which TV show reminds you of your childhood?".center(100), 'cyan'))
    print(colored("Do you remember your childhood mornings - drinking milk, eating cookies and watching cartoons?".center(100) , 'cyan'))
    print(colored("Talking about cookies …Do you know what starts with letter C?\n".center(100), 'cyan'))
    print(colored("Good enough for me, not only for me and you but for this main character also!\n".center(100), 'cyan'))
    print(colored("What are we talking about? Cookie starts with C! Are you already recognizing this song?\n".center(100), 'cyan'))
    print(colored("Cookie Monster is a Muppet on the long-running children's television show Sesame Street.\n".center(100), 'cyan'))
    print(colored("Now you have a unique opportunity to become CookieMonster.\n".center(100), 'cyan'))
    print(colored("Your job will be get as many candies as you can.\n".center(100), 'cyan'))
    print(colored("On the other hands you'll be forced to mental effort as well as defeat the monsters.\n".center(100), 'cyan'))
    print(colored("So let's try your skills !!!".center(100), 'cyan'))
    time.sleep(15.0)

def bubble_sort(table):
    """function which sort all records in our table"""
    position_of_points = 1

    for i in range(len(table)):
        j = len(table)-1
        while j > i:
            if int(table[j][1]) > int(table[j-1][1]):
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
    index = 1
    print(colored("\n***** The best 5 players *****\n", 'green'))
    for line in results[0:5]:
        print(index, ". ", " : ".join(line))
        index += 1 


def print_menu(list_options):
    index = 1
    for key in list_options:
        if key != 0:
            print("(",index,")", list_options[key])
            index += 1 
    print("( 0 )", list_options[0])


def print_table(data):
    index = 0
    print("-" * 40)
    for key in data:
        if index == 0:
            print(colored(key.ljust(int(len("Level of difficulty"))), "cyan"),":",colored(data[key], "cyan")," 😈")
        else:
            print(colored(key.ljust(int(len("Level of difficulty"))), "cyan"),":",colored(data[key], "cyan"))
        index += 1       
    print("-" * 40) 

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

