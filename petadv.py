
def parse_pet_time(message):
    """Your pet started an adventure, it will be back in 4h 0m 0s!
    Check its progress in pets"""
    params = message.split()
    hrs = int(params[10].replace('h', ''))
    mins = int(params[11].replace('m', ''))
    seconds = int(params[12].replace('s!', ''))

    total_secs = 60 * (hrs * 60 + mins) + seconds

def parse_pet_id(message):
    """ rpg pet adv a dig """
    params = message.split()
    return params[3].upper()

"""
        if 'pet adv' in msg or 'pets adv' in msg:
            id = petadv.parse_pet_id(msg)
            def check(m):
                erpgmsg = 'Your pet started an adventure, it will be back in'
                return message.author.id == 555955826880413696 and erpgmsg in message.content
            try:
                erpgresponse = await client.wait_for('message', check=check, timeout=5)
                await message.channel.send("Parsed pet adventure time: {}".format(petadv.parse_pet_time((erpgresponse))))
                await asyncio.sleep(petadv.parse_pet_time(erpgresponse))
                response = f"{mention}: Pet {id} has returned from its adventure!"
                await message.channel.send(response)
                return
            except asyncio.TimeoutError:
                await message.channel.send("Could not find ERPG response for pet adv.")
                return
"""