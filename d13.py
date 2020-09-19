"""
{'name': 'AndyNub moved 1 room closer to the dragon', 'value': "—————————————————————\nTHE ULTRA-OMEGA DRAGON HITS AndyNub BY 0 POINTS OF LIFE\nAndyNub — :heart: 846/996\nTHE ULTRA-OMEGA DRAGON — :purple_heart: 666/lmao\n—————————————————————\nQUESTION: How many miliseconds have passed since you started this dungeon?\n:door: :door: :door:\nLeft: 170678\nCenter: 172606\nRight: 211659\n\n- Choosing the correct answer will move you 1 room closer when the room number is even, otherwise 2 rooms further\n- Choosing the wrong (but not so wrong) answer will move you 4 rooms further when the room number is lower than 9, otherwise 1 room closer\n- Choosing the wrong answer will move you 2 rooms closer when the dragon is at least 8 rooms away from you, 5 rooms further when the dragon is 3 or less rooms away, otherwise you won't move\n\nDragon's damage depends on how close you are", 'inline': False}
"""

""" ['fields']{"""
# room: {'correct': '', 'wrong': '', 'notsowrong': ''}
questions_key = {
    'wooden log tiers goes': {
        'correct': 'yes',
        'notsowrong': 'idk lol',
        'wrong': 'that\'s how the developer planned it'
    },
    'arcsin': {
        'correct': '-5.3175',
        'notsowrong': '-0.26399',
        'wrong': '63.2217'
    },
    'hi': {
        'correct': 'hi >w<!!',
        'notsowrong': 'hi owo',
        'wrong': 'hi'
    },
    '\'duel\'': {
        'correct': 'pvp',
        'notsowrong': 'fight',
        'wrong': 'there was not a command like that'
    },
    'maximum level': {
        'correct': '2147483647',
        'notsowrong': '2389472895789437',
        'wrong': '200'
    },
    'number am i thinking': {
        'correct': 'highest',
        'notsowrong': 'middle',
        'wrong': 'lowest'
    },
    'get an epic fish': {
        'correct': 'Area 2+',
        'notsowrong': 'The river',
        'wrong': 'Area 1+'
    },
    'coins do you start': {
        'correct': '250',
        'notsowrong': '500',
        'wrong': '0'
    },
    'types of trainings': {
        'correct': '5',
        'notsowrong': '4',
        'wrong': '1'
    },
    'cap in time travels': {
        'correct': 'like very high',
        'notsowrong': '10',
        'wrong': 'none'
    },
    'arena cookies do you have': {
        'correct': 'lowest',
        'notsowrong': 'middle',
        'wrong': 'highest'
    },
    'minimum level required to craft an electronical': {
        'correct': '20',
        'notsowrong': '22',
        'wrong': '24'
    },
    'vehicles are in epic rpg?': {
        'correct': '2',
        'notsowrong': '1',
        'wrong': 'What? there\'s no vehicles'
    },
    'best solo dungeon': {
        'correct': 'yes',
        'notsowrong': 'no, dungeon #12 was the best',
        'wrong': 'no, dungeon #11 was the best'
    },
    'miliseconds have passed since': {
        'correct': 'middle',
        'notsowrong': 'lowest',
        'wrong': 'highest'
    },
}
# room: {away: 'answer'}
answers_key = {
    1: {5: 'notsowrong', 0: 'attack'},
    2: {1: 'correct', 5: 'notsowrong', 0: 'attack'},
    3: {5: 'notsowrong'},
    4: {2: 'correct', 1: 'correct'},
    8: {9: 'notsowrong', 3: 'correct', 8: 'notsowrong', 2: 'correct', 7: 'notsowrong'},
    9: {4: 'notsowrong', 9: 'notsowrong', 3: 'notsowrong', 8: 'notsowrong'},
    10: {5: 'notsowrong', 4: 'notsowrong', 9: 'notsowrong'},
    11: {6: 'notsowrong', 5: 'notsowrong'},
    12: {7: 'notsowrong', 6: 'notsowrong'},
    13: {9: 'wrong', 8: 'wrong', 7: 'notsowrong'},
    14: {11: 'wrong', 10: 'wrong', 9: 'wrong'},
    15: {13: 'wrong', 12: 'wrong', 11: 'wrong'}
}

def get_answer(question, choices, room, rooms_away):
    response = {
        'door': '',
        'answer': ''
    }
    if not answers_key.get(room) or not answers_key[room].get(rooms_away):
        return {
            'door': 'Pattern not found.. Keep moving until re-aligned.',
            'answer': 'Pattern not found.. Keep moving until re-aligned.'
        }
    correct_choice = answers_key[room][rooms_away]
    if correct_choice == 'attack':
        return {
            'door': answers_key[room][rooms_away].upper(),
            'answer': answers_key[room][rooms_away].upper()
        }

    for shortq in questions_key.keys():
        if shortq == 'hi' and shortq == question:
            response.update({'answer': questions_key[shortq][correct_choice]})
            break
        if shortq != 'hi' and shortq in question:
            response.update({'answer': questions_key[shortq][correct_choice]})
            break

    if response['answer'] == 'lowest':
        lowest = min(int(choices['left']), int(choices['center']), int((choices['right'])))
        response.update({'door': get_key(choices, lowest, True)})
    elif response['answer'] == 'highest':
        highest = max(int(choices['left']), int(choices['center']), int((choices['right'])))
        response.update({'door': get_key(choices, highest, True)})
    elif response['answer'] == 'middle':
        middle = sorted([int(choices['left']), int(choices['center']), int(choices['right'])])[1]
        response.update({'door': get_key(choices, middle, True)})
    else:
        response.update({'door': get_key(choices, response['answer'].lower())})
    return response

def get_key(choices, value, number=False):
    for key, val in choices.items():
        if number:
            if int(val) == value:
                return key
        elif val == value:
            return key
    return None

def parse_question(message):
    msg = message.replace('**', '').replace('__', '')
    if '\n :door:' in msg:
        question = msg[msg.index('question: ')+10:msg.index('\n :door:')]
    else:
        question = msg[msg.index('question: ')+10:msg.index('\n:door:')]
    return question

def parse_choices(message):
    choices = {
        'left': '',
        'center': '',
        'right': '',
    }
    if '\n**left:**' in message:
        choices.update({'left': message[message.index('\n**left:**')+11:message.index('\n**center:**')]})
    if '\n**center:**' in message:
        choices.update({'center': message[message.index('\n**center:**')+13:message.index('\n**right:**')]})
    if '\n**right:**' in message:
        choices.update({'right': message[message.index('\n**right:**')+12:message.index('\n\n-')]})
    return choices

def parse_room(message):
    room = int(message[message.index('`')+1:message.rindex('`\n')])
    return room

def parse_rooms_away(message):
    rooms_away = int(message[message.index('is ')+3:message.index(' rooms away from you')])
    return rooms_away