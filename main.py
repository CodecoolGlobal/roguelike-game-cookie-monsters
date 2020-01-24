import util
import dictionaries
import engine
import ui
import time
import players
import menu_start
import view
from termcolor import colored

def main():

    # initial board
    board = engine.create_board(dictionaries.BOARD['BOARD_1'])

    # initial level
    level = 'BOARD_1'   #tutaj bedzie musialo sie zmieniac, zeby odpalil drugi level 

    # initial key
    key = ''

    menu_start.run()

    while True:    
        
        engine.first_level(board, dictionaries.inventory, dictionaries.player, level, dictionaries.others, dictionaries.items, 1, key, time, dictionaries.BOARD)
        
        engine.second_level(board, dictionaries.inventory, dictionaries.player, level, dictionaries.others, dictionaries.items, 2, key, time, dictionaries.BOARD)
        
        engine.third_level(board, dictionaries.inventory, dictionaries.player, level, dictionaries.others, dictionaries.items, 3, key, time, dictionaries.BOARD)
        
    

    if level == 'WIN':

        while True:
            print('YOU WON!!!')
            time.sleep(0.7)
            print('🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪')
            time.sleep(0.7)

    elif level == 'QUIT':

        while True:
            print('GAME OVER')
            time.sleep(0.7)


if __name__ == '__main__':
    main()
