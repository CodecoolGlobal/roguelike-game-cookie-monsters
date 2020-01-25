import random
import ui
import main
import dictionaries
import math
import util
import view
import players


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


def put_other_on_board(board, others):
    '''
    Modifies the game board by placing the other character icon at its coordinates.
    Args:
    list: The game board
    dictionary: The other character information containing the icon and coordinates
    Returns:
    Nothing
    '''
    
    for other in others:
        x = 0
        for row in board:
            y = 0
            for cell in row:
                if cell == others[other]['other_icon']:
                    board[x][y] = ' '
                y += 1
            x += 1

    for other in others:
        height = others[other]['position_y']
        width = others[other]['position_x']

        for row in range(height - (math.floor(others[other]["width"] / 2)), height + (math.ceil(others[other]["width"] / 2))):
            for cell in range(width - (math.floor(others[other]["width"] / 2)), width + (math.ceil(others[other]["width"] / 2))):
                board[row][cell] = others[other]['other_icon']

    return board


def get_random_position_of_other(others, width, height):
    """
    Randomly generates and updates position of Other Character
    based on the Character's step. Other Character respects the walls.

    Args:
        other: dictionary
        BOARD_HEIGHT and BOARD_WEIGHT: int

    """
    for other in others:

        if others[other]["other_health"] > 0:
            random_selection = random.randrange(4)
            if random_selection == 0:
                potential_position = others[other]["position_x"] + others[other]["step"]
                if potential_position >= width - 1:
                    pass
                else:
                    others[other]["position_x"] += others[other]["step"]
            if random_selection == 1:
                potential_position = others[other]["position_x"] - others[other]["step"]
                if potential_position <= 0:
                    pass
                else:
                    others[other]["position_x"] -= others[other]["step"]
            if random_selection == 2:
                potential_position = others[other]["position_y"] + others[other]["step"]
                if potential_position >= height - 1:
                    pass
                else:
                    others[other]["position_y"] += others[other]["step"]
            if random_selection == 3:
                potential_position = others[other]["position_y"] - others[other]["step"]
                if potential_position <= 0:
                    pass
                else:
                    others[other]["position_y"] -= others[other]["step"]


def add_to_inventory(inventory, item_key):
    """Add to the inventory dictionary a list of items"""

    item_key = item_key[:-1]

    if item_key == 'first_ai':
        pass

    elif item_key in inventory:
        inventory[item_key] += 1
    else:
        inventory[item_key] = 1


def put_item_on_board(board, items, level):

    for item_key in items:
        if items[item_key]['board'] == int(level[-1]):
            board[items[item_key]['position_y']][items[item_key]['position_x']] = items[item_key]['item_icon']

    return board


def player_meets_other(others, player):
    """
    Checks if Player meets the Other Character (is next to it, above or under)
    Args:
        other: dictionary
        player: dictionary
    Returns:
        if_meet: boolean
    """
    if_meet = False

    for other in others:
        if others[other]["other_health"] > 0:
            if others[other]["position_y"] == player["position_y"] and (others[other]["position_x"] == player["position_x"] + 1 or others[other]["position_x"] == player["position_x"] - 1):
                return other
            elif others[other]["position_x"] == player["position_x"] and (others[other]["position_y"] == player["position_y"] + 1 or others[other]["position_y"] == player["position_y"] - 1):
                return other
            elif others[other]["position_y"] == player["position_y"] and others[other]["position_x"] == player["position_x"]:
                return other

    return if_meet
            
def movement(board, player, key, others):

    height = len(board)
    width = len(board[0])
    if key in ['w', 's', 'a', 'd']:
        get_random_position_of_other(others, width, height)

    if key == 'w':
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


def item_vs_player(inventory, item, player):

    item_to_delete = ''

    for item_key in item:
        if item[item_key]['position_x'] == player['position_x'] and item[item_key]['position_y'] == player['position_y']:

            add_to_inventory(inventory, item_key)
            item_to_delete = item_key
            item[item_key]['number'] -= 1
            

            if item_key == 'first_aid':
                ui.print_message('\n' + ' +1 Life point! ')
                player['player_life'] += 1 
            else:
                ui.print_message('\n' + 'This item has been added to your inventory!')
                

    if item_to_delete == '':
        pass

    elif item[item_to_delete]['number'] == 0:
        del item[item_to_delete]

def add_life_points(item, player):

    try:

        if item['first_aid']['position_x'] == player['position_x'] and item['first_aid']['position_y'] == player['position_y']:
            player['player_life'] += 1
        
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


 


def player_vs_other_quiz(player, other, others, inventory, questions, questions_number=2):
    """
    Player fights agains the Other Character answering questions.
    When Player replies correctly, the Other Character loses health points.
    Otherwise Player loses health points.
    Player lost all health - game over. The Other Character losing
    health - it disappears and the Player gets flour.
    """

    ui.print_message(("Play the quiz to get %s from the %s" % (others[other]["goal_quiz"], others[other]["other_name"])))

    q_count = 0

    questions = [question for question in questions if question[2] is False]

    while q_count <= questions_number and others[other]["other_health"] > 0:
        answer = input(questions[q_count][0])
        if answer == questions[q_count][1]:
            # player['player_power'] += 1  moze +1 power za kazda dobra odpowiedz?
            others[other]["other_health"] -= 1
            questions[q_count][2] = True
            ui.print_message("Correct!")
        else:
            # player['player_power'] -= 1  moze -1 power za kazda bledna odpowiedz?
            ui.print_message("Wrong!")
        q_count += 1

    if others[other]["other_health"] > 0:
        player["player_life"] -= 1
        ui.print_message("To get %s you have to come back and reply correctly to the questions!" % others[other]["goal_quiz"])
    else:
        player["player_life"] += 1
        add_to_inventory(inventory, "flour0")
        ui.print_message("Wonderful! The %s gave you %s." % (others[other]["other_name"], others[other]["goal_quiz"]))
        ui.print_message('+1 life point!')




def fight(player, others, other, inventory, items):
    
    player_x = player['position_x']
    player_y = player['position_y']
    other_x = others[other]['position_x']
    other_y = others[other]['position_y']

    items_sumaric_power = 0
    if player_x == other_x and player_y == other_y:
        for item in inventory:
            items_sumaric_power += items[item]['added_power']
        
    player_hit = (player['player_power'] + items_sumaric_power) * random.randrange(2)
    other_hit = others[other]['other_power'] #* random.randrange(2)

    if player_hit > other_hit:
        ui.print_message('You just won the fight with %s! +1 to power for you!' %(others[other]['other_name']))
        player['player_power'] += 1
        others[other]['other_health'] -= 1

    elif player_hit == other_hit:
        ui.print_message('You just fought with %s! It was a draw' %(others[other]['other_name']))
    
    else:
        ui.print_message('You just lost fight with %s! You loose one life point' %(others[other]['other_name']))
        player['player_life'] -= 1