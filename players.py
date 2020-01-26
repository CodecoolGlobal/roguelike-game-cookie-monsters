import data_manager
import view
import sys
import main
import dictionaries
from termcolor import colored

BOARD_WIDTH = 80
BOARD_HEIGHT = 20

file_nicknames = "data_nickname.txt"
file_results = "results.txt"


list_labels = ["Nickname", "Type", "Level of difficulty"]

game_player = {'race' : ['1', '2', '3'],
            'Level_of_difficulty' : ['1', '2', '3'],
}

def user_info(list_labels, player_nickname):

    print("Please, provide your's nickname: ")

    nickname = 0
    for elem in range(len(list_labels)):
        user_answer = input(str(list_labels[elem])+" : ")
        if elem == 0:
            data_manager.read_file_record(file_nicknames)
            for line in player_nickname:
                if user_answer == line[5]:
                    raise Exception("This user already exist. Try again and select other name")
            print("\nYou can choose who you want to be :D \nYour options: (1)CookieMan, (2)CookieMum or (3)CookieBaby\n")        
        
        elif elem == 1:
            if user_answer not in game_player['race']:
                raise Exception(colored("It's not acceptable choice. Try again\n", "red"))   
            else:
                if user_answer == '1':
                    print(colored("You are a CookieMan so you are more powerful than you think", 'magenta'))
                    dictionaries.player['player_power'] = 5
                elif user_answer == '2':
                    print(colored("You chose CookieMum and you get rolling pin :D!!!It can be useful later",'magenta' ))
                    dictionaries.player['additional_elements'] = 'rolling_pin'
                elif user_answer == '3':    
                    print(colored("Hello little boy ;) Because you're still a child, You get a more life_points ", 'magenta'))
                    dictionaries.player['player_life'] = 2
                print("\nOptions: (1) Easy, (2) Medium, (3) Hard \n")
        elif elem == 2:
            if user_answer not in game_player['Level_of_difficulty']:
                raise Exception(colored("You choose only (1)Easy ,(2) Medium or (3)Hard level of difficulty\n", "red"))
            else:
                if user_answer == '1':
                    dictionaries.player['player_life'] = dictionaries.player['player_life'] + 5
                elif user_answer == '2':
                    dictionaries.player['player_life'] = dictionaries.player['player_life'] + 3
                elif user_answer == '3':
                    dictionaries.player['player_life'] = dictionaries.player['player_life'] + 1
     
        dictionaries.player[list_labels[elem]] = user_answer
    data_manager.add_new_record(dictionaries.player, file_nicknames)    
    

def data_to_print(data):
    keys = ["Nickname", "Type", "Level of difficulty"]
    data_print = {key : dictionaries.player[key] for key in keys }
    for key in data_print:
        if key == "Type":
            if data_print[key] == '1':
                data_print[key] = 'CookieMan'
            elif data_print[key] == '2':
                data_print[key] = 'CookieMum'
            else:
                data_print[key] = 'CookieBaby'
        elif key == "Level of difficulty":  
            if data_print[key] == '1':
                data_print[key] = 'Easy'
            elif data_print[key] == '2':
                data_print[key] = 'Medium'
            else:
                data_print[key] = 'Hard'              
    return data_print

def count_points():
    points = dictionaries.player['player_power'] + (int(dictionaries.player['player_life']) * 2)
    data = {
        'Nickname' : dictionaries.player['Nickname'],
        'points' : points
        }   
    return data

def add_results(data, result):
    if dictionaries.player['used_code'] == False:
        data_manager.add_new_record(data,file_results)
    else:
        print('You cheated') 