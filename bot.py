# -*- coding: utf-8 -*-
"""
ERPG Discord Bot

pip install -U python-dotenv
pip install -U discord

"""
import asyncio
import discord
from dotenv import load_dotenv
import os
import sys

import constants
import emoji
import enchant
import d13
import dungeon
from dung_sim import *
from dung_tr_solver import *
import materials
import reminders

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN') #"NzM2NzEwMDIyMjUxMTUxNDYy.XxywrA.DiLLolnudZFZ5e2nL8HDcEUOk5A"

client = discord.Client()
erpg_bot_id = 555955826880413696

@client.event
async def on_message(message):
    try:
        guild = message.guild
        mention = message.author.mention
        msg = " ".join(message.content.lower().split())
        user = message.author
        cd = 1
        if len(message.embeds) > 0:
            msg_embed = message.embeds[0].to_dict()
        else:
            msg_embed = 0
        msg_txt = emoji.demojize(message.content)

        #if len(message.embeds)>0:
        #    embed_dict = message.embeds[0].to_dict()
        #    await message.channel.send(f"```{embed_dict}```")

        # Training Solver, D13 Solver, D14 Solver
        if message.author.id in [erpg_bot_id, client.user.id]:
            # Training Solver
            if "is training in" in msg_txt.lower():
                response = trhelper(msg_txt.lower())
                await message.channel.send(response)
                return

            # D13 and D14 Solver (Ruch)
            if msg_embed != 0:
                response = dungeon_auto_solver(msg_embed)
                if response != 0:
                    await message.channel.send(response)
                    return

            # # D13 Solver (wrak)
            # if len(message.embeds) > 0:
            #     embed_dict = message.embeds[0].to_dict()
            #     if embed_dict.get('fields') and len(embed_dict['fields']) >= 3 and any([
            #         'ultra-omega dragon' in embed_dict['fields'][0]['value'].lower(),
            #         'ultra-omega dragon' in embed_dict['fields'][0]['name'].lower()]):
            #         question = d13.parse_question(embed_dict['fields'][0]['value'].lower())
            #         choices = d13.parse_choices(embed_dict['fields'][0]['value'].lower())
            #         room = d13.parse_room(embed_dict['fields'][2]['value'].lower())
            #         rooms_away = d13.parse_rooms_away(embed_dict['fields'][2]['value'].lower())
            #         answer = d13.get_answer(question, choices, room, rooms_away)
            #         embed = discord.Embed(
            #             title="D13 Solver",
            #             color=0x498fc9)
            #         embed.add_field(name='**Answer:**', value=f'`{answer["door"]}`', inline=False)
            #         embed.add_field(name='**Location:**', value=f'Current Room: `{room}`\nRooms Away: `{rooms_away}`',
            #                         inline=False)
            #         embed.set_thumbnail(url=constants.dungeon_images['d13'])
            #         await message.channel.send(embed=embed)
            #     return

        # Ignore if message is from our bot
        if message.author == client.user:
            return

        # Memes
        if msg.startswith('ping'):
            response = '{} Shut the fuck up idiot leave me alone'.format(mention)
            await message.channel.send(response)
            return

        if 'tprtm' in msg:
            response = '**TPRTM 쎾쓰** https://tenor.com/view/ishiki-foodwars-shokugeki-no-soma-gif-10828799'
            await message.channel.send(response)
            return

        # Donor CD Self-Assign
        if msg.startswith('role'):
            if len(msg.split()) > 1 and 'donor cd' in msg:
                role = discord.utils.get(guild.roles, name="-35% Donor CD")
                if role in user.roles:
                    await user.remove_roles(role)
                    await message.channel.send(f'Removed -35% Donor CD role from {mention}')
                else:
                    await user.add_roles(role)
                    await message.channel.send(f'Added -35% Donor CD role from {mention}')
                return
            elif 'help' in msg:
                await message.channel.send('Adds/removes -35% Donor CD role. Usage: `role -35% Donor CD`')
                return
            return

        # Reminders
        if msg.startswith('rpg'):
            if discord.utils.get(guild.roles, name="-35% Donor CD"):
                role = discord.utils.get(guild.roles, name="-35% Donor CD")
            else:
                role = await guild.create_role(name="-35% Donor CD")
            if role in user.roles:
                cd = 1 - .35
            cooldown = reminders.parse_message_cd(msg, cd)
            if not cooldown:
                return

            def check_cd(m):
                if len(m.embeds) > 0 and \
                        m.embeds[0].to_dict().get('fields') and \
                        m.embeds[0].to_dict()['fields'][0]['name'] and \
                        'cooldown' not in m.embeds[0].to_dict()['fields'][0]['name'].lower():
                    return False
                if message.author == m.author:
                    return False
                return m.author.id == erpg_bot_id and 'epic guard' not in m.content.lower()
            def check_tr(m):
                if message.author == m.author:
                    return False
                return check_cd(m) and any([
                    'well done' in m.content.lower(),
                    'better luck next time' in m.content.lower()
                ])
            def check_lb(m):
                if message.author == m.author:
                    return False
                return check_cd(m) and 'can\'t carry more than 1 lootbox' not in m.content.lower()
            try:
                if 'rpg tr' == msg or 'rpg training' in msg:
                    await client.wait_for('message', check=check_tr, timeout=10)
                    await asyncio.sleep(cooldown)
                    await message.channel.send(f'Reminder {mention}: **RPG TR** is ready!')
                    return
                if msg.startswith('rpg buy') and any(['lb' in msg, 'lootbox' in msg]):
                    await client.wait_for('message', check=check_lb, timeout=10)
                    await asyncio.sleep(cooldown)
                    await message.channel.send(f'Reminder {mention}: **RPG BUY LOOTBOX** is ready!')
                    return
                if msg.startswith('rpg guild'):
                    if any(['raid' in msg, 'upgrade' in msg]):
                        await client.wait_for('message', check=check_cd, timeout=10)
                        await asyncio.sleep(cooldown)
                        await message.channel.send(f'Reminder {mention}: **{message.content.upper()}** is ready!')
                        return
                    return
                if msg.startswith('rpg duel'):
                    await client.wait_for('message', check=check_cd, timeout=10)
                    await asyncio.sleep(cooldown)
                    await message.channel.send(f'Reminder {mention}: **RPG DUEL** is ready!')
                    return
                if msg.startswith('rpg horse breed'):
                    await client.wait_for('message', check=check_cd, timeout=10)
                    await asyncio.sleep(cooldown)
                    await message.channel.send(f'Reminder {mention}: **RPG HORSE BREED** is ready!')
                    return
                if msg.startswith('rpg pet') and 'adv' in msg:
                    await client.wait_for('message', check=check_cd, timeout=10)
                    await asyncio.sleep(cooldown)
                    await message.channel.send(f'Reminder {mention}: **RPG PET ADV** is ready!')
                    return
                await client.wait_for('message', check=check_cd, timeout=10)
                await asyncio.sleep(cooldown)
                await message.channel.send(f'Reminder {mention}: **{message.content.upper()}** is ready!')
                return
            except asyncio.TimeoutError:
                print(f'OOF. Timed out waiting for ERPG response for {message.author}\'s msg: {message.content}!')
                return
            return

        # if msg.startswith('rpg'):
        #     if discord.utils.get(guild.roles, name="-35% Donor CD") in user.roles:
        #         print(f'haha this noob is donor {message.author} haha -35% cd hahaha {message.content}')
        # # # Reminders
        # if msg.startswith('rpg'):
        #     if not discord.utils.get(guild.roles, name="-35% Donor CD"):
        #         role = await guild.create_role(name="-35% Donor CD")
        #     else:
        #         role = discord.utils.get(guild.roles, name="-35% Donor CD")
        #     if role in user.roles:
        #         cd = 1 - .35
        #     cooldown = reminders.parse_message_cd(msg, cd)
        #     if not cooldown:
        #         return
        #
        #     def check(m):
        #         return m.author.id == erpg_bot_id and 'epic guard' not in m.content.lower() and \
        #                all([
        #                    m.embeds[0].to_dict().get('description'),
        #                    'cooldown' in m.embeds[0].to_dict()['description'].lower()])
        #
        #     def check_tr(m):
        #         return m.author.id == erpg_bot_id and 'epic guard' not in m.content.lower() and \
        #                all([len(m.embeds) > 0,
        #                     m.embeds[0].to_dict().get('description'),
        #                     'cooldown' in m.embeds[0].to_dict()['description'].lower()]) and \
        #                any([
        #                    'well done' in m.content.lower(),
        #                    'better luck next time' in m.content.lower()
        #                ])
        #
        #     def check_lb(m):
        #         return m.author.id == erpg_bot_id and 'epic guard' not in m.content.lower() and \
        #                all([len(m.embeds) > 0,
        #                     m.embeds[0].to_dict().get('description'),
        #                     'cooldown' in m.embeds[0].to_dict()['description'].lower()]) and \
        #                'cannot carry more' not in m.content.lower()
        #
        #     def check_duel(m):
        #         return m.author.id == erpg_bot_id and 'epic guard' not in m.content.lower() and \
        #                all([len(m.embeds) > 0,
        #                     m.embeds[0].to_dict().get('description'),
        #                     'cooldown' in m.embeds[0].to_dict()['description'].lower()]) and \
        #                all([user in m.embeds[0].to_dict()['author']['name'],
        #                     'duel' in m.embeds[0].to_dict()['author']['name']])
        #
        #     def check_horse(m):
        #         return m.author.id == erpg_bot_id and 'epic guard' not in m.content.lower() and \
        #                all([len(m.embeds) > 0,
        #                     m.embeds[0].to_dict().get('description'),
        #                     'cooldown' in m.embeds[0].to_dict()['description'].lower()]) and \
        #                'breeding request accepted' in m.embeds[0].to_dict()['values'][0]['name']
        #
        #     try:
        #         if msg.startswith('rpg tr'):
        #             print('waiting for erpg response for rpg tr')
        #             response = await client.wait_for('message', check=check_tr, timeout=10)
        #             print(f'found response for rpg tr! sleeping for {cooldown}')
        #             await asyncio.sleep(cooldown)
        #             await message.channel.send(f'{mention}: **{msg.upper()}** is ready!')
        #             return
        #         if msg.startswith('rpg buy') and any([msg.contains('lb'), msg.contains('lootbox')]):
        #             print('waiting for erpg response for rpg buy lb')
        #             response = await client.wait_for('message', check=check_lb, timeout=10)
        #             print(f'found response for rpg buy lb! sleeping for {cooldown}')
        #             await asyncio.sleep(cooldown)
        #             await message.channel.send(f'{mention}: **{msg.upper()}** is ready!')
        #             return
        #         if msg.startswith('rpg duel'):
        #             print('waiting for erpg response for rpg duel')
        #             response = await client.wait_for('message', check=check_duel, timeout=10)
        #             print(f'found response for rpg duel! sleeping for {cooldown}')
        #             await asyncio.sleep(cooldown)
        #             await message.channel.send(f'{mention}: **RPG DUEL** is ready!')
        #             return
        #         if msg.startswith('rpg horse breed'):
        #             print('waiting for erpg response for rpg horse breed')
        #             response = await client.wait_for('message', check=check_horse, timeout=10)
        #             print(f'found response for rpg horse breed! sleeping for {cooldown}')
        #             await asyncio.sleep(cooldown)
        #             await message.channel.send(f'{mention}: **RPG HORSE BREED** is ready!')
        #             return
        #         # Checks for non-epic guard responses
        #         print(f'waiting for erpg response for {msg}')
        #         response = await client.wait_for('message', check=check, timeout=10)
        #         print(f'found response for {msg}! sleeping for {cooldown}')
        #         await asyncio.sleep(cooldown)
        #         await message.channel.send(f'{mention}: **{msg.upper()}** is ready!')
        #         return
        #     except asyncio.TimeoutError:
        #         await message.channel.send(f"Could not find ERPG response for this command... :{msg}")
        #         print(f"{message.author} has error'd while doing some shitty cmd!: {msg}")
        #     return

        # Dungeon Sim

        if msg.startswith('dungeon') and message.author.id != erpg_bot_id:
            if len(msg.split(' ')) >= 4:
                if int(msg.split(' ')[3]) <= 0:
                    await message.channel.send('fk u ruch')
                    return
            response = dungeon.parse_input(message.content)
            embed = discord.Embed(title="Dungeon Simulator", description="", color=0x498fc9)
            embed.add_field(name='Results', value=response, inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/753854654051385455.png?v=1")
            await message.channel.send(embed=embed)
            return

        # Enchanter
        if msg.startswith('enchant until'):
            thumbnail = "https://cdn.discordapp.com/emojis/651128516779442179.png?v=1"
            if not discord.utils.get(guild.roles, name="wrakMuted"):
                role = await guild.create_role(name="wrakMuted")
                for channel in guild.channels:
                    await channel.set_permissions(role, send_messages=False, read_message_history=True)

            goal_enchant = msg.split()[2]
            if not enchant.enchants.get(goal_enchant):
                embed = discord.Embed(
                    title="Enchant Helper",
                    description=f'Ha.. nice try.. **{" ".join(msg.split()[2:])}** is not a valid enchantment nerd.',
                    color=0x498fc9)
                embed.set_thumbnail(url=thumbnail)
                await message.channel.send(embed=embed)
                return

            ack = f"{constants.emotes['sparkles']} Ok {mention}, you will be muted for 5 secs " \
                  f"when your enchantment is **{goal_enchant.upper()}** or higher. {constants.emotes['sparkles']}\n" \
                  f"You can turn off the bot with `enchant off`"
            embed = discord.Embed(
                title="Enchant Helper",
                description=ack,
                color=0x498fc9)
            embed.set_thumbnail(url=thumbnail)
            await message.channel.send(embed=embed)
            print(f"{message.author} is currently enchanting until {goal_enchant}!!")
            done = False
            while not done:
                def check(m):
                    return m.author.id == erpg_bot_id or m.author.id == message.author.id
                try:
                    response = await client.wait_for('message', check=check, timeout=300)
                    if 'enchant off' in response.content:
                        done = True
                        embed = discord.Embed(
                            title="Enchant Helper",
                            description=f'No longer tracking your enchants {mention}',
                            color=0x498fc9)
                        embed.set_thumbnail(url=thumbnail)
                        await message.channel.send(embed=embed)
                        break
                    if response.author.id == message.author.id:
                        continue
                    if len(response.embeds) <= 0:
                        continue
                    embed_dict = response.embeds[0].to_dict()
                    if embed_dict.get('description') and 'cooldown' in embed_dict['description'].lower():
                        continue
                    if not embed_dict.get('description') or 'enchant' not in embed_dict['description'].lower() or 'broke' in embed_dict['description'].lower():
                        continue
                    name = embed_dict['author']['name']
                    if name[:name.index("'")] not in str(message.author):
                        continue
                    enchant_str = embed_dict['fields'][0]['name']
                    current_enchant = enchant.parse_enchant(enchant_str)
                    if enchant.compare_enchant(current_enchant, goal_enchant):
                        goal_met = f"{constants.emotes['wrakuwu']} {mention} **{current_enchant.upper()}** has " \
                                   f"been found!! It is better or equal to your goal! {constants.emotes['wrakuwu']}"
                        embed = discord.Embed(
                            title="Enchant Helper",
                            description=goal_met,
                            color=0x498fc9)
                        embed.set_thumbnail(url=thumbnail)
                        await message.channel.send(embed=embed)
                        muted = discord.utils.get(user.guild.roles, name="wrakMuted")
                        embed = discord.Embed(
                            title="Enchant Helper",
                            description=f'Muting {mention} for 5 seconds',
                            color=0x498fc9)
                        embed.set_thumbnail(url=thumbnail)
                        await message.channel.send(embed=embed)
                        await user.add_roles(muted)
                        await asyncio.sleep(5)
                        await user.remove_roles(muted)
                        done = True
                        print(f"{message.author} is done enchanting!!")
                        return
                except asyncio.TimeoutError:
                    await message.channel.send(f"Looks like you're done enchanting! "
                                               f"No longer tracking enchants for {mention}...")
                    print(f"{message.author} has error'd/timeout'd while enchanting!")
                    return
            print(f"{message.author} is done enchanting!!")
            return

        # Mat Calc
        if msg.startswith('craft'):
            parse = materials.parse_command(msg)
            if parse.get('error'):
                embed = discord.Embed(
                    title="Material Crafting Calculator",
                    color=0x498fc9
                )
                embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/753854031805284372.png?v=1")
                embed.add_field(name='Error', value=parse['error'], inline=False)
                await message.channel.send(embed=embed)
                return
            if parse.get('help'):
                embed = discord.Embed(
                    title="Material Crafting Calculator",
                    color=0x498fc9
                )
                embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/753854031805284372.png?v=1")
                embed.add_field(name='Help', value=parse['help'], inline=False)
                await message.channel.send(embed=embed)
                return

            def check(m):
                return m.author.id == erpg_bot_id

            embed = discord.Embed(
                title="Material Crafting Calculator",
                description=f'Type `rpg i` so I can check your current inventory.',
                color=0x498fc9
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/753854031805284372.png?v=1")
            await message.channel.send(embed=embed)
            found_inv = False
            while not found_inv:
                try:
                    response = await client.wait_for('message', check=check)
                    if len(response.embeds) <= 0:
                        continue
                    embed_dict = response.embeds[0].to_dict()
                    if embed_dict.get('name') and message.author not in embed_dict['name']:
                        continue
                    inventory = materials.parse_inventory(embed_dict)
                    found_inv = True
                    if 'fruitsalad' in parse['item']:
                        craft_dict = materials.calc_fruit_salad(inventory, parse)
                    else:
                        craft_dict = materials.calc_mats(inventory, parse)

                    if craft_dict.get('error'):
                        embed = discord.Embed(
                            title="Material Crafting Calculator",
                            color=0x498fc9
                        )
                        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/753854031805284372.png?v=1")
                        embed.add_field(name='Error', value=craft_dict['error'], inline=False)
                        await message.channel.send(embed=embed)
                        return
                    response = materials.parse_response(craft_dict)
                    embed = discord.Embed(
                        title="Material Crafting Calculator",
                        description=f'Inventory found for **{mention}**!',
                        color=0x498fc9
                    )
                    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/753854031805284372.png?v=1")
                    embed.add_field(name=f'**Craft the following:**', value=response, inline=False)
                    await message.channel.send(embed=embed)
                    return
                except asyncio.TimeoutError:
                    await message.channel.send("Could not find ERPG response for this enchant...")

        # D11 Simulator
        if message.content.lower().startswith('d11sim'):
            command_list = ['up',
                            'left',
                            'right',
                            'pass',
                            'attack',
                            'forfeit']
            nickname = message.author.name
            user = message.author
            channel = message.channel
            string = message.content.split(' ')
            if len(string) == 1:
                density = 50
            else:
                density = int(string[1])
            board_disp, board, hp = dungeon_init_eleven()
            boss = 2
            while boss > 0 and hp > 0:
                mydict = dungeon_dict_eleven(nickname, hp, boss, board_disp)
                myembed = discord.Embed.from_dict(mydict)
                if 'impossible' in board_disp:
                    await message.channel.send(board_disp)
                else:
                    await message.channel.send(embed=myembed)

                def check(m):
                    return m.content.lower() in command_list and m.author == user and m.channel == channel

                try:
                    msg = await client.wait_for('message', timeout=30.0, check=check)
                except asyncio.TimeoutError:
                    await channel.send(nickname + ' took too long to act!')
                    break
                else:
                    if msg.content.lower() == 'forfeit':
                        break
                    board_disp, board, hp, attack_flag = dungeon_update_eleven(msg.content, board, hp, density)
                    if attack_flag == 1:
                        boss = boss - 1
            if boss == 0:
                mydict = dungeon_dict_end_eleven(nickname, hp, boss, board_disp)
                myembed = discord.Embed.from_dict(mydict)
                myembed.set_footer(text=nickname + " has cleared dungeon 11.")
            else:
                hp = 0
                mydict = dungeon_dict_end_eleven(nickname, hp, boss, board_disp)
                myembed = discord.Embed.from_dict(mydict)
                myembed.set_footer(text=nickname + " is dead. Better luck next time!")
            await message.channel.send(embed=myembed)
            return

        # D14 Simulator
        if message.content.lower().startswith('d14sim'):
            command_list = ['up',
                            'left',
                            'right',
                            'down',
                            'pass',
                            'attack',
                            'forfeit']
            nickname = message.author.name
            user = message.author
            channel = message.channel
            state = 0
            dmg = 0
            boss = 2
            board_disp, board, hp, dragon, current_on = dungeon_init_fourteen()
            while boss > 0 and hp > 0:
                mydict = dungeon_dict_fourteen(nickname, hp, boss, board_disp, dmg, state)
                myembed = discord.Embed.from_dict(mydict)
                if 'impossible' in board_disp:
                    await message.channel.send(board_disp)
                else:
                    await message.channel.send(embed=myembed)

                def check(m):
                    return m.content.lower() in command_list and m.author == user and m.channel == channel

                try:
                    msg = await client.wait_for('message', timeout=30.0, check=check)
                except asyncio.TimeoutError:
                    await channel.send(nickname + ' took too long to act!')
                    break
                else:
                    if msg.content.lower() == 'forfeit':
                        break
                    board_disp, board, hp, state, dmg, attack_flag, current_on, dragon = dungeon_update_fourteen(
                        msg.content, board, hp, state, current_on, dragon)
                if attack_flag == 1:
                    boss = boss - 1
            if boss == 0:
                mydict = dungeon_dict_end_fourteen(nickname, hp, boss, board_disp)
                myembed = discord.Embed.from_dict(mydict)
                myembed.set_footer(text=nickname + " has cleared dungeon 14.")
            else:
                hp = 0
                mydict = dungeon_dict_end_fourteen(nickname, hp, boss, board_disp)
                myembed = discord.Embed.from_dict(mydict)
                myembed.set_footer(text=nickname + " is dead. Better luck next time!")
            await message.channel.send(embed=myembed)
            return

        # Embed Getter
        if msg.startswith('!get'):
            msg_id = msg.split(' ')[1]
            fetched = await message.channel.fetch_message(msg_id)
            if len(fetched.embeds) > 0:
                await message.channel.send(embed=fetched.embeds[0])
                # embed_dict = msg.embeds[0].to_dict()
                # for key, value in embed_dict.items():
                #     if key == 'fields':
                #         await message.channel.send("embed_dict['fields'][0]['value']")
                #         await message.channel.send(f"```{embed_dict['fields'][0]['value']}```")
                #     else:
                #         await message.channel.send(f"embed_dict['{key}']")
                #         await message.channel.send(f"```{embed_dict[key]}```")
            else:
                await message.channel.send(fetched)
            return
    except:
        e = sys.exc_info()
        print(f"Error for message from {message.author}: {message.content}"
              f"{e}")

@client.event
async def on_ready():
    print(f'Connected as {client.user.name} {client.user.id}')

client.run(TOKEN)