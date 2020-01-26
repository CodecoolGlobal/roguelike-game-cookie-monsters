import data_manager
import view
import sys
import players
import main
from termcolor import colored
import util

file_nicknames = "data_nickname.txt"
file_results = "results.txt"

list_labels = ["Nickname", "Type", "Level of difficulty"]
player_nickname = data_manager.read_file_nicknames(file_nicknames)
list_options = {
                1 : 'Start Play',
                2 : 'Check all of results',
                3 : 'Check instruction game',
                4 : 'Hall of Fame',
                0 : 'Exit'
} 

choice_options = ['0', '1', '2', '3', '4']

label_results = ["Nickname", "Points"]


def run():
    print(colored("MAIN MENU", 'yellow'))
    view.print_menu(list_options)
    print("\n")
    choice = input(str(colored('Your choice is: ', "green")))
    while choice in choice_options:
        if choice == '1':
            util.clear_screen()
            try:
                players.user_info(list_labels, player_nickname)
                break               
            except Exception as error:
                print(str(error))
                continue
        elif choice == '2':
            view.print_result(label_results,data_manager.read_file_nicknames(file_results))
            print("\n")
            user_decision = input("If you want to come to main menu, please press 0 :")
            if user_decision == "0" :
                util.clear_screen()
                run()
            else:
                print("try again")
        elif choice == '3':
            view.print_instruction()
            print("\n")
            user_decision = input("If you want to come to main menu, please press 0 :")
            if user_decision == "0" :
                util.clear_screen()
                run()
            else:
                print("try again")
        elif choice == '4':
            view.print_Hall_of_fame(view.bubble_sort(data_manager.read_file_nicknames(file_results)))
            print("\n")
            user_decision = input("If you want to come to main menu, please press 0 :")
            if user_decision == "0" :
                util.clear_screen()
                run()
            else:
                print("try again")        
        elif choice == '0':
            view.exit_message() 
            sys.exit()      
    else:
        print("Incorrect input. Try again, please!!!")    
  
