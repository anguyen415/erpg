from numpy import *
from copy import deepcopy
import random as rm

def dungeon_init_eleven():
    hp = 901
    board = zeros((8,8))
    board[7][1] = 9
    board[0][0] = 1
    board[0][2] = 1
    board[0][4] = 1
    board[0][6] = 1
    board_disp = dungeon_disp_eleven(board)
    return board_disp, board, hp

def dungeon_update_eleven(msg_content,board,hp,density):
    if msg_content.lower() == 'up':
      direction = 1
    if msg_content.lower() == 'left':
      direction = 2
    if msg_content.lower() == 'right':
      direction = 3
    if msg_content.lower() == 'pass':
      direction = 0
    if msg_content.lower() == 'attack':
      direction = 9
    attack_flag = 0
    board_update = deepcopy(board)
    init = where(board==9)
    x = int(''.join(map(str,init[0])))
    y = int(''.join(map(str,init[1])))
    feasible = dungeon_feasible_eleven(direction,x,y)
    if feasible == 0:
        board_disp = 'This action is impossible!'
        return board_disp, board_update, hp, attack_flag
    if feasible == 2:
        attack_flag = 1
        board_update = zeros((8,8))
        board_update[6][1] = 9
        board_disp = dungeon_disp_eleven(board_update)
        return board_disp, board_update, hp, attack_flag
    for i in range(1,8):
        for j in range(1,9):
            board_update[i][j-1] = board[i-1][j-1]
    for j in range(1,9):
        a = rm.random()*100
        if a < density:
            board_update[0][j-1] = 1
        else:
            board_update[0][j-1] = 0
    if direction == 0:
        if board_update[x][y] == 1:
            hp = hp-110
        else:
            hp = hp-10
        board_update[x][y] = 9
        if x < 7:
            board_update[x+1][y] = 0
    if direction == 1:
        if board_update[x-1][y] == 1 or board[x-1][y] == 1:
            hp = hp-100
        board_update[x-1][y] = 9
        board_update[x][y] = 0
        if x < 7:
            board_update[x+1][y] = 0
    if direction == 2:
        if board_update[x][y-1] == 1:
            hp = hp-100
        board_update[x][y-1] = 9
        if x < 7:
            board_update[x+1][y] = 0
    if direction == 3:
        if board_update[x][y+1] == 1:
            hp = hp-100
        board_update[x][y+1] = 9
        if x < 7:
            board_update[x+1][y] = 0
    board_disp = dungeon_disp_eleven(board_update)
    return board_disp, board_update, hp, attack_flag


def dungeon_disp_eleven(board_update):
    board_disp = ''
    for i in range(1,9):
        for j in range(1,9):
            if board_update[i-1][j-1] == 0:
                board_disp = board_disp + ':stop_button:'
            if board_update[i-1][j-1] == 1:
                board_disp = board_disp + ':fire:'
            if board_update[i-1][j-1] == 9:
                board_disp = board_disp + '<:ultraedgysword:754562251389665291>'
            if j == 8:
                if i == 1:
                    board_disp = board_disp + '<:d11:753653328721739947>\n'
                else:
                    board_disp = board_disp + '\n'
    return board_disp

def dungeon_feasible_eleven(direction,x,y):
    if x == 0 and direction == 1:
        return 0
    if y == 0 and direction == 2:
        return 0
    if y == 7 and direction == 3:
        return 0
    if x == 0 and y == 7 and direction == 9:
        return 2
    if (x != 0 or y != 7) and direction == 9:
        return 0
    return 1

def dungeon_dict_eleven(nickname,hp,boss,board_disp):
    mydict = {'author': {'name': nickname + "'s dungeon"},
              'fields': [{'name': '<:d11:753653328721739947> **THE ULTRA-EDGY DRAGON**',
                          'value': '—————————————————————\n**' + nickname + '** — :heart: ' + str(hp) + '/901\n**THE ULTRA-EDGY DRAGON** — :purple_heart: ' + str(boss*500) + '/1000\n—————————————————————',
                          'inline': False},
                         {'name': 'Map',
                          'value': board_disp,
                          'inline': False},
                         {'name': 'What will you do, ****' + nickname + '****?',
                          'value': '```UP - Move up\nLEFT - Move to the left\nRIGHT - Move to the right\nPASS - Does not move, but loses 10 HP\nATTACK - 500 Damage || Must be next to the dragon```',
                          'inline': False}],
              'color': 10115509, 'type': 'rich'}
    return mydict

def dungeon_dict_end_eleven(nickname,hp,boss,board_disp):
    mydict = {'author': {'name': nickname + "'s dungeon"},
              'fields': [{'name': '<:d11:753653328721739947> **THE ULTRA-EDGY DRAGON**',
                          'value': '—————————————————————\n**' + nickname + '** — :heart: ' + str(hp) + '/901\n**THE ULTRA-EDGY DRAGON** — :purple_heart: ' + str(boss*500) + '/1000\n—————————————————————',
                          'inline': False}],
              'color': 10115509, 'type': 'rich'}
    return mydict

