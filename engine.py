def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''

    board = []

    board.append([''] + width * ['-'])

    for a in range(height - 2):
        board.append(['|'] + (width - 2) * [' '] + ['|'])

    board.append([''] + width * ['-'])

    return board


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    x = 0 
    for row in board:
        y = 0
        for cell in row:
            if cell == player['player_icon']:
                board[x][y] = ' '

            y += 1
        x += 1

    height = player['position_y']
    width = player['position_x']

    board[height][width] = player['player_icon']

    return board

def add_to_inventory(inventory, item_key):
    """Add to the inventory dictionary a list of items"""

    if item_key in inventory:
        inventory[item_key] += 1
    else:
        inventory[item_key] = 1

def put_item_on_board(board, item, item_key):

    board[item[item_key]['position_y']][item[item_key]['position_x']] = item[item_key]['item_icon'] 

    return board