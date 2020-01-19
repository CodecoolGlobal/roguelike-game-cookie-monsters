import util
import engine
import ui
import time

PLAYER_ICON = '@'
PLAYER_START_X = 1
PLAYER_START_Y = 2

OTHER_NAME = "Miller"
OTHER2_NAME = "Cook"
OTHER3_NAME = "Cow"

OTHER_ICON = "M"
OTHER2_ICON = "C"
OTHER3_ICON = "K"

OTHER_HEALTH = 3
OTHER2_HEALTH = 3
OTHER3_HEALTH = 3

OTHER_START_X = 5
OTHER_START_Y = 5

OTHER_STEP = 1

BOARD = {
    'BOARD_1':{
        'BRICK': '#',
        'COLOR': 'green',
        'WIDTH': 100,
        'HEIGHT': 30,
        'GATE_POSITION_X': 5,
        'GATE_POSITION_Y': 0,
        'NEXT_LEVEL': 'BOARD_2'
        },
    'BOARD_2':{
        'BRICK': '%',
        'COLOR': 'yellow',
        'WIDTH': 100,
        'HEIGHT': 30,
        'GATE_POSITION_X': 0,
        'GATE_POSITION_Y': 10,
        'NEXT_LEVEL': 'BOARD_3'
        },
    'BOARD_3':{
        'BRICK': 'X',
        'COLOR': 'yellow',
        'WIDTH': 100,
        'HEIGHT': 30,
        'GATE_POSITION_X': 60,
        'GATE_POSITION_Y': 0,
        'NEXT_LEVEL': 'WIN'
        }
    }


def create_player():
    pass


def create_other():
    other = {
        'other_name': OTHER_NAME,
        'other_icon': OTHER_ICON,
        'position_x': OTHER_START_X,
        'position_y': OTHER_START_Y,
        'step': OTHER_STEP}
    return other


def main():
    inventory = {}
    # player = create_player()

    player = {'player_icon': PLAYER_ICON, 'position_x': PLAYER_START_X, 'position_y': PLAYER_START_Y}
    item = {
        'flour0': {
            'type': 'ingridient',
            'item_icon': 'S',
            'position_x': 11,
            'position_y': 2,
            'number': 2
            },
        'sugar0': {
            'type': 'ingridient',
            'item_icon': 'S',
            'position_x': 9,
            'position_y': 18,
            'number': 1
            },
        'sugar2': {
            'type': 'ingridient',
            'item_icon': 'S',
            'position_x': 55,
            'position_y': 25,
            'number': 1
            },
        'sugar3': {
            'type': 'ingridient',
            'item_icon': 'F',
            'position_x': 90,
            'position_y': 2,
            'number': 2
            }
         }

    # initial board
    board = engine.create_board(BOARD['BOARD_1'])

    other = create_other()

    # initial level
    level = 'BOARD_1'

    is_running = True

    while is_running:

        if level == 'BOARD_1':

            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(2.0)

            while level == 'BOARD_1':

                board = engine.create_board(BOARD[level])

                board = engine.put_player_on_board(board, player)
                board = engine.put_other_on_board(board, other)

                for item_key in item:
                    board = engine.put_item_on_board(board, item, item_key)

                ui.display_board(board)

                key = util.key_pressed()
                
                level = engine.player_enters_gate(level, BOARD, player, key)

                engine.movement(board, player, key, other)

                if engine.player_meets_other(other, player):
                    ui.print_message("Now you will fight!")

                engine.item_vs_player(inventory, item, player)

                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(inventory)

                util.clear_screen()


            
            #level = engine.player_enters_gate(BOARD, player, key)
    
        elif level == 'BOARD_2':

            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(2.0)

            while level == 'BOARD_2':

                board = engine.create_board(BOARD[level])

                board = engine.put_player_on_board(board, player)
                board = engine.put_other_on_board(board, other)

                for item_key in item:
                    board = engine.put_item_on_board(board, item, item_key)

                ui.display_board(board)

                key = util.key_pressed()
                
                level = engine.player_enters_gate(level, BOARD, player, key)

                engine.movement(board, player, key, other)

                if engine.player_meets_other(other, player):
                    ui.print_message("Now you will fight!")

                engine.item_vs_player(inventory, item, player)

                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(inventory)

                util.clear_screen()

        elif level == 'BOARD_3':

            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(2.0)
            
            while level == 'BOARD_3':
                
                board = engine.create_board(BOARD[level])

                board = engine.put_player_on_board(board, player)
                board = engine.put_other_on_board(board, other)

                for item_key in item:
                    board = engine.put_item_on_board(board, item, item_key)

                ui.display_board(board)

                key = util.key_pressed()
                
                level = engine.player_enters_gate(level, BOARD, player, key)

                engine.movement(board, player, key, other)

                if engine.player_meets_other(other, player):
                    ui.print_message("Now you will fight!")
                engine.item_vs_player(inventory, item, player)

                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(inventory)

                util.clear_screen()
        
        elif level == 'WIN':

            while True:
                print('YOU WON!!!')
                time.sleep(0.7)
                print('🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪')
                time.sleep(0.7)

        elif key == 'q':
            is_running = False


if __name__ == '__main__':
    main()
