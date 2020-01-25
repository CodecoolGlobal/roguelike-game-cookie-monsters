import util
import dictionaries
import engine
import ui
import time
import players
import menu_start
import view
from termcolor import colored
from PIL import Image


with Image.open("cookiemonster.jpg") as img:
        img.show()

def main():
   
    # initial board
    board = engine.create_board(dictionaries.BOARD['BOARD_1'])

    # initial level
    level = 'BOARD_1'

    # initial key
    key = ''

    menu_start.run()
    while level != 'WIN' and level != 'QUIT':
        
        # BOARD 1
        if level == 'BOARD_1':
            
            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(1.0)
            util.clear_screen()

            while level == 'BOARD_1':

                view.print_table(players.data_to_print(dictionaries.player))

                # Set up board
                board = engine.create_board(dictionaries.BOARD[level])
                board = engine.put_player_on_board(board, dictionaries.player)
                board = engine.put_other_on_board(board, dictionaries.others)
                board = engine.put_item_on_board(board, dictionaries.items) 

                # Display essential info
                ui.print_player_essential_atributes(dictionaries.player)
                
                # Display board
                ui.display_board(board)

                # Interaction whit items
                engine.item_vs_player(dictionaries.inventory, dictionaries.items, dictionaries.player)

                # Display inventory
                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(dictionaries.inventory)

                # Player input
                key = util.key_pressed()
                                
                # Movement
                engine.movement(board, dictionaries.player, key, dictionaries.others)

                # Clear screen
                util.clear_screen()

                # Interaction with other characters
                if engine.player_meets_other(dictionaries.others, dictionaries.player) != False:
                    other = engine.player_meets_other(dictionaries.others, dictionaries.player)
                    if other == 'other3':
                        print("Moooooo!")
                    elif other == 'other2':
                        print('Bon Appétit!')
                    else:
                        engine.player_vs_other_quiz(dictionaries.player, other, dictionaries.others, dictionaries.inventory, dictionaries.others[other]['questions'])

                # Gate and level change handling
                level = engine.player_enters_gate(level, dictionaries.BOARD, dictionaries.player, key)

                # Check if quit
                if key == 'q':
                    level = 'QUIT'


        # BOARD 2
        if level == 'BOARD_2':
            view.print_table(players.data_to_print(dictionaries.player))
            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(1.0)
            util.clear_screen()

            while level == 'BOARD_2':

                # Set up board
                board = engine.create_board(dictionaries.BOARD[level])
                board = engine.put_player_on_board(board, dictionaries.player)
                board = engine.put_other_on_board(board, dictionaries.others)
                board = engine.put_item_on_board(board, dictionaries.items)

                # Display essential info
                ui.print_player_essential_atributes(dictionaries.player)
                
                # Display board
                ui.display_board(board)

                # Interaction whit items
                engine.item_vs_player(dictionaries.inventory, dictionaries.items, dictionaries.player)

                # Display inventory
                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(dictionaries.inventory)

                # Player input
                key = util.key_pressed()
                                
                # Movement
                engine.movement(board, dictionaries.player, key, dictionaries.others)

                # Clear screen
                util.clear_screen()

                # Interaction with other characters
                if engine.player_meets_other(dictionaries.others, dictionaries.player) != False:
                    other = engine.player_meets_other(dictionaries.others, dictionaries.player)
                    if other == 'other3':
                        print("Moooooo!")
                    elif other == 'other2':
                        print('Bon Appétit!')
                    else:
                        engine.player_vs_other_quiz(dictionaries.player, other, dictionaries.others, dictionaries.inventory, dictionaries.others[other]['questions'])

                # Gate and level change handling
                level = engine.player_enters_gate(level, dictionaries.BOARD, dictionaries.player, key)

                # Check if quit
                if key == 'q':
                    level = 'QUIT'


        # BOARD 3
        if level == 'BOARD_3':
            view.print_table(players.data_to_print(dictionaries.player))
            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(1.0)
            util.clear_screen()

            while level == 'BOARD_3':

                # Set up board
                board = engine.create_board(dictionaries.BOARD[level])
                board = engine.put_player_on_board(board, dictionaries.player)
                board = engine.put_other_on_board(board, dictionaries.others)
                board = engine.put_item_on_board(board, dictionaries.items)

                # Display essential info
                ui.print_player_essential_atributes(dictionaries.player)
                
                # Display board
                ui.display_board(board)

                # Interaction whit items
                engine.item_vs_player(dictionaries.inventory, dictionaries.items, dictionaries.player)

                # Display inventory
                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(dictionaries.inventory)

                # Player input
                key = util.key_pressed()
                                
                # Movement
                engine.movement(board, dictionaries.player, key, dictionaries.others)

                # Clear screen
                util.clear_screen()

                # Interaction with other characters
                if engine.player_meets_other(dictionaries.others, dictionaries.player) != False:
                    other = engine.player_meets_other(dictionaries.others, dictionaries.player)
                    if other == 'other3':
                        print("Moooooo!")
                    elif other == 'other2':
                        print('Bon Appétit!')
                    else:
                        engine.player_vs_other_quiz(dictionaries.player, other, dictionaries.others, dictionaries.others[other]['questions'])

                # Gate and level change handling
                level = engine.player_enters_gate(level, dictionaries.BOARD, dictionaries.player, key)

                # Check if quit
                if key == 'q' or dictionaries.player['player_life'] < 1:
                    level = 'QUIT'

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
