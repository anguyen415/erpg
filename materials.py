# This code is messy... Eventually reformat it.
# It's currently reading emote names without spaces, then adding spaces back in when sending msgs.
# Ideally read full item name from inventory.

from constants import mats, mat_tiers

""" Main """
def calc_mats(inventory, goal_dict):
    goal_item = goal_dict['item']
    goal_amt = goal_dict['amt']
    item_type, item_type_emote = get_item_type(goal_item)
    emote = get_item_emote(goal_item)
    if inventory.get(goal_item):
        if inventory[goal_item] >= goal_amt:
            return {'error': f'fk u. u alrdy have **{goal_amt} {emote} {add_space(goal_item)}**... stop making me do work'}
        goal_amt -= inventory[goal_item]

    craft_dict = {
        'normiefish': 0,
        'goldenfish': 0,
        'epicfish': 0,
        'woodenlog': 0,
        'epiclog': 0,
        'superlog': 0,
        'megalog': 0,
        'hyperlog': 0,
        'ultralog': 0,
        'apple': 0,
        'banana': 0
    }

    for tier in reversed(range(0, mat_tiers[item_type].index(goal_item))):
        item = mat_tiers[item_type][tier]
        goal_amt = goal_amt * mats[mat_tiers[item_type][mat_tiers[item_type].index(item)+1]][1]
        if inventory.get(item):
            if inventory[item] >= goal_amt:
                break
            goal_amt -= inventory[item]
        if tier > 0:
            craft_dict.update({mat_tiers[item_type][tier]: goal_amt})
        else:
            return {'error': f'**OOF!!** u poor. not enuf mats. git gud. \n'
                             f'**__{goal_amt} additional {add_space(item)}__** {get_item_emote(item)} '
                             f'are required to craft **{goal_dict["amt"]} {add_space(goal_dict["item"])}** '
                             f'{get_item_emote(goal_dict["item"])}\n'
                             f'Try again after obtaining/trading the required {get_item_emote(item)} '
                             f'**{add_space(item)}**'}
    if inventory.get(goal_dict['item']):
        craft_dict.update({goal_item: (goal_dict['amt']-inventory[goal_item])})
    else:
        craft_dict.update({goal_item: goal_dict['amt']})
    return craft_dict

def calc_fruit_salad(inventory, goal_dict):
    craft_dict = {
        'apple': 0,
        'banana': 0
    }
    total_apples = goal_dict['amt'] * 25
    total_bananas = goal_dict['amt'] * 6
    converted_total_apples = (total_bananas * 15) + total_apples
    converted_current_apples = calc_base_mats(inventory, type='fruit')
    if converted_current_apples < converted_total_apples:
        diff = converted_total_apples - converted_current_apples
        return {
            'error': f'**OOF!!** u poor. not enuf mats. git gud. \n'
                     f'**__{diff} additional {add_space("apple")}__** {get_item_emote("apple")} '
                     f'are required to craft **{goal_dict["amt"]} FRUIT SALAD <:fruitsalad:754211288837652531>** \n'
                     f'Try again after obtaining/trading the required '
                     f'{get_item_emote("apple")} **{add_space("apple")}**'
        }
    if inventory.get('banana'):
        total_bananas -= inventory['banana']
        if inventory['apple']/15 >= total_bananas:
            craft_dict.update({'banana': total_bananas})
    else:
        craft_dict.update({'banana': total_bananas})
    craft_dict.update({'fruitsalad': goal_dict['amt']})
    return craft_dict


""" Parsers """
def parse_command(message):
    """ craft 2 ultralog """
    try:
        params = message.split(' ')
        if params[1] == 'help':
            return {
                'help': f'**Syntax**: `craft amt item`\n'
                        f'**Example**: `craft 2 ultralog` | `craft 2 fruit salad`'
            }
        amt = int(params[1])
        item = "".join(params[2:])
        if item == 'fruitsalad':
            return {
                'amt': amt,
                'item': item
            }

        if item == 'woodenlog' or item == 'normiefish' or item == 'apple' or item == 'ruby' or not mats.get(item):
            return {
                'error': f'**{item}** is not supported by this function idiot???\n'
                         f'**__Supported Items__**: \n'
                         f'**Epic Log and above** {get_item_emote("epiclog")} {get_item_emote("superlog")}'
                         f'{get_item_emote("megalog")} {get_item_emote("hyperlog")} {get_item_emote("ultralog")}\n'
                         f'**Golden Fish and above** {get_item_emote("goldenfish")} {get_item_emote("epicfish")}\n'
                         f'**Bananas** {get_item_emote("banana")}'
                         f'**Fruit Salad** <:fruitsalad:754211288837652531>'
            }
        if mats.get(item):
            return {
                'amt': amt,
                'item': item
            }
        return {
            'error': "Incorrect syntax. Proper usage: `craft amt item` Ex: `craft 2 ultra log`"
        }

    except Exception as e:
        return {
            'error': "Incorrect syntax. Proper usage: `craft amt item` Ex: `craft 2 ultra log`"
        }

def parse_inventory(embed_dict):
    """ Parses each material in inventory and returns it as a dictionary """
    inventory = {}
    items = embed_dict['fields'][0]['value'].split('\n')
    for item in items:
        key = item[item.index("**") + 2:item.rindex("**")].lower().replace(' ', '')
        value = int(item[item.index(": ") + 2:])
        inventory[key] = value
    return inventory

def parse_response(craft_dict):
    response = ''
    for item, amt in craft_dict.items():
        if int(amt) > 0:
            if 'log' in item:
                response += f'{amt} {get_item_emote(item)} {item.replace("log", " log")}\n'
            if 'fish' in item:
                response += f'{amt} {get_item_emote(item)} {item.replace("fish", " fish")}\n'
            if 'apple' in item or 'banana' in item:
                response += f'{amt} {get_item_emote(item)} {item}\n'
            if 'fruitsalad' in item:
                response += f'{amt} <:fruitsalad:754211288837652531> fruit salad'
    return response

def add_space(item):
    if 'log' in item:
        item = item.replace("log", " log")
    elif 'fish' in item:
        item = item.replace("fish", " fish")
    return item.upper()

""" Getters"""
def get_item_type(item):
    if 'log' in item:
        return 'log', mats['woodenlog'][0]
    if 'fish' in item:
        return 'fish', mats['normiefish'][0]
    if 'apple' == item or 'banana' == item:
        return 'fruit', mats['apple'][0]

def get_item_emote(item):
    if mats.get(item):
        return mats[item][0]
    return '<couldnt find emote lul>'

""" Retired """
def calc_base_mats(inventory, type='log'):
    total = 0
    for item, amt in inventory.items():
        if type in item:
            total += int(amt) * mats[item][1]
        if type == 'fruit' and (item == 'apple' or item == 'banana'):
            total += int(amt) * mats[item][1]
    return total