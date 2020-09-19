from numpy import *

############################################
#
# msg_txt = emoji.demojize(message.content)
# msg_embed = message.embeds[0].to_dict()
#
############################################

############################################
#
# trhelper
#
############################################

def trhelper(msg_txt):
  if "the name of this fish" in msg_txt.lower():
    if ":normiefish:" in msg_txt.lower():
      response = 'Answer: **1**'
      return response
    if ":goldenfish:" in msg_txt.lower():
      response = 'Answer: **2**'
      return response
    if ":epicfish:" in msg_txt.lower():
      response = 'Answer: **3**'
      return response
  if "is this a" in msg_txt.lower():
    if "is this a **diamond**" in msg_txt.lower():
      if ":gem:" in msg_txt.lower():
        response = 'Answer: **Y**'
      else:
        response = 'Answer: **N**'
      return response
    if "is this a **four leaf clover**" in msg_txt.lower():
      if ":four_leaf_clover:" in msg_txt.lower():
        response = 'Answer: **Y**'
      else:
        response = 'Answer: **N**'
      return response
    if "is this a **coin**" in msg_txt.lower():
      if ":coin:" in msg_txt.lower():
        response = 'Answer: **Y**'
      else:
        response = 'Answer: **N**'
      return response
    if "is this a **dice**" in msg_txt.lower():
      if ":game_die:" in msg_txt.lower():
        response = 'Answer: **Y**'
      else:
        response = 'Answer: **N**'
      return response
    if "is this a **gift**" in msg_txt.lower():
      if ":gift:" in msg_txt.lower():
        response = 'Answer: **Y**'
      else:
        response = 'Answer: **N**'
      return response
  if "letter of" in msg_txt.lower():
    if ":banana:" in msg_txt.lower():
      if "**first**" in msg_txt.lower():
        response = 'Answer: **B**'
        return response
      if "**second**" in msg_txt.lower():
        response = 'Answer: **A**'
        return response
      if "**third**" in msg_txt.lower():
        response = 'Answer: **N**'
        return response
      if "**fourth**" in msg_txt.lower():
        response = 'Answer: **A**'
        return response
      if "**fifth**" in msg_txt.lower():
        response = 'Answer: **N**'
        return response
      if "**sixth**" in msg_txt.lower():
        response = 'Answer: **A**'
        return response
    if ":apple:" in msg_txt.lower():
      if "**first**" in msg_txt.lower():
        response = 'Answer: **A**'
        return response
      if "**second**" in msg_txt.lower():
        response = 'Answer: **P**'
        return response
      if "**third**" in msg_txt.lower():
        response = 'Answer: **P**'
        return response
      if "**fourth**" in msg_txt.lower():
        response = 'Answer: **L**'
        return response
      if "**fifth**" in msg_txt.lower():
        response = 'Answer: **E**'
        return response
  if "how many" in msg_txt.lower() and "do you see" in msg_txt.lower():
    if "how many <:woodenlog:" in msg_txt.lower():
      num = msg_txt.lower().count(":woodenlog:") - 1
      response = 'Answer: **' + str(num) + '**'
      return response
    if "how many <:epicwoodenlog:" in msg_txt.lower():
      num = msg_txt.lower().count(":epicwoodenlog:") - 1
      response = 'Answer: **' + str(num) + '**'
      return response
    if "how many <:superepicwoodenlog:" in msg_txt.lower():
      num = msg_txt.lower().count(":superepicwoodenlog:") - 1
      response = 'Answer: **' + str(num) + '**'
      return response
    if "how many <:megasuperepicwoodenlog:" in msg_txt.lower():
      num = msg_txt.lower().count(":megasuperepicwoodenlog:") - 1
      response = 'Answer: **' + str(num) + '**'
      return response
    if "how many <:hypermegasuperepicwoodenlog:" in msg_txt.lower():
      num = msg_txt.lower().count(":hypermegasuperepicwoodenlog:") - 1
      response = 'Answer: **' + str(num) + '**'
      return response
    if "how many <:ultramegasuperepicwoodenlog:" in msg_txt.lower():
      num = msg_txt.lower().count(":ultramegasuperepicwoodenlog:") - 1
      response = 'Answer: **' + str(num) + '**'
      return response
  if "in your inventory" in msg_txt.lower():
    response = 'Answer: **N**'
    return response

