import util
import engine
import ui

BOARD_WIDTH = 100
BOARD_HEIGHT = 30

PLAYER_ICON = '@'
PLAYER_START_X = 1
PLAYER_START_Y = 2
PLAYER_HEALTH = 5

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
OTHER_START_Y = 20

OTHER_STEP = 1


def create_player():
    pass


def create_other():
    other = {
        'other_name': OTHER_NAME,
        'other_icon': OTHER_ICON,
        'position_x': OTHER_START_X,
        'position_y': OTHER_START_Y,
        'step': OTHER_STEP,
        'other_health': OTHER_HEALTH
        }
    return other


def main():
    inventory = {}
    # player = create_player()

    player = {
        'player_icon': PLAYER_ICON,
        'position_x': PLAYER_START_X,
        'position_y': PLAYER_START_Y,
        'player_health': PLAYER_HEALTH
        }
    item = {
        'flour0': {
            'type': 'ingridient',
            'item_icon': 'F',
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
            'item_icon': 'S',
            'position_x': 90,
            'position_y': 2,
            'number': 2
            }
         }


    empty_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    other = create_other()

    is_running = True

    while is_running:

        board = engine.put_player_on_board(empty_board, player)
        
        if other["other_health"] > 0:
            board = engine.put_other_on_board(board, other)

        for item_key in item:
            board = engine.put_item_on_board(board, item, item_key)

        ui.display_board(board)

        key = util.key_pressed()

        engine.movement(board, player, key, other, BOARD_WIDTH, BOARD_HEIGHT)

        util.clear_screen()

        if engine.player_meets_other(other, player):
            engine.player_vs_other_quiz(player, other, item, questions_number=2)

        engine.item_vs_player(inventory, item, player)

        if key == 'i':
            message = 'This is your inventory content: '
            ui.print_message(message)
            ui.print_table(inventory)

        elif key == 'q':
            is_running = False


if __name__ == '__main__':
    main()
