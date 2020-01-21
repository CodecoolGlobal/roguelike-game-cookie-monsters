import data_manager
import view
import sys
import main



BOARD_WIDTH = 80
BOARD_HEIGHT = 20

file_nicknames = "data_nickname.txt"
file_results = "results.txt"


list_labels = ["Nickname", "Type", "Level of difficulty"]

game_player = {'race' : ['CookieMen', 'CookieMum', 'CookieBaby'],
            'Level_of_difficulty' : ['1', '2', '3'],
}

def user_info(list_labels, player_nickname):
    player_data = {}
    print("Please, provide check data :)!")
    nickname = 0
    for elem in range(len(list_labels)):
        user_answer = input(str(list_labels[elem])+" : ")
        if elem == 0:
            data_manager.read_file_nicknames(file_nicknames)
            for line in player_nickname:
                if user_answer == line[nickname]:
                    raise Exception("This user just exist. Try again and select other name")
            print("\nYou can choose who you want to be :D \nYour options: CookieMen, CookieWomen or CookieBaby\n")        
        elif elem == 1:
            if user_answer not in game_player['race']:
                raise Exception("It's not acceptable choice. Try again\n")       
        elif elem == 2:
            if user_answer not in game_player['Level_of_difficulty']:
                raise Exception("You choose only 1 ,2 or 3 level of difficulty\n")
            else:
                if user_answer == '1':
                    healthy = 5
                elif user_answer == '2':
                    healthy = 3
                elif user_answer == '3':
                    healthy = 1
                player_data["Healthy"] = healthy  
        player_data[list_labels[elem]] = user_answer
    data_manager.add_new_nicknames(player_data, file_nicknames)    
    return player_data

def run():
    
    try:
        view.print_table(user_info(list_labels,data_manager.read_file_nicknames(file_nicknames)))  
        main.run()  
    except Exception as error:
        print(str(error))
