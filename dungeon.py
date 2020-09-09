"""
Dungeon Calculator

Calculates success rates for a player in a dungeon (assuming 2 players)

Example Usage:

import dungeon

dungeon.parse_input(message)

Command Format:
    
dungeon bestmove dungeon# attack defense life [samplesize]
dungeon sample dungeon# attack defense life move [samplesize]
dungeon calc dungeon# attack defense life [move]

Examples:

dungeon bestmove 7 238 240 360
dungeon sample 7 238 240 360 bite
dungeon calc 7 238 240 360

"""

from random import random

# For 2 players
# 'dx': (hp, attack)
dungeon_stats = {
    1: (100, 37),
    2: (450, 71),
    3: (850, 109),
    4: (1250, 143),
    5: (3000, 179),
    6: (5000, 215),
    7: (8000, 253),
    8: (12000, 286),
    9: (30000, 323)
    }

# 'move': (chance, dmg multiplier)
attack_stats = {
    'bite': (1.0, 1),
    'stab': (0.7, 2),
    'power': (0.4, 4)
    }

def calc(dungeon, attack, defense, life, move='bite', printstats=True):
    '''
    One simulation run of dungeon

    Parameters
    ----------
    dungeon : int
        Dungeon: 1, 2, 3, ... 9
    attack : int
        Attack Stat
    defense : int
        Defense Stat
    life : int
        Life Points (include Life Boost if wanted)
    move : string, optional
        Attack moves bite, stab, or power. The default is 'bite'.
    size : int, optional
        Sample size. The default is 1000.
    printstats : bool, optional
        If true, prints out stats of the run. The default is True.

    Returns
    -------
    bool
        True if success, False if fail
    rounds : int
        Total rounds of dungeon
    dragon_hp : int
        Remaining Dragon HP
    player_hp : int
        Remaining Player HP

    '''
    player_hp = life
    dragon_hp = dungeon_stats[dungeon][0]
    dragon_atk = dungeon_stats[dungeon][1]
    
    rounds = 0
    successful_attacks = 0
    failed_attacks = 0
    
    while dragon_hp > 0:
        if calc_percentage(move.lower()):
            dragon_hp -= (attack * attack_stats[move][1])
            successful_attacks += 1
        else:
            failed_attacks += 1
        dmg_taken = dragon_atk - defense
        if defense > dragon_atk:
            dmg_taken = 1
        player_hp -= dmg_taken
        rounds += 1
         
    response = '''Simulating **Dungeon {}** using **{}**
    
    **Dungeon Stats:**
    Dungeon: **{}**
    Dragon HP: {}
    Dragon ATK: {}
    
    **Player Stats:**
    ATK: {}
    DEF: {}
    LIFE: {}
    
    **Results:**
    Resulting Dragon HP: {}
    Resulting Player HP: {}
    Total Rounds: {}
    
    '''.format(
    dungeon, move.upper(),
    dungeon,
    dragon_hp,
    dragon_atk,
    attack,
    defense,
    life,
    dragon_hp,
    player_hp,
    rounds)
    
    if player_hp > 0:
        response+=('**Dungeon CLEAR!!!**')
    else:
        response+=('**Dungeon FAILED NOOB**')
        
    if printstats:
        print(response)
        
    if player_hp > 0:
        return (response, True, rounds, dragon_hp, player_hp)
    else:
        return (response, False, rounds, dragon_hp, player_hp)
        
def calc_percentage(move):
    percentage = attack_stats[move][0]
    if random() < percentage:
        return True
    return False
       
def sample(dungeon, attack, defense, life, move, size=1000, printstats=True):
    '''
    Simulate dungeon instance (size) amount of times
    
    Parameters
    ----------
    dungeon : int
        Dungeon 1, 2, 3 ... 9
    attack : int
        Attack Stat
    defense : int
        Defense Stat
    life : int
        Life Points (include Life Boost if wanted)
    move : string
        Attack moves bite, stab, or power. The default is 'bite'.
    size : int, optional
        Sample size. The default is 1000.
    printstats : bool, optional
        If true, prints out stats of the run. The default is True.

    Returns
    -------
    success_rate : float
        Success rate

    '''
    clear_count = 0
    fail_count = 0
    rounds_list = []
    dragon_hp_list = []
    life_list = []
    
    dragon_hp = dungeon_stats[dungeon][0]
    dragon_atk = dungeon_stats[dungeon][1]
    
    for _ in range(size):
        _, result, rounds, dhp, hp = calc(dungeon, attack, defense, life, move=move, printstats=False)
        if result is True:
            clear_count += 1
        else:
            fail_count += 1
        
        rounds_list.append(rounds)
        dragon_hp_list.append(dhp)
        life_list.append(hp)
        
    avg_rounds = sum(rounds_list)/size
    avg_dragon_hp = sum(dragon_hp_list)/size
    avg_life = sum(life_list)/size
    success_rate = (clear_count/size)*100
    
    response = '''Sampling Size of **{}** using **{}**
    
    **Dungeon Stats:**
    Dungeon: **{}**
    Dragon HP: {}
    Dragon ATK: {}
    
    **Player Stats:**
    ATK: {}
    DEF: {}
    LIFE: {}
    
    **Results:**
    Avg Rounds: {}
    Avg Remaining Dragon HP: {}
    Avg Remaining Life: {}
    # Success: {}
    # Failed: {}
    Success Rate: {}
    '''.format(
    size, move.upper(),
    dungeon,
    dragon_hp,
    dragon_atk,
    attack,
    defense,
    life,
    avg_rounds,
    avg_dragon_hp,
    avg_life,
    clear_count, fail_count,
    success_rate)
    
    if printstats:
        print(response)

    return (response, success_rate)