def dungeon_init_fourteen():
    hp = 2000
    dragon = 1
    board = zeros((7,8))
    for i in range(1,8):
        for j in range(1,9):
            board[i-1][j-1] = rm.choices(range(1,8))[0]
    y = rm.choices(range(1,9))[0]
    current_on = rm.choices(range(1,8))[0]
    board[6][y-1] = 9
    board_disp = dungeon_disp_fourteen(board,dragon)
    return board_disp, board, hp, dragon, current_on

def dungeon_update_fourteen(msg_content,board,hp,state,current_on,dragon):
    if msg_content.lower() == 'up':
        direction = 1
    if msg_content.lower() == 'left':
        direction = 2
    if msg_content.lower() == 'right':
        direction = 3
    if msg_content.lower() == 'down':
        direction = 4
    if msg_content.lower() == 'pass':
        direction = 0
    if msg_content.lower() == 'attack':
        direction = 9
    
    attack_flag = 0
    board_update = board+1

    init = where(board==9)
    x = int(''.join(map(str,init[0])))
    y = int(''.join(map(str,init[1])))

    ind = where(board_update==8)
    board_update[ind] = 1
    
    feasible = dungeon_feasible_fourteen(direction,x,y)
    if feasible == 0:
        board_disp = 'This action is impossible!'
        dmg = 0
        return board_disp, board, hp, state, dmg, attack_flag, current_on, dragon
    if feasible == 2:
        attack_flag = 1
        dragon = 2
        board_update[init] = 9
        hp, state, dmg = damage(direction,x,y,board,hp,state)
        board_disp = dungeon_disp_fourteen(board_update,dragon)
        return board_disp, board_update, hp, state, dmg, attack_flag, current_on, dragon
    if feasible == 3:
        attack_flag = 1
        dragon = 3
        board_update[init] = 9
        hp, state, dmg = damage(direction,x,y,board,hp,state)
        board_disp = dungeon_disp_fourteen(board_update,dragon)
        return board_disp, board_update, hp, state, dmg, attack_flag, current_on, dragon
    hp, state, dmg = damage(direction,x,y,board,hp,state)
    
    if direction == 1:
        x = x-1
    if direction == 2:
        y = y-1
    if direction == 3:
        y = y+1
    if direction == 4:
        x = x+1
    if direction == 0:
        board_update[init] = 9
    if current_on < 7:
        board_update[init] = current_on+1
    else:
        board_update[init] = 1
    current_on = board[x][y]
    board_update[x][y] = 9

    if current_on == 4:
        board_update[x][y] = 5
        x = 6
        board_update[x][y] = 9
    if current_on == 5:
        board_update[x][y] = 6
        x = rm.choices(range(5,8))[0]-1
        y = rm.choices(range(1,9))[0]-1
        board_update[x][y] = 9
    if current_on == 7:
        board_update[x][y] = 3
        x = minimum(x+2,6)
        board_update[x][y] = 9
    
    board_disp = dungeon_disp_fourteen(board_update,dragon)
    return board_disp, board_update, hp, state, dmg, attack_flag, current_on, dragon

def dungeon_disp_fourteen(board_update,dragon):
    board_disp = ''
    if dragon == 1:
        board_disp = ':brown_square:<:d14:753653329158078614>:brown_square::brown_square::brown_square::brown_square:<:d14:753653329158078614>:brown_square:\n'
    if dragon == 2:
        board_disp = ':brown_square::brown_square::brown_square::brown_square::brown_square::brown_square:<:d14:753653329158078614>:brown_square:\n'
    if dragon == 3:
        board_disp = ':brown_square:<:d14:753653329158078614>:brown_square::brown_square::brown_square::brown_square::brown_square::brown_square:\n'
    for i in range(1,8):
        for j in range(1,9):
            if board_update[i-1][j-1] == 1:
                board_disp = board_disp + ':orange_square:'
            if board_update[i-1][j-1] == 2:
                board_disp = board_disp + ':yellow_square:'
            if board_update[i-1][j-1] == 3:
                board_disp = board_disp + ':green_square:'
            if board_update[i-1][j-1] == 4:
                board_disp = board_disp + ':purple_square:'
            if board_update[i-1][j-1] == 5:
                board_disp = board_disp + ':brown_square:'
            if board_update[i-1][j-1] == 6:
                board_disp = board_disp + ':red_square:'
            if board_update[i-1][j-1] == 7:
                board_disp = board_disp + ':blue_square:'
            if board_update[i-1][j-1] == 9:
                board_disp = board_disp + '<:omegaarmor:754562251079417959>'
            if j == 8:
                board_disp = board_disp + '\n'
    return board_disp

