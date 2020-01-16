import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 6
PLAYER_START_Y = 10

OTHER_ICON = "M"
OTHER2_ICON = "K"
OTHER3_ICON = "C"

OTHER_START_X = 20
OTHER_START_Y = 30

OTHER_STEP = 1

BOARD_WIDTH = 100
BOARD_HEIGHT = 30


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''


def main():

    # player = create_player()
    # other = create_other()

    player = {'player_icon': PLAYER_ICON, 'position_x': PLAYER_START_X, 'position_y': PLAYER_START_Y}
    other = {'other_icon': OTHER_ICON, 'position_x': OTHER_START_X, 'position_y': OTHER_START_Y, 'step': OTHER_STEP}
    empty_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    is_running = True

    while is_running:

        board = engine.put_player_on_board(empty_board, player)
        board = engine.put_other_on_board(board, other)

        ui.display_board(board)

        key = util.key_pressed()

        if key == 'q':
            is_running = False

        elif key == 'w':
            if player['position_y'] == 2:
                pass
            else:
                player['position_y'] -= 1
            engine.get_random_position_of_other(other)

        elif key == 's':
            if player['position_y'] == len(board) - 1:
                pass
            else:
                player['position_y'] += 1
            engine.get_random_position_of_other(other)
        elif key == 'a':
            if player['position_x'] == 2:
                pass
            else:
                player['position_x'] -= 1
            engine.get_random_position_of_other(other)
        elif key == 'd':
            if player['position_x'] == len(board[0]) - 2:
                pass
            else:
                player['position_x'] += 1
            engine.get_random_position_of_other(other)
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
