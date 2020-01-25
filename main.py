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
from PIL import Image
from pygame import mixer
import data_manager



def main():
    MUSIC_FILE = "Cookie Monster Sings C is for Cookie.wav"
    mixer.init()
    mixer.music.load(MUSIC_FILE)
    mixer.music.play()
    view.print_images(data_manager.read_file_nicknames('ascii-art.txt'))
    view.start_descriptions()    
    # initial level
    level = 'BOARD_1'   

    # initial key`
    key = ''

    menu_start.run()
        
    ui.print_message('\n\n\n LEVEL %s \n\n\n' % (level[-1]))
    time.sleep(1.0)
    util.clear_screen()

    while level != 'WIN' and level != 'QUIT' and level != 'LOSE':

        view.print_table(players.data_to_print(dictionaries.player))

        # Set up board
        board = engine.create_board(dictionaries.BOARD[level])
        board = engine.put_player_on_board(board, dictionaries.player)
        board = engine.put_other_on_board(board, dictionaries.others)
        board = engine.put_item_on_board(board, dictionaries.items, level) 

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
        engine.movement(board,dictionaries.player, key, dictionaries.others)

        # Clear screen
        util.clear_screen()

        # Interaction with other characters
        if engine.player_meets_other(dictionaries.others, dictionaries.player) != False:
            other = engine.player_meets_other(dictionaries.others, dictionaries.player)
            if dictionaries.others[other]['other_type'] == 'enemy':
                engine.fight(dictionaries.player, dictionaries.others, other, dictionaries.inventory, dictionaries.items)
            elif dictionaries.others[other]['other_type'] == 'quiz':
                engine.player_vs_other_quiz(dictionaries.player, other, dictionaries.others, dictionaries.inventory, dictionaries.others[other]['questions'])

        # Gate and level change handling
        if engine.player_enters_gate(level, dictionaries.BOARD, dictionaries.player, key) != level:
            util.clear_screen()
            level = engine.player_enters_gate(level, dictionaries.BOARD, dictionaries.player, key)
            if level == 'WIN':
                pass
            else:
                ui.print_message('\n\n\n LEVEL %s \n\n\n' % (level[-1]))
                time.sleep(1.0)
                util.clear_screen()

        # Check if quit
        if key == 'q':
            quit_assertion = ''
            while quit_assertion != 'y' and quit_assertion != 'n':
                util.clear_screen()
                print('Are you sure you want to quit? ( Y / N )')
                quit_assertion = util.key_pressed()
                if quit_assertion == 'y':
                    level = 'QUIT'
                elif quit_assertion == 'n':
                    pass
                else:
                    pass

        
        elif dictionaries.player['player_life'] == 0:
            level = 'LOSE'


    if level == 'WIN':
        util.clear_screen()
        ui.display_board(board)
        print(text2art("VICTORY!", font='block', chr_ignore=True))

    elif level == 'LOSE':
        util.clear_screen()
        ui.display_board(board)
        print(text2art("GAME OVER!", font='block', chr_ignore=True))
        time.sleep(10.7)
    
    print('\n\n\n Goodbye, see you soon!')
    time.sleep(1.0)

    with Image.open("cookiemonster.jpg") as img:
        img.show()


if __name__ == '__main__':
    main()
