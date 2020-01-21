import random
import ui


def create_board(board):

    brick = board['BRICK']
    width = board['WIDTH']
    height = board['HEIGHT']

    new_board = []

    new_board.append(width * [brick])

    for a in range(height - 2):
        new_board.append([brick] + (width - 2) * [' '] + [brick])

    new_board.append(width * [brick])

    new_board[board['GATE_POSITION_Y']][board['GATE_POSITION_X']] = ' '

    return new_board


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
            if cell == other['other_icon']:
                board[x][y] = ' '
            y += 1
        x += 1

    height = other['position_y']
    width = other['position_x']
    if other["other_health"] > 0:
        board[height][width] = other['other_icon']

    return board


def get_random_position_of_other(other, width, height):
    """
    Randomly generates and updates position of Other Character
    based on the Character's step. Other Character respects the walls.

    Args:
        other: dictionary
        BOARD_HEIGHT and BOARD_WEIGHT: int

    """
    if other["other_health"] > 0:
        random_selection = random.randrange(4)
        if random_selection == 0:
            potential_position = other["position_x"] + other["step"]
            if potential_position >= width - 1:
                pass
            else:
                other["position_x"] += other["step"]
        if random_selection == 1:
            potential_position = other["position_x"] - other["step"]
            if potential_position <= 0:
                pass
            else:
                other["position_x"] -= other["step"]
        if random_selection == 2:
            potential_position = other["position_y"] + other["step"]
            if potential_position >= height - 1:
                pass
            else:
                other["position_y"] += other["step"]
        if random_selection == 3:
            potential_position = other["position_y"] - other["step"]
            if potential_position <= 0:
                pass
            else:
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


def put_item_on_board(board, item):

    for item_key in item:
        board[item[item_key]['position_y']][item[item_key]['position_x']] = item[item_key]['item_icon']

    return board


def player_meets_other(other, player):
    """
    Checks if Player meets the Other Character (is next to it, above or under)
    Args:
        other: dictionary
        player: dictionary
    Returns:
        if_meet: boolean
    """
    if_meet = False
    if other["other_health"] > 0:
        if other["position_y"] == player["position_y"] and (other["position_x"] == player["position_x"] + 1 or other["position_x"] == player["position_x"] - 1):
            if_meet = True
        elif other["position_x"] == player["position_x"] and (other["position_y"] == player["position_y"] + 1 or other["position_y"] == player["position_y"] - 1):
            if_meet = True
        elif other["position_y"] == player["position_y"] and other["position_x"] == player["position_x"]:
            if_meet = True

    return if_meet


def movement(board, player, key, other):

    height = len(board)
    width = len(board[0])

    if key == 'w':
        if player['position_y'] == 1:
            pass
        else:
            player['position_y'] -= 1
        get_random_position_of_other(other, width, height)

    elif key == 's':
        if player['position_y'] == len(board) - 2:
            pass
        else:
            player['position_y'] += 1
        get_random_position_of_other(other, width, height)
    elif key == 'a':
        if player['position_x'] == 1:
            pass
        else:
            player['position_x'] -= 1
        get_random_position_of_other(other, width, height)
    elif key == 'd':
        if player['position_x'] == len(board[0]) - 3:
            pass
        else:
            player['position_x'] += 1
        get_random_position_of_other(other, width, height)
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
                ui.print_message('\n' + ' +1 Life point! ')
            else:
                ui.print_message('\n' + 'This item has been added to your inventory!')
                

    if item_to_delete == '':
        pass

    elif item[item_to_delete]['number'] == 0:
        del item[item_to_delete]

def add_life_points(item, player):

    try:

        if item['first_aid']['position_x'] == player['position_x'] and item['first_aid']['position_y'] == player['position_y']:
            player['player_health'] += 1
        
    except KeyError:
        pass
def player_enters_gate(level, BOARD, player, key):

    # entering gate that is up in relation to player
    if player['position_x'] == BOARD[level]['GATE_POSITION_X'] and (player['position_y'] - 1) == BOARD[level]['GATE_POSITION_Y'] and key == 'w':
        return BOARD[level]['NEXT_LEVEL']

    # entering gate that is down in relation to player
    elif player['position_x'] == BOARD[level]['GATE_POSITION_X'] and (player['position_y'] + 1) == BOARD[level]['GATE_POSITION_Y'] and key == 's':
        return BOARD[level]['NEXT_LEVEL']

    # entering gate that is left in relation to player
    elif (player['position_x'] - 1) == BOARD[level]['GATE_POSITION_X'] and player['position_y'] == BOARD[level]['GATE_POSITION_Y'] and key == 'a':
        return BOARD[level]['NEXT_LEVEL']

    # entering gate that is left in relation to player
    elif (player['position_x'] + 1) == BOARD[level]['GATE_POSITION_X'] and player['position_y'] == BOARD[level]['GATE_POSITION_Y'] and key == 'a':
        return BOARD[level]['NEXT_LEVEL']

    else:
        return level




        


def player_vs_other_quiz(player, other, item, questions, questions_number=2):
    """
    Player fights agains the Other Character answering questions.
    When Player replies correctly, the Other Character loses health points.
    Otherwise Player loses health points.
    Player lost all health - game over. The Other Character losing
    health - it disappears and the Player gets flour.
    """

    print("Play the quiz to get %s from the %s" % (other["goal_quiz"], other["other_name"]))
    q_count = 0
    questions = [question for question in questions if question[2] is False]
    while q_count <= questions_number and other["other_health"] > 0:
        answer = input(questions[q_count][0])
        if answer == questions[q_count][1]:
            player["player_health"] += 1
            other["other_health"] -= 1
            questions[q_count][2] = True
            print("Correct!")
        else:
            player["player_health"] -= 1
            print("Wrong!")
        q_count += 1

    if other["other_health"] > 0:
        print("To get %s you have to come back and reply correctly to the questions!" % other["goal_quiz"])
    else:
        #  here flour(goal) needs to be added to inventory
        print("Wonderful! The %s gave you %s." % (other["other_name"], other["goal_quiz"]))
