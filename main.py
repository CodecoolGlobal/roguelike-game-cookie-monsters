import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 6
PLAYER_START_Y = 10

BOARD_WIDTH = 30
BOARD_HEIGHT = 30

def create_player():
    pass


def main():
    inventory = {}

    #player = create_player()
    player = {'player_icon': PLAYER_ICON, 'position_x': PLAYER_START_X, 'position_y': PLAYER_START_Y}
    item = {
    'flour':{ 
        'type': 'ingridient', 
        'item_icon': 'F',
        'position_x': 11,
        'position_y': 2
        },
    'sugar':{ 
        'type': 'ingridient', 
        'item_icon': 'S',
        'position_x': 9,
        'position_y': 18
        }
    }

    empty_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
   


    is_running = True

    while is_running:

        board = engine.put_player_on_board(empty_board, player)

        for item_key in item:
            board = engine.put_item_on_board(board, item, item_key)

        ui.display_board(board) 

        key = util.key_pressed()

        if key == 'q':
            is_running = False   

        elif key == 'w':
            if player['position_y'] == 1:
                pass
            else:
                player['position_y'] -= 1

        elif key == 's':
            if player['position_y'] == len(board) - 2:
                pass
            else:
                player['position_y'] += 1

        elif key == 'a':
            if player['position_x'] == 1:
                pass
            else:
                player['position_x'] -= 1

        elif key == 'd':
            if player['position_x'] == len(board[0]) - 3:
                pass
            else:
                player['position_x'] += 1
        else:
            pass

        for item_key in item:
            if item[item_key]['position_x'] == player['position_x'] and item[item_key]['position_y'] == player['position_y']:
                engine.add_to_inventory(inventory, item_key)
                
        util.clear_screen()
        print(inventory)


        

if __name__ == '__main__':
    main()