############################################
#
# d14_manual_solver_map(msg_txt)
# d14_manual_solver_id(msg_embed)
# dungeon_auto_solver(msg_embed)
#
############################################

def d14_manual_solver_map(msg_txt):
    D = d14read(msg_txt)
    current_on = 9
    stringsL, hpL = d14solveL(D,current_on)
    stringsR, hpR = d14solveR(D,current_on)
    response = '**Left Dragon**:\n'
    if hpL < 99999:
      response = response + 'Solution found: ' + stringsL + '\n' + 'Damage taken: '+ str(hpL)
    else:
      response = response + stringsL
    response = response + '\n' + '**Right Dragon**:\n'
    if hpR < 99999:
      response = response + 'Solution found: ' + stringsR + '\n' + 'Damage taken: '+ str(hpR)
    else:
      response = response + stringsR
    return response

def d14_manual_solver_id(msg_embed):
    if 'the godly dragon' in msg_embed['fields'][0]['name'].lower():
      if 'waiting for you' in msg_embed['fields'][0]['name'].lower():
        dung = msg_embed['fields'][0]['value']
      else:
        dung = msg_embed['fields'][1]['value']
      D = d14read(dung)
      current_on = 9
      stringsL, hpL = d14solveL(D,current_on)
      stringsR, hpR = d14solveR(D,current_on)
      response = '**Left Dragon**:\n'
      if hpL < 99999:
        response = response + 'Solution found: ' + stringsL + '\n' + 'Damage taken: '+ str(hpL)
      else:
        response = response + stringsL
      response = response + '\n' + '**Right Dragon**:\n'
      if hpR < 99999:
        response = response + 'Solution found: ' + stringsR + '\n' + 'Damage taken: '+ str(hpR)
      else:
        response = response + stringsR
      return response
    return 0

def dungeon_auto_solver(msg_embed):
    if 'room' in msg_embed['fields'][0]['name'].lower() or 'ultra-omega' in msg_embed['fields'][0]['name'].lower():
      str1 = msg_embed['fields'][0]['value'].split('\n')
      str2 = msg_embed['fields'][2]['value'].split('\n')
      r1 = int(''.join(i for i in str2[0] if i.isdigit()))
      r2 = int(''.join(i for i in str2[1] if i.isdigit()))
      room = [r1,r2]
      if 'question' in str1[0].lower():
        response = d13solve(str1[0],str1[2],str1[3],str1[4],room)
        return response
      else:
        response = d13solve(str1[5],str1[7],str1[8],str1[9],room)
      return response

    if 'the godly dragon' in msg_embed['fields'][0]['name'].lower():
      if 'waiting for you' in msg_embed['fields'][0]['name'].lower():
        dung = msg_embed['fields'][0]['value']
        current_on = 9
      else:
        dung = msg_embed['fields'][1]['value']
        current_on_txt = msg_embed['fields'][0]['value']
        len_txt = current_on_txt.split('\n')
        if 'poisoned (tier ii' in current_on_txt.lower():
            current_on = 1
        elif 'poisoned (tier i' in current_on_txt.lower():
            current_on = 2
        elif 'was cured from poison' in current_on_txt.lower() or len(len_txt) == 5:
            current_on = 3
        elif 'pushed to the bottom' in current_on_txt.lower():
            current_on = 4
        elif 'teleported' in current_on_txt.lower():
            current_on = 5
        elif 'was damaged by' in current_on_txt.lower():
            current_on = 6
        elif 'pushed' in current_on_txt.lower() and 'twice' in current_on_txt.lower():
            current_on = 7
        else:
            current_on = 9

      fd = dung.split('\n')
      dragon_info = ''.join([i for i in fd[0] if not i.isdigit()])
      dragon_info = ''.join([i for i in dragon_info if (i != '<' and i != '>')])
      dragon_info = dragon_info.split('::')
      
      if 'godly' in dragon_info[1].lower() and 'godly' in dragon_info[6].lower():
        D = d14read(dung)
        stringsL, hpL = d14solveL(D,current_on)
        D = d14read(dung)
        stringsR, hpR = d14solveR(D,current_on)
        if hpL < 99999 and hpR < 99999:
          if hpL < hpR:
            response = 'Solution found for left dragon: **' + stringsL + '**' + '\n' + 'Damage taken: '+ str(hpL)
          else:
            response = 'Solution found for right dragon: **' + stringsR + '**' + '\n' + 'Damage taken: '+ str(hpR)
          return response
        if hpL < 99999:
          response = 'Solution found for left dragon: **' + stringsL + '**' + '\n' + 'Damage taken: '+ str(hpL)
          return response
        if hpR < 99999:
          response = 'Solution found for right dragon: **' + stringsR + '**' + '\n' + 'Damage taken: '+ str(hpR)
          return response
        response = stringsL
        return response

      if 'godly' in dragon_info[1].lower() and 'brown' in dragon_info[6].lower():
        D = d14read(dung)
        stringsL, hpL = d14solveL(D,current_on)
        if hpL < 99999:
          response = 'Solution found for left dragon: **' + stringsL + '**' + '\n' + 'Damage taken: '+ str(hpL)
          return response
        response = stringsL
        return response

      if 'brown' in dragon_info[1].lower() and 'godly' in dragon_info[6].lower():
        D = d14read(dung)
        stringsR, hpR = d14solveR(D,current_on)
        if hpR < 99999:
          response = 'Solution found for right dragon: **' + stringsR + '**' + '\n' + 'Damage taken: '+ str(hpR)
          return response
        response = stringsR
        return response
    return 0

