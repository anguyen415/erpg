enchants = {
    'normie': 0,
    'good': 1,
    'great': 2,
    'mega': 3,
    'epic': 4,
    'hyper': 5,
    'ultimate': 6,
    'perfect': 7,
    'edgy': 8,
    'ultra-edgy': 9,
    'omega': 10,
    'ultra-omega': 11,
    'godly': 12
}

def parse_enchant(message):
    """
    embed_dict = erpgresponse.embeds[0].to_dict()
    embed_dict['fields'][0]['name']
    """
    return message[message.index("**") + 2: message.rindex("**")]

def compare_enchant(current, goal):
    if enchants[current.lower()] >= enchants[goal.lower()]:
        return True
    return False