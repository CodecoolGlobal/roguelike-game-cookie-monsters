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
        'Chocolate':{
            'type': 'ingridient',
            'item_icon': 'C',
            'position_x': 5,
            'position_y': 20,
            'number': 1,
            'board': 3,
            'added_power': 0            
            },
        'Jelly':{ 
            'type': 'ingridient', 
            'item_icon': 'J',
            'position_x': 12,
            'position_y': 18,
            'number': 1,
            'board': 3,
            'added_power': 0
            },
        'Pudding':{ 
            'type': 'ingridient', 
            'item_icon': 'P',
            'position_x': 55,
            'position_y': 25,
            'number': 1,
            'board': 3,
            'added_power': 0
            },
        'Ice Cream':{ 
            'type': 'ingridient', 
            'item_icon': 'I',
            'position_x': 92,
            'position_y': 7,
            'number': 2,
            'board': 2,
            'added_power': 0
            },
        'Jam0':{
            'type': 'ingridient',
            'item_icon': 'Z',
            'position_x': 13,
            'position_y': 3,
            'number': 2,
            'board': 2,
            'added_power': 0
            },
        'Biscuits':{ 
            'type': 'ingridient', 
            'item_icon': 'B',
            'position_x': 10,
            'position_y': 19,
            'number': 1,
            'board': 2,
            'added_power': 0
            },
        'Pralines':{ 
            'type': 'ingridient', 
            'item_icon': 'Q',
            'position_x': 57,
            'position_y': 27,
            'number': 1,
            'board': 2,
            'added_power': 0
            },
        'Candy':{ 
            'type': 'ingridient', 
            'item_icon': 'U',
            'position_x': 91,
            'position_y': 2,
            'number': 2,
            'board': 2,
            'added_power': 0
            },
        'Honey':{
            'type': 'ingridient',
            'item_icon': 'H',
            'position_x': 11,
            'position_y': 4,
            'number': 2,
            'board': 1,
            'added_power': 0
            },
        'Lollipop':{ 
            'type': 'ingridient', 
            'item_icon': 'L',
            'position_x': 9,
            'position_y': 17,
            'number': 1,
            'board': 1,
            'added_power': 0
            },
        'Donut':{ 
            'type': 'ingridient', 
            'item_icon': 'D',
            'position_x': 56,
            'position_y': 26,
            'number': 1,
            'board': 1,
            'added_power': 0
            },
        'Candy':{ 
            'type': 'ingridient', 
            'item_icon': 'E',
            'position_x': 90,
            'position_y': 5,
            'number': 2,
            'board': 1,
            'added_power': 0
            },
        'first_aid':{ 
            'type': 'life', 
            'item_icon': 'A',
            'position_x': 70,
            'position_y': 15,
            'number': 1,
            'board': 1,
            'added_power': 0
        }
    }


# OTHER CHARACTERS --------------

others = {
    'other': {
        'other_type': "quiz",
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
                        ["How many islands there are in Faroe Islands?\n(a) 412\n(b) 779\n(c) 18\n", "b", False]],
        'width': 1,
        'other_power': 1,
        'board': 1
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
        'questions': [],
        'width': 1,
        'other_power': 1,
        'board': 1
        },
    'other3': {
        'other_type': "enemy",
        'other_name': "Cow",
        'other_icon': "K",
        'position_x': 33,
        'position_y': 15,
        'step': 0,
        'other_health': 3,
        'goal_quiz': "milk",
        'questions': [],
        'width': 1,
        'other_power': 1,
        'board': 2
        },
    'boss': {
        'other_type': "enemy",
        'other_name': "Boss",
        'other_icon': "B",
        'position_x': 50,
        'position_y': 15,
        'step': 2,
        'other_health': 3,
        'goal_quiz': "winning",
        'questions': [],
        'width': 5,
        'other_power': 1,
        'board': 3
        }
    }  


# INVENTORY ---------------------

inventory = {}

