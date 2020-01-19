import random
import ui


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


def put_other_on_board(board, other):
    '''
    Modifies the game board by placing the other character icon at its coordinates.

    Args:
    list: The game board
    dictionary: The other character information containing the icon and coordinates

    Returns:
    Nothing
    '''

    x = 0
    for row in board:
        y = 0
        for cell in row:
            if cell == other["other_icon"]:
                board[x][y] = ' '
            y += 1
        x += 1

    x_index = other["position_x"]
    y_index = other["position_y"]
    board[x_index][y_index] = other["other_icon"]

    return board


def get_random_position_of_other(other):
    """
    Randomly generates and updates position of Other Character
    based on the Character's step.

    Args:
        other: dictionary

    """
    random_selection = random.randrange(4)
    if random_selection == 0:
        other["position_x"] += other["step"]
    elif random_selection == 1:
        other["position_x"] -= other["step"]
    elif random_selection == 2:
        other["position_y"] += other["step"]
    elif random_selection == 3:
        other["position_y"] -= other["step"]


def add_to_inventory(inventory, item_key):
    """Add to the inventory dictionary a list of items"""

    item_key = item_key[:-1]

    if item_key == 'first_ai':
        pass

    elif item_key in inventory:
        inventory[item_key] += 1
    else:
        inventory[item_key] = 1


def put_item_on_board(board, item, item_key):

    board[item[item_key]['position_y']][item[item_key]['position_x']] = item[item_key]['item_icon'] 

    return board



def movement(board, player, key, other):
    
        
    if key == 'w':
        if player['position_y'] == 1:
            pass
        else:
            player['position_y'] -= 1
        get_random_position_of_other(other)

    elif key == 's':
        if player['position_y'] == len(board) - 2:
            pass
        else:
            player['position_y'] += 1
        get_random_position_of_other(other)
    elif key == 'a':
        if player['position_x'] == 1:
            pass
        else:
            player['position_x'] -= 1
        get_random_position_of_other(other)
    elif key == 'd':
        if player['position_x'] == len(board[0]) - 3:
            pass
        else:
            player['position_x'] += 1
        get_random_position_of_other(other)
    else:
        pass

def item_vs_player(inventory, item, player):

    item_to_delete = ''

    for item_key in item:
        if item[item_key]['position_x'] == player['position_x'] and item[item_key]['position_y'] == player['position_y']:
            add_to_inventory(inventory, item_key)
            item_to_delete = item_key
            item[item_key]['number'] -= 1

            if item_key == 'first_aid':
                ui.print_message(' +1 Life point! ')
            else:
                ui.print_message('This item has been added to your inventory!')
                

    if item_to_delete == '':
        pass

    elif item[item_to_delete]['number'] == 0:
        del item[item_to_delete]

def add_life_points(item, player):

    try:

        if item['first_aid']['position_x'] == player['position_x'] and item['first_aid']['position_y'] == player['position_y']:
            player['life_points'] += 1
        
    except KeyError:
        pass