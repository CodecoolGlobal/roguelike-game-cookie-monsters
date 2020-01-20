
print("Hello in our cookie games \n")
print("Maybe Do you want to play some game :D? \n")
print("So, first you have to get mi some informations about You :) \n")

list_labels = ["Nickname", "Type", "Level of difficulty"]

game_player = {'race' : ['CookieMen', 'CookieMum', 'CookieBaby'],
            'Level_of_difficulty' : ['1', '2', '3'],
}

BOARD_WIDTH = 80
BOARD_HEIGHT = 20
file_nicknames = "data_nickname.txt"
file_results = "results.txt"

title = 'Hello'
list_options = {
                1 : 'Start Play',
                2 : 'Check the best Player',
                3 : 'Check options games',
                0 : 'Exit'
} 

exit_message = 'Goodbay, See you soon!'


def read_file_nicknames(file):
    file = open(file_nicknames, "r")
    lines = file.readlines()
    players_info = []
    for line in lines:
        item = line.strip("\n").split(",")
        players_info.append(item)
     
    return players_info 

def add_new_nicknames(data, file):
    with open(file_nicknames, 'a') as fil:
        record = []
        for key in data.keys():
            record.append(data[key])
        row = ",".join(map(str, record))
        fil.write(row + "\n")



def user_info(list_labels, player_nickname):
    player_data = {}
    print("Please, provide check data :)!")
    nickname = 0
    for elem in range(len(list_labels)):
        user_answer = input(str(list_labels[elem])+" : ")
        if elem == 0:
            read_file_nicknames(file_nicknames)
            for line in player_nickname:
                if user_answer == line[nickname]:
                    raise Exception("This user just exist. Try again and select other name")
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
    add_new_nicknames(player_data, file_nicknames)    
    return player_data


def print_result(label, result):
    table_results = []
    i = 1
    for elem in label:
        table_results.append(elem + " : " + result[i])
        i += 1   
    return table_results


def print_menu(title, list_options):
    
    print(title)
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
        

def main():
    print_menu(title, list_options)
    choice = input(str('Your choice is:' )) 
    while choice != '0':
        if choice == '1':
            try:
                print_table(user_info(list_labels,read_file_nicknames(file_nicknames)))
            except Exception as error:
                print(str(error))
                continue
        elif choice == '2':
            read_file_nicknames(file_results)
        #elif choice == '3': write code responsible for that
    print(exit_message)    


main()