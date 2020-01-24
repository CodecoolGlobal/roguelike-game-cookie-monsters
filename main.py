import util
import dictionaries
import engine
import ui
import time
import players
import menu_start
import view
from art import text2art
from termcolor import colored

def main():

    # initial board
    board = engine.create_board(dictionaries.BOARD['BOARD_1'])

    # initial level
    level = 'BOARD_1'   #tutaj bedzie musialo sie zmieniac, zeby odpalil drugi level 

    # initial key`
    key = ''

    menu_start.run()

    while True:    
        
        engine.first_level(board, dictionaries.inventory, dictionaries.player, level, dictionaries.others, dictionaries.items, 1, key, time, dictionaries.BOARD)
        
        engine.second_level(board, dictionaries.inventory, dictionaries.player, level, dictionaries.others, dictionaries.items, 2, key, time, dictionaries.BOARD)
        
        engine.third_level(board, dictionaries.inventory, dictionaries.player, level, dictionaries.others, dictionaries.items, 3, key, time, dictionaries.BOARD)
        
    

    if level == 'WIN':
        util.clear_screen()
        ui.display_board(board)
        print(text2art("VICTORY!",font='block',chr_ignore=True))
        while True:
            time.sleep(0.7)
            print('🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪')

    elif level == 'QUIT':
        util.clear_screen()
        ui.display_board(board)
        print(text2art("GAME OVER!",font='block',chr_ignore=True))
        time.sleep(10.7)
        


if __name__ == '__main__':
    main()