def dungeon_feasible_fourteen(direction,x,y):
    if x == 0 and direction == 1:
        return 0
    if x == 6 and direction == 4:
        return 0
    if y == 0 and direction == 2:
        return 0
    if y == 7 and direction == 3:
        return 0
    if (x==0 and y==1) and direction == 9:
        return 2
    if (x==0 and y==6) and direction == 9:
        return 3
    if (x!=0 or y!=1) and (x!=0 or y!=6) and direction == 9:
        return 0
    return 1

def damage(direction,x,y,board,hp,state):
    rng = rm.random()*0.15+0.85
    if direction == 1:
        x = x-1
    if direction == 2:
        y = y-1
    if direction == 3:
        y = y+1
    if direction == 4:
        x = x+1
    tile  = board[x][y]

    if direction == 0 or direction == 9 or tile == 4 or tile == 5 or tile == 7:
        pt = 0
        if direction == 0:
            pt = 1
        if state == 0:
            dmg = 0
            state = 0
        if state == 1:
            dmg = 0
            state = 0
        if state == 2:
            dmg = 34
            state = 1
        if state == 3:
            dmg = 34
            state = 2
        if state == 4:
            dmg = 0
            state = 0
        if state == 5:
            dmg = 88
            state = 4
        if state == 6:
            dmg = 88
            state = 5
        dmg = int(round(dmg*rng))+250*pt
        hp = hp-dmg
        return hp, state, dmg

    if tile == 1:
        if state == 0:
            dmg = 88
        if state == 1:
            dmg = 88
        if state == 2:
            dmg = 120
        if state == 3:
            dmg = 120
        if state == 4:
            dmg = 88
        if state == 5:
            dmg = 88
        if state == 6:
            dmg = 88
        state = 6

    if tile == 2:
        if state == 0:
            dmg = 34
        if state == 1:
            dmg = 34
        if state == 2:
            dmg = 34
        if state == 3:
            dmg = 34
        if state == 4:
            dmg = 34
        if state == 5:
            dmg = 120
        if state == 6:
            dmg = 120
        state = 3

    if tile == 3:
        dmg = 0
        state = 0

    if tile == 6:
        if state == 0:
            dmg = 244
            state = 0
        if state == 1:
            dmg = 244
            state = 0
        if state == 2:
            dmg = 278
            state = 1
        if state == 3:
            dmg = 278
            state = 2
        if state == 4:
            dmg = 244
            state = 0
        if state == 5:
            dmg = 332
            state = 4
        if state == 6:
            dmg = 332
            state = 5
    dmg = int(round(dmg*rng))
    hp = hp-dmg
    return hp, state, dmg

def dungeon_dict_fourteen(nickname,hp,boss,board_disp,dmg,state):
    embedmsg = 'You took a total of ' + str(dmg) + ' damage last turn.\n'
    if state == 2:
      embedmsg = embedmsg + 'Poison Tier I will last for 1 more turn.'
    if state == 3:
      embedmsg = embedmsg + 'Poison Tier I will last for 2 more turns.'
    if state == 5:
      embedmsg = embedmsg + 'Poison Tier II will last for 1 more turn.'
    if state == 6:
      embedmsg = embedmsg + 'Poison Tier II will last for 2 more turns.'
    if state == 0 or state == 1 or state == 4:
      embedmsg = embedmsg + 'You do not have any abnormal status right now.'
    mydict = {'author': {'name': nickname + "'s dungeon"},
              'fields': [{'name': '<:d14:753653329158078614>THE GODLY DRAGON',
                          'value': embedmsg + '\n—————————————————————\n**' + nickname + '** — :heart: ' + str(hp) + '/2000\n**THE GODLY DRAGON** — :purple_heart: ' + str(boss*1000) + '/2000\n—————————————————————',
                          'inline': False},
                         {'name': 'Map', 'value': board_disp,
                          'inline': False},
                         {'name': 'What will you do, **' + nickname + '**?', 'value': '```UP - Move up\nLEFT - Move to the left\nRIGHT - Move to the right\nDOWN - Move down\nPASS - Does not move, but loses 250 HP\nATTACK - 100% AT || Must be next to the dragon```',
                          'inline': False}], 'color': 10181046, 'type': 'rich'}
    return mydict

def dungeon_dict_end_fourteen(nickname,hp,boss,board_disp):
    mydict = {'author': {'name': nickname + "'s dungeon"},
              'fields': [{'name': '<:d14:753653329158078614>THE GODLY DRAGON',
                          'value': '—————————————————————\n**' + nickname + '** — :heart: ' + str(hp) + '/2000\n**THE GODLY DRAGON** — :purple_heart: ' + str(boss*1000) + '/2000\n—————————————————————',
                          'inline': False}], 'color': 10181046, 'type': 'rich'}
    return mydict