def best_move(dungeon, attack, defense, life, size=1000, printstats=True):
    '''
    Calculates the move with highest probability of success
    
    Returns tuple with Best Move, and dictionary of Success Rates
    Access each rate by success_rates['move']

    Parameters
    ----------
    dungeon : string
        Dungeon 1, 2, 3 ... 9
    attack : int
        Attack Stat
    defense : int
        Defense Stat
    life : int
        Life Points (include Life Boost if wanted)
    move : string, optional
        Attack moves bite, stab, or power. The default is 'bite'.
    size : int, optional
        Sample size. The default is 1000.
    printstats : bool, optional
        If true, prints out stats of the run. The default is True.
        
    Returns
    -------
    best_move : string
        Move with highest probability of success
    success_rates : dict
        Dictionary containing all success rates for each move
        
    '''
    success_rates = {
        'bite': sample(dungeon, attack, defense, life, move='bite', size=size, printstats=False)[1],
        'stab': sample(dungeon, attack, defense, life, move='stab', size=size, printstats=False)[1],
        'power': sample(dungeon, attack, defense, life, move='power', size=size, printstats=False)[1]
        }
    dragon_hp = dungeon_stats[dungeon][0]
    dragon_atk = dungeon_stats[dungeon][1]
        
    if success_rates['bite'] == success_rates['stab'] and success_rates['stab'] == success_rates['power'] and success_rates['bite'] != 0:
        best_move  = 'power'
    elif success_rates['bite'] == 0 and success_rates['stab'] == 0 and success_rates['power'] == 0:
        best_move = 'N/A... FAIL REGARDLESS'
    else:
        best_move = max(success_rates, key=success_rates.get)
    
    response ='''Best Move Success Rate with Sample Size of **{}**
    
    **Dungeon Stats:**
    Dungeon: **{}**
    Dragon HP: {}
    Dragon ATK: {}
    
    **Player Stats:**
    ATK: {}
    DEF: {}
    LIFE: {}
    
    Success using **BITE**: {}
    Success using **STAB**: {}
    Success using **POWER**: {}
    
    Highest Success using: **{}**'''.format(
    size,
    dungeon,
    dragon_hp,
    dragon_atk,
    attack,
    defense,
    life,
    success_rates['bite'],
    success_rates['stab'],
    success_rates['power'],
    best_move.upper())
    
    if printstats:
        print(response)
        
    return (response, best_move.upper())
        
def parse_input(input_str):
    try:
        params = input_str.split(' ')
        fnc = params[1]
        if fnc == 'help':
            return '''**__Dungeon Simulation Functions__**\n
                  `dungeon bestmove dungeon# attack defense life [samplesize]`
                  \t-Gets highest probability move for success. Default samplesize=1000
                  \tEx: `dungeon bestmove 7 238 240 360`\n
                  `dungeon sample dungeon# attack defense life move [samplesize]`
                  \t-Simulates dungeon samplesize amount of times. Default samplesize=1000
                  \tEx: `dungeon sample 7 238 240 360 bite`\n
                  `dungeon calc dungeon# attack defense life [move]`
                  \t-Simulates dungeon 1 time. Default move is 'bite'
                  \tEx: `dungeon calc 7 238 240 360`'''
                  
        dungeon = int(params[2])
        attack = int(params[3])
        defense = int(params[4])
        life = int(params[5])
        if fnc == 'bestmove':
            if len(params) > 6:
                size = int(params[6])
            else:
                size = 1000
            return best_move(dungeon, attack, defense, life, size)[0]
        elif fnc == 'sample':
            move = params[6]
            if len(params) > 7:
                size = int(params[7])
            else:
                size = 1000
            return sample(dungeon, attack, defense, life, move, size)[0]
        elif fnc == 'calc':
            if len(params) > 6:
                move = params[6]
            else:
                move = 'bite'
            return calc(dungeon, attack, defense, life, move)[0]
        else:
            raise Exception('function {} not found'.format(fnc))
    except Exception as e:
        return '''Error parsing input: {}.\n
              Command Formats:\n
              `dungeon bestmove dungeon# attack defense life [samplesize]`\n
              `dungeon sample dungeon# attack defense life move [samplesize]`\n
              `dungeon calc dungeon# attack defense life [move]`\n\n
              Parameters in brackets are optional\n\nSmh fking idiot'''.format(e)