import constants

def parse_message_cd(message, cooldown):
    params = message.split()
    if len(params) <= 1:
        return None
    command = params[1]
    if len(params) >= 3:
        if command.startswith('pet') and params[2].startswith('adv'):
            return constants.cooldowns.get('pet adv')
        if command.startswith('buy') and any(['lb' in message, 'lootbox' in message]):
            return constants.cooldowns.get('lootbox')
        if command.startswith('duel'):
            return constants.cooldowns.get('duel')
        if command.startswith('horse') and any([params[2].startswith('breed'), params[2].startswith('race')]):
            return constants.cooldowns.get('horse breed') * cooldown
        if command.startswith('guild') and any([params[2] == 'raid', params[2] == 'upgrade']):
            return constants.cooldowns.get('guild')

    if command in constants.worker_cmds:
        return constants.cooldowns.get('worker') * cooldown
    if any([command.startswith('hunt'),
            'hunt t' in message,
            'hunt h t' in message,
            'hunt hardmode t' in message]):
        return constants.cooldowns.get('hunt') * cooldown
    if command.startswith('adv'):
        return constants.cooldowns.get('adventure') * cooldown
    if command == 'tr' or command == 'training':
        return constants.cooldowns.get('training') * cooldown
    if constants.cooldowns.get(" ".join(params[1:])):
        return constants.cooldowns.get(" ".join(params[1:])) * cooldown
    return None