def d13solve(question,ans1,ans2,ans3,room):
    mat = [[4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [4,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0],
           [4,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0],
           [4,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0],
           [4,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [4,0,1,1,0,0,0,2,2,2,0,0,0,0,0,0],
           [4,0,0,2,2,0,0,0,2,2,0,0,0,0,0,0],
           [4,0,0,0,2,2,0,0,0,2,0,0,0,0,0,0],
           [4,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0],
           [4,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0],
           [4,0,0,0,0,0,0,2,3,3,0,0,0,0,0,0],
           [4,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0],
           [4,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0]]
    if room[0] > 15 or room [1] > 15:
        return 'Not an intended room, choose a random answer.'
    ans = mat[room[0]][room[1]]
    if ans == 0:
        return 'Not an intended room, choose a random answer.'
    if ans == 4:
        return 'Answer: **ATTACK**'
    if 'wooden log' in question.lower():
        if ans == 1:
            if 'yes' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'yes' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'yes' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if 'idk lol' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'idk lol' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'idk lol' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if 'idk lol' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'idk lol' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'idk lol' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'arcsin' in question.lower():
        if ans == 1:
            if '-5.31' in ans1.lower():
                return 'Answer: **LEFT**'
            if '-5.31' in ans2.lower():
                return 'Answer: **CENTER**'
            if '-5.31' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if '-0.26' in ans1.lower():
                return 'Answer: **LEFT**'
            if '-0.26' in ans2.lower():
                return 'Answer: **CENTER**'
            if '-0.26' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if '63.22' in ans1.lower():
                return 'Answer: **LEFT**'
            if '63.22' in ans2.lower():
                return 'Answer: **CENTER**'
            if '63.22' in ans3.lower():
                return 'Answer: **RIGHT**'
    if question.lower().endswith('hi'):
        if ans == 1:
            if '>w<' in ans1.lower():
                return 'Answer: **LEFT**'
            if '>w<' in ans2.lower():
                return 'Answer: **CENTER**'
            if '>w<' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if 'owo' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'owo' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'owo' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if ans1.lower().endswith('hi'):
                return 'Answer: **LEFT**'
            if ans2.lower().endswith('hi'):
                return 'Answer: **CENTER**'
            if ans3.lower().endswith('hi'):
                return 'Answer: **RIGHT**'
    if 'duel' in question.lower():
        if ans == 1:
            if 'pvp' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'pvp' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'pvp' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if 'fight' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'fight' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'fight' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if 'command' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'command' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'command' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'maximum level' in question.lower():
        if ans == 1:
            if '2147' in ans1.lower():
                return 'Answer: **LEFT**'
            if '2147' in ans2.lower():
                return 'Answer: **CENTER**'
            if '2147' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if '2389' in ans1.lower():
                return 'Answer: **LEFT**'
            if '2389' in ans2.lower():
                return 'Answer: **CENTER**'
            if '2389' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if '200' in ans1.lower():
                return 'Answer: **LEFT**'
            if '200' in ans2.lower():
                return 'Answer: **CENTER**'
            if '200' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'number am i' in question.lower():
        ans1 = int(''.join(i for i in ans1 if i.isdigit()))
        ans2 = int(''.join(i for i in ans2 if i.isdigit()))
        ans3 = int(''.join(i for i in ans3 if i.isdigit()))
        if ans == 1:
            if max([ans1,ans2,ans3]) == ans1:
                return 'Answer: **LEFT**'
            if max([ans1,ans2,ans3]) == ans2:
                return 'Answer: **CENTER**'
            if max([ans1,ans2,ans3]) == ans3:
                return 'Answer: **RIGHT**'
        if ans == 2:
            if ans1 > 10000 and ans1 < 200000:
                return 'Answer: **LEFT**'
            if ans2 > 10000 and ans2 < 200000:
                return 'Answer: **CENTER**'
            if ans3 > 10000 and ans3 < 200000:
                return 'Answer: **RIGHT**'
        if ans == 3:
            if ans1 < 10000:
                return 'Answer: **LEFT**'
            if ans2 < 10000:
                return 'Answer: **CENTER**'
            if ans3 < 10000:
                return 'Answer: **RIGHT**'
    if 'epic fish' in question.lower():
        if ans == 1:
            if '2+' in ans1.lower():
                return 'Answer: **LEFT**'
            if '2+' in ans2.lower():
                return 'Answer: **CENTER**'
            if '2+' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if 'river' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'river' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'river' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if '1+' in ans1.lower():
                return 'Answer: **LEFT**'
            if '1+' in ans2.lower():
                return 'Answer: **CENTER**'
            if '1+' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'coins do' in question.lower():
        ans1 = int(''.join(i for i in ans1 if i.isdigit()))
        ans2 = int(''.join(i for i in ans2 if i.isdigit()))
        ans3 = int(''.join(i for i in ans3 if i.isdigit()))
        if ans == 1:
            if ans1 == 250:
                return 'Answer: **LEFT**'
            if ans2 == 250:
                return 'Answer: **CENTER**'
            if ans3 == 250:
                return 'Answer: **RIGHT**'
        if ans == 2:
            if ans1 == 500:
                return 'Answer: **LEFT**'
            if ans2 == 500:
                return 'Answer: **CENTER**'
            if ans3 == 500:
                return 'Answer: **RIGHT**'
        if ans == 3:
            if ans1 == 0:
                return 'Answer: **LEFT**'
            if ans2 == 0:
                return 'Answer: **CENTER**'
            if ans3 == 0:
                return 'Answer: **RIGHT**'
    if 'training' in question.lower():
        if ans == 1:
            if '5' in ans1.lower():
                return 'Answer: **LEFT**'
            if '5' in ans2.lower():
                return 'Answer: **CENTER**'
            if '5' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if '4' in ans1.lower():
                return 'Answer: **LEFT**'
            if '4' in ans2.lower():
                return 'Answer: **CENTER**'
            if '4' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if '1' in ans1.lower():
                return 'Answer: **LEFT**'
            if '1' in ans2.lower():
                return 'Answer: **CENTER**'
            if '1' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'the cap' in question.lower():
        if ans == 1:
            if 'like' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'like' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'like' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if '10' in ans1.lower():
                return 'Answer: **LEFT**'
            if '10' in ans2.lower():
                return 'Answer: **CENTER**'
            if '10' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if 'none' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'none' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'none' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'cookies' in question.lower():
        ans1 = int(''.join(i for i in ans1 if i.isdigit()))
        ans2 = int(''.join(i for i in ans2 if i.isdigit()))
        ans3 = int(''.join(i for i in ans3 if i.isdigit()))
        lowest = min([ans1,ans2,ans3])
        if ans == 1:
            if ans1 == lowest:
                return 'Answer: **LEFT**'
            if ans2 == lowest:
                return 'Answer: **CENTER**'
            if ans3 == lowest:
                return 'Answer: **RIGHT**'
        if ans == 2:
            if ans1 == lowest+1:
                return 'Answer: **LEFT**'
            if ans2 == lowest+1:
                return 'Answer: **CENTER**'
            if ans3 == lowest+1:
                return 'Answer: **RIGHT**'
        if ans == 3:
            if ans1 == lowest+2:
                return 'Answer: **LEFT**'
            if ans2 == lowest+2:
                return 'Answer: **CENTER**'
            if ans3 == lowest+2:
                return 'Answer: **RIGHT**'
    if 'minimum level' in question.lower():
        if ans == 1:
            if '20' in ans1.lower():
                return 'Answer: **LEFT**'
            if '20' in ans2.lower():
                return 'Answer: **CENTER**'
            if '20' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if '22' in ans1.lower():
                return 'Answer: **LEFT**'
            if '22' in ans2.lower():
                return 'Answer: **CENTER**'
            if '22' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if '24' in ans1.lower():
                return 'Answer: **LEFT**'
            if '24' in ans2.lower():
                return 'Answer: **CENTER**'
            if '24' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'vehicles' in question.lower():
        if ans == 1:
            if '2' in ans1.lower():
                return 'Answer: **LEFT**'
            if '2' in ans2.lower():
                return 'Answer: **CENTER**'
            if '2' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if '1' in ans1.lower():
                return 'Answer: **LEFT**'
            if '1' in ans2.lower():
                return 'Answer: **CENTER**'
            if '1' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if 'what' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'what' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'what' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'solo dungeon' in question.lower():
        if ans == 1:
            if 'yes' in ans1.lower():
                return 'Answer: **LEFT**'
            if 'yes' in ans2.lower():
                return 'Answer: **CENTER**'
            if 'yes' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 2:
            if '12' in ans1.lower():
                return 'Answer: **LEFT**'
            if '12' in ans2.lower():
                return 'Answer: **CENTER**'
            if '12' in ans3.lower():
                return 'Answer: **RIGHT**'
        if ans == 3:
            if '11' in ans1.lower():
                return 'Answer: **LEFT**'
            if '11' in ans2.lower():
                return 'Answer: **CENTER**'
            if '11' in ans3.lower():
                return 'Answer: **RIGHT**'
    if 'have passed' in question.lower():
        ans1 = int(''.join(i for i in ans1 if i.isdigit()))
        ans2 = int(''.join(i for i in ans2 if i.isdigit()))
        ans3 = int(''.join(i for i in ans3 if i.isdigit()))
        lowest = min([ans1,ans2,ans3])
        highest = max([ans1,ans2,ans3])
        if ans == 1:
            if ans1 < highest and ans1 > lowest:
                return 'Answer: **LEFT**'
            if ans2 < highest and ans1 > lowest:
                return 'Answer: **CENTER**'
            if ans2 < highest and ans1 > lowest:
                return 'Answer: **RIGHT**'
        if ans == 2:
            if ans1 == lowest:
                return 'Answer: **LEFT**'
            if ans2 == lowest:
                return 'Answer: **CENTER**'
            if ans3 == lowest:
                return 'Answer: **RIGHT**'
        if ans == 3:
            if ans1 == highest:
                return 'Answer: **LEFT**'
            if ans2 == highest:
                return 'Answer: **CENTER**'
            if ans3 == highest:
                return 'Answer: **RIGHT**'

def d14read(fd):
    fd = ''.join([i for i in fd if not i.isdigit()])
    fd = ''.join([i for i in fd if (i != '<' and i != '>')])
    fd = fd.split('\n')
    
    D = zeros((7,8))
    for i in range(1,8):
        for j in range(1,9):
            C = fd[i].split('::')
            if 'orange' in C[j-1]:
                D[i-1][j-1] = 1
            if 'yellow' in C[j-1]:
                D[i-1][j-1] = 2
            if 'green' in C[j-1]:
                D[i-1][j-1] = 3
            if 'purple' in C[j-1]:
                D[i-1][j-1] = 4
            if 'brown' in C[j-1]:
                D[i-1][j-1] = 5
            if 'red' in C[j-1]:
                D[i-1][j-1] = 6
            if 'blue' in C[j-1]:
                D[i-1][j-1] = 7
            if 'omega' in C[j-1].lower():
                D[i-1][j-1] = 9
    return(D)

def board_update(D,pos):
    U = D+1
    ind = (U==8).nonzero()
    U[ind] = 1
    x = pos[0]
    y = pos[1]
    U[x][y] = D[x][y]
    
    init = (D==9).nonzero()
    if init[0].size > 0:
      U[init] = 9  
    return U

def damage(tile,state):
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
        st = 6

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
        st = 3

    if tile == 3:
        dmg = 0
        st = 0

    if tile == 6:
        if state == 0:
            dmg = 244
            st = 0
        if state == 1:
            dmg = 244
            st = 0
        if state == 2:
            dmg = 278
            st = 1
        if state == 3:
            dmg = 278
            st = 2
        if state == 4:
            dmg = 244
            st = 0
        if state == 5:
            dmg = 332
            st = 4
        if state == 6:
            dmg = 332
            st = 5
    result = [dmg,st]
    return result

def d14solve(D,current_on):
    D_init = D
    init = (D_init==9).nonzero()
    x = int(''.join(map(str,init[0])))
    y = int(''.join(map(str,init[1])))
    init = [x,y]
    hp_now = 99999
    sol = 'No solution found, keep moving around.'

    if current_on != 9:
      D_init[x][y] = current_on
    
    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while (pos[0]!=0 or pos[1]!=1) and (pos[0]!=0 or pos[1]!=6):
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and D[x-1][y]<4:
            x = x-1
            direction = 'UP '
        else:
            if y>0 and D[x][y-1]<4:
                y = y-1
                direction = 'LEFT '
            else:
                if y<7 and D[x][y+1]<4:
                    y = y+1
                    direction = 'RIGHT '
                else:
                    if x<6 and D[x+1][y]<4:
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)

    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while (pos[0]!=0 or pos[1]!=1) and (pos[0]!=0 or pos[1]!=6):
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and D[x-1][y]<4:
            x = x-1
            direction = 'UP '
        else:
            if y<7 and D[x][y+1]<4:
                y = y+1
                direction = 'RIGHT '
            else:
                if y>0 and D[x][y-1]<4:
                    y = y-1
                    direction = 'LEFT '
                else:
                    if x<6 and D[x+1][y]<4:
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)

    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while (pos[0]!=0 or pos[1]!=1) and (pos[0]!=0 or pos[1]!=6):
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and (D[x-1][y]<4 or D[x-1][y]==6):
            x = x-1
            direction = 'UP '
        else:
            if y>0 and (D[x][y-1]<4 or D[x][y-1]==6):
                y = y-1
                direction = 'LEFT '
            else:
                if y<7 and (D[x][y+1]<4 or D[x][y+1]==6):
                    y = y+1
                    direction = 'RIGHT '
                else:
                    if x<6 and (D[x+1][y]<4 or D[x+1][y]==6):
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)
    
    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while (pos[0]!=0 or pos[1]!=1) and (pos[0]!=0 or pos[1]!=6):
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and (D[x-1][y]<4 or D[x-1][y]==6):
            x = x-1
            direction = 'UP '
        else:
            if y<7 and (D[x][y+1]<4 or D[x][y+1]==6):
                y = y+1
                direction = 'RIGHT '
            else:
                if y>0 and (D[x][y-1]<4 or D[x][y-1]==6):
                    y = y-1
                    direction = 'LEFT '
                else:
                    if x<6 and (D[x+1][y]<4 or D[x+1][y]==6):
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)
    
    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'
          
    return sol, hp_now

