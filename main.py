import util
import engine
import ui
import time

BOARD_WIDTH = 100
BOARD_HEIGHT = 30

PLAYER_ICON = '@'
PLAYER_START_X = 1
PLAYER_START_Y = 2
PLAYER_HEALTH = 5

question_prompts = [
    "What's the first name of 'Ooops I did it again' singer?\n(a) Christina\n(b) Britney\n(c) Jessica\n",
    "Which river passes through Vienna?\n(a) Vistula\n(b) Douro\n(c) Danube\n",
    "What color are bananas?\n(a) Red\n(b) Orange\n(c) Yellow\n",
    "What band Nergal plays in?\n(a) Behemoth\n(b) Acid Drinkers\n(c) Coma\n",
    "What is the capital of Australia?\n(a) Sydney\n(b) Canberra\n(c) Melbourne\n",
    "How many islands there are in Faroe Islands?\n(a) 412\n(b) 779\n(c) 18\n"
    ]

questions = [
    [question_prompts[0], "b", False],
    [question_prompts[1], "c", False],
    [question_prompts[2], "c", False],
    [question_prompts[3], "a", False],
    [question_prompts[4], "b", False],
    [question_prompts[5], "b", False],
]

BOARD = {
    'BOARD_1': {
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

other = {
    'other_type': "enemy",
    'other_name': "Miller",
    'other_icon': "M",
    'position_x': 5,
    'position_y': 5,
    'step': 1,
    'other_health': 3,
    'goal_quiz': "flour"
    }

other2: {
    'other_type': "friend",
    'other_name': "Cook",
    'other_icon': "C",
    'position_x': 20,
    'position_y': 30,
    'step': 0,
    'other_health': 3,
    'goal_quiz': "information"
    }

other3: {
    'other_type': "enemy",
    'other_name': "Cow",
    'other_icon': "K",
    'position_x': 33,
    'position_y': 15,
    'step': 2,
    'other_health': 3,
    'goal_quiz': "milk"
    }


def create_player():
    pass


def create_other():
    pass


def main():
    inventory = {}
    # player = create_player()

    item = {
        'eggs0':{
            'type': 'ingridient',
            'item_icon': 'E',
            'position_x': 11,
            'position_y': 2,
            'number': 2
            },
        'sugar0':{ 
            'type': 'ingridient', 
            'item_icon': 'S',
            'position_x': 9,
            'position_y': 18,
            'number': 1
            },
        'sugar2':{ 
            'type': 'ingridient', 
            'item_icon': 'S',
            'position_x': 55,
            'position_y': 25,
            'number': 1
            },
        'sugar3':{ 
            'type': 'ingridient', 
            'item_icon': 'S',
            'position_x': 90,
            'position_y': 2,
            'number': 2
            },
        'first_aid':{ 
            'type': 'life', 
            'item_icon': 'A',
            'position_x': 70,
            'position_y': 15,
            'number': 1
        }
    }
    player = {
        'player_icon': PLAYER_ICON,
        'position_x': PLAYER_START_X,
        'position_y': PLAYER_START_Y,
        'player_health': 3,
        'player_power': 1
        }


    # initial board
    board = engine.create_board(BOARD['BOARD_1'])

    # initial level
    level = 'BOARD_1'

    # initial key
    key = ''


    while level != 'WIN' and level != 'QUIT':


        # BOARD 1
        if level == 'BOARD_1':

            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(1.0)
            util.clear_screen()

            while level == 'BOARD_1':

                board = engine.create_board(BOARD[level])
                board = engine.put_player_on_board(board, player)
                board = engine.put_other_on_board(board, other)
                board = engine.put_item_on_board(board, item)

                # Display essential info
                ui.print_player_essential_atributes(player)
                
                # Display board
                ui.display_board(board)

                # Interaction whit items
                engine.item_vs_player(inventory, item, player)

                # Display inventory
                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(inventory)

                # Player input
                key = util.key_pressed()
                
                # Movement
                engine.movement(board, player, key, other)

                # Interaction with other characters
                if engine.player_meets_other(other, player):
                    engine.player_vs_other_quiz(player, other, item, questions)

                # Gate and level change handling
                level = engine.player_enters_gate(level, BOARD, player, key)

                # Check if quit
                if key == 'q':
                    level = 'QUIT'

                # Clear screen
            util.clear_screen()




        # BOARD 2
        if level == 'BOARD_2':

            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(1.0)
            util.clear_screen()

            while level == 'BOARD_2':

                # Set up board
                board = engine.create_board(BOARD[level])
                board = engine.put_player_on_board(board, player)
                board = engine.put_other_on_board(board, other)
                board = engine.put_item_on_board(board, item)

                # Display essential info
                ui.print_player_essential_atributes(player)
                
                # Display board
                ui.display_board(board)

                # Interaction whit items
                engine.item_vs_player(inventory, item, player)

                # Display inventory
                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(inventory)

                # Player input
                key = util.key_pressed()
                
                # Movement
                engine.movement(board, player, key, other)

                # Interaction with other characters
                if engine.player_meets_other(other, player):
                    engine.player_vs_other_quiz(player, other, item, questions)

                # Gate and level change handling
                level = engine.player_enters_gate(level, BOARD, player, key)

                # Check if quit
                if key == 'q':
                    level = 'QUIT'

                # Clear screen
                util.clear_screen()


        # BOARD 3
        if level == 'BOARD_3':

            print(3 * '\n' + "LEVEL ", level[-1], 3 * '\n')
            time.sleep(1.0)
            util.clear_screen()

            while level == 'BOARD_3':

                # Set up board
                board = engine.create_board(BOARD[level])
                board = engine.put_player_on_board(board, player)
                board = engine.put_other_on_board(board, other)
                board = engine.put_item_on_board(board, item)

                # Display essential info
                ui.print_player_essential_atributes(player)
                
                # Display board
                ui.display_board(board)

                # Interaction whit items
                engine.item_vs_player(inventory, item, player)

                # Display inventory
                if key == 'i':
                    message = 'This is your inventory content: '
                    ui.print_message(message)
                    ui.print_table(inventory)

                # Player input
                key = util.key_pressed()
                
                # Movement
                engine.movement(board, player, key, other)

                # Interaction with other characters
                if engine.player_meets_other(other, player):
                    engine.player_vs_other_quiz(player, other, item, questions)

                # Gate and level change handling
                level = engine.player_enters_gate(level, BOARD, player, key)

                # Check if quit
                if key == 'q':
                    level = 'QUIT'

                # Clear screen
                util.clear_screen()


    if level == 'WIN':

        while True:
            print('YOU WON!!!')
            time.sleep(0.7)
            print('🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪')
            time.sleep(0.7)




    


if __name__ == '__main__':
    main()
