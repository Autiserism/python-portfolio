'''
Global state with multiple variables
Write a program that tracks a simple game with three global variables —
player_health, player_gold and player_level.
Write functions to take_damage, earn_gold, spend_gold and level_up.
Each function should validate input, update globals, log the change and print a status update.
'''

import random, logging
logging.basicConfig(level=logging.DEBUG)

logging.disable(logging.CRITICAL)

player_health = 100
player_level = 0
player_gold = 10
player_exp = 0
fights_won = 0
rest_timer = 50

def take_damage():
    global player_health
    damage = random.randint(1, 99)
    print(f"Player took {damage} damage")
    logging.debug(f"{damage} amount of damage taken")
    player_health -= damage
    print(f"player health {player_health}")
    logging.debug(f"player health {player_health}")
    return

def earn_gold():
    global player_gold
    gold = random.randint(0, 5)
    player_gold += gold
    print(f"player earned {gold} Gold! \nYou now have {player_gold} Gold!")
    logging.debug(f"earned {gold} gold total gold now {player_gold}")
    return

def spend_gold():
    global player_gold, player_health
    choice = input("Medic: \n'would you like too restore 25 health for only 8 gold?' \n1. for yes, 2. for no\n")
    if choice == '1':
        if player_gold >= 8:
            player_gold -= 8
            player_health += 25
            print(f"Transaction complete player has {player_gold} Gold left and {player_health} health")
            logging.debug(f"health for gold, player gold {player_gold},health {player_health} ")
            return
        else:
            print("Not enough Gold enter the arena to earn more")
            logging.debug(f"not enough gold for health")
            return
    elif choice == '2':
        print('its your funneral')
    else:
        print("Medic: 'is all that fighting getting to you? its a yes or no question'")
        logging.debug("user appears to be concussed")
        return

def level_up():
    global player_health, player_level, player_exp
    player_level += 1
    player_exp -= 100
    print(f"You have leveled up to {player_level}")
    if player_health < 100:
        player_health = 100
        print(f"player health restored to full \nHP {player_health}")
        logging.debug(f"player health was restored to full 100")
    else:
        player_health += 30
        print(f"player health restored by 30 \nHP {player_health}")
        logging.debug(f"player health was restored by 30")
    return

def earn_exp():
    global player_exp
    exp_gain = random.randint(10, 60)
    player_exp += exp_gain
    print(f"player earned {exp_gain} exp")
    logging.debug(f"player earned {exp_gain} exp")
    return

def rest_to_full_hp():
    global rest_timer, player_health
    if player_health >=100:
        print("you are already at full health")
        return
    elif rest_timer >= 100 :
        rest_timer -= 100
        player_health = 100
        print(f"You Feel well rested Hp recoverd to {player_health}")
        logging.debug(f"restored hp{player_health} reduced rest timer{rest_timer}")
        return
    else:
        print("fight more to earn your rest")
        return

def earn_rest():
    global rest_timer
    rest_points = random.randint(1,40)
    print(f"you earned {rest_points} Rest points")
    rest_timer += rest_points
    return

print("Fight for your freedom! \nin the gladiator arena! \nMake it to level 50 to walk free!")
while True:
    if player_level >= 50:
            print(f"you are free you won {fights_won} fights")
            break
    try:
        choice = int(input("Choose \n1. Fight in the arena \n2. Visit the Medic \n3. Rest \n9. View all stats \n"))
        if choice == 1:
            take_damage()
            if player_health <= 0 :
                print(f"you dieded RIP in peace you made it to level {player_level}")
                logging.debug(f'guy funkin ded')
                break
            print("you emerge victorius!")
            earn_gold()
            earn_exp()
            earn_rest()
            fights_won += 1
            if player_exp >= 100:
                level_up()
            continue
        elif choice == 2:
            print(f"you have {player_gold} Gold")
            spend_gold()
            continue
        elif choice == 3:
            print(f"you have {rest_timer} rest points")
            rest_to_full_hp()
            continue
        elif choice == 9:
            print(f"""Current Stats
                Hp {player_health}
                Gold {player_gold}
                Level {player_level}
                {player_exp}% of the way to the next level
                Fights won {fights_won}
                Rest points {rest_timer}: need atleast 100 to rest
            """)
            continue
        else:
            print("choose between your only options")
            continue
    except ValueError:
        print("to the lions with you if you dont choose")
        continue

logging.disable(logging.CRITICAL)
































