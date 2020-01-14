import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 6
PLAYER_START_Y = 10

BOARD_WIDTH = 100
BOARD_HEIGHT = 30

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
def players():

def main():

    #player = create_player()
    player = {'player_icon': PLAYER_ICON, 'position_x': PLAYER_START_X, 'position_y': PLAYER_START_Y}

    empty_board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
   


    is_running = True

    while is_running:

        board = engine.put_player_on_board(empty_board, player)

        ui.display_board(board)

        key = util.key_pressed()

        if key == 'q':
            is_running = False   

        elif key == 'w':
            if player['position_y'] == 2:
                pass
            else:
                player['position_y'] -= 1

        elif key == 's':
            if player['position_y'] == len(board) - 1:
                pass
            else:
                player['position_y'] += 1

        elif key == 'a':
            if player['position_x'] == 2:
                pass
            else:
                player['position_x'] -= 1

        elif key == 'd':
            if player['position_x'] == len(board[0]) - 2:
                pass
            else:
                player['position_x'] += 1

        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
