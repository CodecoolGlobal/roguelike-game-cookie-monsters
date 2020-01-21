import data_manager
import view
import sys
import players


file_nicknames = "data_nickname.txt"
file_results = "results.txt"


list_options = {
                1 : 'Start Play',
                2 : 'Check the best Player',
                3 : 'Check options games',
                0 : 'Exit'
} 


label_results = ["Nickname", "Time", "Points", "Life"]


def run():
    view.start_descriptions()
    view.print_menu(list_options)
    choice = input(str('Your choice is:' )) 
    while True:
        if choice == '1':
            players.run()  
        elif choice == '2':
            view.print_result(label_results,data_manager.read_file_nicknames(file_results))
        #elif choice == '3': write code responsible for that
        elif choice == '0':
            view.exit_message() 
            sys.exit()   
