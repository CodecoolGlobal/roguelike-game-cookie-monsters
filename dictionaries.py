# PLAYER -------------------------

player = {
    'player_icon': '@',
    'position_x': 10,
    'position_y': 10,
    'player_life': 3,
    'player_power': 1
    }

# BOARD -------------------------

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


# ITEMS -------------------------

items = {
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


# OTHER CHARACTERS --------------

others = {
    'other': {
        'other_type': "enemy",
        'other_name': "Miller",
        'other_icon': "M",
        'position_x': 5,
        'position_y': 5,
        'step': 1,
        'other_health': 3,
        'goal_quiz': "flour",
        'questions':   [["What's the first name of 'Ooops I did it again' singer?\n(a) Christina\n(b) Britney\n(c) Jessica\n", "b", False],
                        ["Which river passes through Vienna?\n(a) Vistula\n(b) Douro\n(c) Danube\n", "c", False],
                        ["What color are bananas?\n(a) Red\n(b) Orange\n(c) Yellow\n", "c", False],
                        ["What band Nergal plays in?\n(a) Behemoth\n(b) Acid Drinkers\n(c) Coma\n", "a", False],
                        ["What is the capital of Australia?\n(a) Sydney\n(b) Canberra\n(c) Melbourne\n", "b", False], 
                        ["How many islands there are in Faroe Islands?\n(a) 412\n(b) 779\n(c) 18\n", "b", False]]
        },
    'other2': {
        'other_type': "friend",
        'other_name': "Cook",
        'other_icon': "C",
        'position_x': 20,
        'position_y': 25,
        'step': 0,
        'other_health': 3,
        'goal_quiz': "information",
        'questions': []
        },
    'other3': {
        'other_type': "enemy",
        'other_name': "Cow",
        'other_icon': "K",
        'position_x': 33,
        'position_y': 15,
        'step': 2,
        'other_health': 3,
        'goal_quiz': "milk",
        'questions': []
        }
    }   


# INVENTORY ---------------------

inventory = {}