def d14solveL(D,current_on):
    D_init = D
    init = (D_init==9).nonzero()
    x = int(''.join(map(str,init[0])))
    y = int(''.join(map(str,init[1])))
    init = [x,y]
    hp_now = 99999
    sol = 'No solution found, keep moving around.'

    if current_on != 9:
      D_init[x][y] = current_on

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while pos[0]!=0 or pos[1]!=1:
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and D[x-1][y]<4:
            x = x-1
            direction = 'UP '
        else:
            if y>0 and D[x][y-1]<4:
                y = y-1
                direction = 'LEFT '
            else:
                if y<7 and D[x][y+1]<4:
                    y = y+1
                    direction = 'RIGHT '
                else:
                    if x<6 and D[x+1][y]<4:
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)

    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while pos[0]!=0 or pos[1]!=1:
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and D[x-1][y]<4:
            x = x-1
            direction = 'UP '
        else:
            if y<7 and D[x][y+1]<4:
                y = y+1
                direction = 'RIGHT '
            else:
                if y>0 and D[x][y-1]<4:
                    y = y-1
                    direction = 'LEFT '
                else:
                    if x<6 and D[x+1][y]<4:
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)

    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while pos[0]!=0 or pos[1]!=1:
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and (D[x-1][y]<4 or D[x-1][y]==6):
            x = x-1
            direction = 'UP '
        else:
            if y>0 and (D[x][y-1]<4 or D[x][y-1]==6):
                y = y-1
                direction = 'LEFT '
            else:
                if y<7 and (D[x][y+1]<4 or D[x][y+1]==6):
                    y = y+1
                    direction = 'RIGHT '
                else:
                    if x<6 and (D[x+1][y]<4 or D[x+1][y]==6):
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)
    
    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while pos[0]!=0 or pos[1]!=1:
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and (D[x-1][y]<4 or D[x-1][y]==6):
            x = x-1
            direction = 'UP '
        else:
            if y<7 and (D[x][y+1]<4 or D[x][y+1]==6):
                y = y+1
                direction = 'RIGHT '
            else:
                if y>0 and (D[x][y-1]<4 or D[x][y-1]==6):
                    y = y-1
                    direction = 'LEFT '
                else:
                    if x<6 and (D[x+1][y]<4 or D[x+1][y]==6):
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)
    
    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    return sol, hp_now

