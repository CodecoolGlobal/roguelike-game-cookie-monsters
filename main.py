import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 6
PLAYER_START_Y = 10

OTHER_NAME = "Miller"
OTHER2_NAME = "Cook"
OTHER3_NAME = "Cow"

OTHER_ICON = "M"
OTHER2_ICON = "C"
OTHER3_ICON = "K"

OTHER_HEALTH = 3
OTHER2_HEALTH = 3
OTHER3_HEALTH = 3

OTHER_START_X = 20
OTHER_START_Y = 30

OTHER_STEP = 2

BOARD_WIDTH = 100
BOARD_HEIGHT = 30


def create_player():
    pass


def create_other():
    other = {'other_name': OTHER_NAME,
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
    'flour':{ 
        'type': 'ingridient', 
        'item_icon': 'F',
        'position_x': 11,
        'position_y': 2,
        'number': 2
        },
    'sugar':{ 
        'type': 'ingridient', 
        'item_icon': 'S',
        'position_x': 9,
        'position_y': 18,
        'number': 6
        }
    }
    empty_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    other = create_other()
    is_running = True

    while is_running:

        board = engine.put_player_on_board(empty_board, player)
        board = engine.put_other_on_board(board, other)

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
            engine.get_random_position_of_other(other)

        elif key == 's':
            if player['position_y'] == len(board) - 2:
                pass
            else:
                player['position_y'] += 1
            engine.get_random_position_of_other(other)
        elif key == 'a':
            if player['position_x'] == 1:
                pass
            else:
                player['position_x'] -= 1
            engine.get_random_position_of_other(other)
        elif key == 'd':
            if player['position_x'] == len(board[0]) - 3:
                pass
            else:
                player['position_x'] += 1
            engine.get_random_position_of_other(other)
        else:
            pass

        item_to_delete = ''

        for item_key in item:
            if item[item_key]['position_x'] == player['position_x'] and item[item_key]['position_y'] == player['position_y']:
                engine.add_to_inventory(inventory, item_key)
                item_to_delete = item_key
                item[item_key]['number'] -= 1 

        if item_to_delete == '':
            pass
        elif item[item_to_delete]['number'] == 0:
            del item[item_to_delete]

        util.clear_screen()
        print(inventory)


if __name__ == '__main__':
    main()