def d14solveR(D,current_on):
    D_init = D
    init = (D_init==9).nonzero()
    x = int(''.join(map(str,init[0])))
    y = int(''.join(map(str,init[1])))
    init = [x,y]
    hp_now = 99999
    sol = 'No solution found, keep moving around.'

    if current_on != 9:
      D_init[x][y] = current_on

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while pos[0]!=0 or pos[1]!=6:
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and D[x-1][y]<4:
            x = x-1
            direction = 'UP '
        else:
            if y>0 and D[x][y-1]<4:
                y = y-1
                direction = 'LEFT '
            else:
                if y<7 and D[x][y+1]<4:
                    y = y+1
                    direction = 'RIGHT '
                else:
                    if x<6 and D[x+1][y]<4:
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)

    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while pos[0]!=0 or pos[1]!=6:
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and D[x-1][y]<4:
            x = x-1
            direction = 'UP '
        else:
            if y<7 and D[x][y+1]<4:
                y = y+1
                direction = 'RIGHT '
            else:
                if y>0 and D[x][y-1]<4:
                    y = y-1
                    direction = 'LEFT '
                else:
                    if x<6 and D[x+1][y]<4:
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)

    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while pos[0]!=0 or pos[1]!=6:
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and (D[x-1][y]<4 or D[x-1][y]==6):
            x = x-1
            direction = 'UP '
        else:
            if y>0 and (D[x][y-1]<4 or D[x][y-1]==6):
                y = y-1
                direction = 'LEFT '
            else:
                if y<7 and (D[x][y+1]<4 or D[x][y+1]==6):
                    y = y+1
                    direction = 'RIGHT '
                else:
                    if x<6 and (D[x+1][y]<4 or D[x+1][y]==6):
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)
    
    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    D = D_init
    pos = init
    path = ''
    st = []
    fail = 0
    while pos[0]!=0 or pos[1]!=6:
        x = pos[0]
        y = pos[1]
        pos_old = pos
        if x>0 and (D[x-1][y]<4 or D[x-1][y]==6):
            x = x-1
            direction = 'UP '
        else:
            if y<7 and (D[x][y+1]<4 or D[x][y+1]==6):
                y = y+1
                direction = 'RIGHT '
            else:
                if y>0 and (D[x][y-1]<4 or D[x][y-1]==6):
                    y = y-1
                    direction = 'LEFT '
                else:
                    if x<6 and (D[x+1][y]<4 or D[x+1][y]==6):
                        x = x+1
                        direction = 'DOWN '
        pos = [x,y]
        if pos == pos_old:
            fail = 1
            break
        path = path+direction
        st = append(st,D[x][y])
        D = board_update(D,pos)
    
    if fail == 0:
        hp = 0
        state = 0
        for k in st:
            result = damage(k,state)
            hp = hp+result[0]
            state = result[1]
        if hp < hp_now:
          hp_now = hp
          sol = path + 'ATTACK'

    return sol, hp_now
