'''
Hand made (primitive version)
-Rism

M1P6 — Text Adventure (No prereq, for fun)
Rooms, descriptions, and choices stored in a JSON file you edit manually in VS Code.
Random encounter table also in the file — triggered as the player moves through rooms.
Simple health stat that changes based on encounters. Win/lose condition.
Adding new rooms or encounters only requires editing the JSON, no code changes.
'''
from pathlib import Path
import random,re,json,time,datetime,os

data_dir = Path.home() / 'projects'/ 'M1P6'
data_dir.mkdir(parents=True,exist_ok=True)

chest_encounters = data_dir / 'chest_encounters.json'
trap_room        = data_dir / 'trap_room.json'
random_encounter = data_dir / 'random_encounter.json'
monsters         = data_dir / 'monsters.json'
safe_rooms       = data_dir / 'safe_rooms.json'
boss_room        = data_dir / 'boss_room.json'
win_exit         = data_dir / 'win_exit.json'
items            = data_dir / 'items.json'

all_encounters = [chest_encounters, trap_room, random_encounter,monsters, safe_rooms, boss_room, win_exit]

def load_json(path):
    if path.exists():
        return json.loads(path.read_text())
    return {}

def save_json(path, data):
    path.write_text(json.dumps(data, indent=4))
    print(f"{path.name} saved.")

chest_encounters = load_json(chest_encounters)
trap_room = load_json(trap_room)
random_encounter = load_json(random_encounter)
monsters = load_json(monsters)
safe_rooms = load_json(safe_rooms)
boss_room = load_json(boss_room)
win_exit = load_json(win_exit)
items = load_json(items)

starting_messege = """THE BRANCHING HALLS
a corridor crawler
Every junction has two identical doors. Behind each waits a
monster, a trap, a chest, a fountain -- or nothing at all.
Reach the exit if you can."""


player_health = 500
def take_damage(num):
    global player_health
    print(f"Player took {num} damage")
    player_health -= num
    print(f"player health {player_health}")
    if player_health < 1:
        print("your journey ends here")
        death_screen()
    return

def death_screen():
    print("done didily dieded")
    pass
    exit()

min_attack = 35
max_attack = 50
def combat(monster_name,monster_pointer,monster_size):
    mhp = monster_pointer["hp"]
    mdmg = monster_pointer["dmg"]
    if monster_name != 'mimic':
        print(f"as the door slams shut you see a {monster_name} stands before you\nas you ready your sword the beast attacks")
    while mhp >0:
        pdmg = random.randint(min_attack,max_attack)
        mhp -= pdmg
        print(f"\nyou swing your sword dealing {pdmg} Damage!")
        if mhp <= 0:
            break
        print(f"\nthe beast has {mhp} Hp remaining\nThe beast stikes back")
        RNG = random.randint(25,mdmg)
        take_damage(RNG)
        _ = input("\n(press enter to attack)")
    print("\nYou deal the final blow, \nthen you search the corpse")
    item = roll_loot(monster_size)

#def advance_time():
    #global tick_time
    #tick_time -= 1


def room_gen():
    print('1')

def roll_loot(reward_type):
    global player_health,min_attack,max_attack
    all_items = items["all_items"]
    if reward_type == "chest":
        reward_type = random.choice(all_items)
        print(reward_type)
    if reward_type == "boss":
        #print(boss_room['victory'])
        print("as you catch your breath some of its essence flows ino you")
        max_attack += 25
        print('your max attack has increased too ',max_attack)
        return
    potion_type = reward_type + "_potion"
    #print(potion_type)
    _ = items["items"][potion_type]
    if _["category"] == "healing":
        print(f'You find a {_["name"]}')
        player_health += _["heal"]
        print("Your wounds begin to close \nHp",player_health)
        print(f'You restored {_["heal"]}Hp ')
        return
    min_max = potion_type[:3]
    if _["category"][:6] == f"attack":#_{min_max}:
        amount = _["attack_boost"]
        dual_name = _["name"]
        print(f"You find a {dual_name} as you drink \nYou feel invigorated and your {min_max} attack is increased")
        if _["category"] == "attack_max":
            max_attack += amount
            print("Your new Maximum attack is ",max_attack)
            return
        if _["category"] == "attack_min":
            min_attack += amount
            print("your new Minimum attack is ",min_attack)
            return
    else:
        print("You find a little piece of paper with a large 'IOU' printed on it")
        return

    #raise min_attack?
    #raise max_attack?
    #gain health potion

def chest_room():
    C_room = ['open', 'proceed']
    _ = chest_encounters
    print(_['single']['description'])
    choice = choice_helper(C_room,'do you \n[1] Open the chest\nOr\n[2] Play it safe and proceed to the next door\n')
    if choice == 'open':
        roll_loot("chest")
        print('after collecting your spoils you open the door behind it\nas')
    else:
        print('You decide better safe then sorry and open the door behind it\nas')

#description
#search_result
#trigger_text
#damage
#tick_drain
def trapped_room():
    P_or_S = ['proceed','search']
    T_room = trap_room["all_traps"]
    picked = random.choice(T_room)
    _ = trap_room[picked]
    print(_['description'])
    choice = choice_helper(P_or_S,'do you \n[1] Proceed \nOr\n[2] Play it safe and search the area first\n')
    if choice == 'proceed':
        take_damage(_['damage'])
        print(_['trigger_text'])
    if choice == 'search':
        print(_["search_result"])

def small_monster():
    kind = monsters["small"]
    names = kind.get("names",'ghost')
    mn = random.choice(names)
    combat(mn,kind,"small")

def health_fountan():
    global player_health,max_attack
    P_or_A = ['proceed','avoid']
    HF = safe_rooms["fountain"]
    print(HF['description'])
    choice = choice_helper(P_or_A,'do you \n[1] Proceed to the fountain and drink\nOr\n[2] Safely Avoid the fountain and proceed to the next door\n')
    if choice == 'proceed':
        print('you approach the fountain and drink')
        print(HF['drink_text'])
        if player_health < 500:
            player_health = 500
            print('Fully healed\nHp',player_health)
            return
        else:
            print('player already at full Hp, +10 Max attack instead')
            max_attack +=10
            return
    if choice == 'avoid':
        print('you pass the fountain and proceed to the next door\nas')
        return


def mimic_room():
    M_room = ['open','scan', 'proceed']
    _ = random_encounter
    print(_['mimic']['disguise_description'])#
    choice = choice_helper(M_room,'do you \n[1] Open the chest\n[2] Scan the enviorment \n[3] Play it safe and proceed to the next door\n')
    if choice == 'open':
        print(_['mimic']['ambush_text'])
        print('catching you off guard it gets a devistating hit in')
        take_damage(140)
    if choice == 'scan':
        print(_['mimic']['search_warning'])
        M_room2 = ['avoid','attack']
        choice2 = choice_helper(M_room2,'Do you\n[1] Avoid it and progress\nOr\n[2] Attack it\n')
        if choice2 == 'avoid':
            print('you decide to play it safe and avoid it \nas')
            return
        if choice2 == 'attack':
            print(_['mimic']['strike_first_text'])
    if choice == 'proceed':
        print('You decide better safe then sorry and open the door behind it\nas')
        return
    kind = monsters["mimic"]
    names = kind.get("names",'ghost')
    mn = random.choice(names)
    combat(mn,kind,"medium")

def medium_monster():
    kind = monsters["medium"]
    names = kind.get("names",'ghost')
    mn = random.choice(names)
    combat(mn,kind,"medium")

def dual_chests():
    DC_room = ['open','open', 'proceed']
    _ = chest_encounters
    print(_['dual']['description'])
    choice = choice_helper(DC_room,'do you \n[1] Open the left chest\n[2] Open the right chest\nOr\n[3] Play it safe and proceed to the next door\n')
    if choice == 'open':
        rng = random.randint(1,100)
        if rng > 35:
            roll_loot("chest")
            print('after collecting your spoils you notice the other chest has vanished, you open the door behind it\nas')
            return
        else:
            print('As you open the lid a gush of flames spit out from within it')
            take_damage(90)
            print('you stumble to the next door and open it without any eyebrows \nas')
            return
    else:
        print('You decide better safe then sorry and open the door behind it\nas')
        return

def large_monter():
    kind = monsters["large"]
    names = kind.get("names",'ghost')
    mn = random.choice(names)
    combat(mn,kind,"large")


def empty_room():
    all_items = items["all_items"]
    P_or_S = ['proceed','search']
    _ = safe_rooms
    rooms = _["loot_or_nothing"]
    room = random.choice(rooms)
    print(_[room]['description'])
    choice = choice_helper(P_or_S,'do you \n[1] Proceed \nOr\n[2] Search the area first\n')
    if choice == 'search':
        print(_[room]['search_result'])
        if room == 'search_find':
            roll_loot(random.choice(all_items))
    else:
        print('You decide to just pass through to open the door\nas')
        return


def boss_encounters():
    global player_health
    _ = boss_room
    print(_['intro'])
    kind = monsters["boss"]
    names = kind.get("names",'ghost')
    name = random.choice(names)
    combat(name,kind,"boss")
    print(_['reward_text'])
    if player_health < 500:
        player_health = 500
        print('hp',player_health)
        return
    else:
        print('you are already overhealed')
        return




def winner():
    _ = win_exit
    print(_["title"])
    print(_["text"])
    exit()


def seed_generator(dificulty):
    seed = []
    for i in range(dificulty[1]):
        seed.append(random.randint(10,98))
    seed.append(99)
    return seed

def choice_helper(helper_list,note):
    while True:
        try:
            value = helper_list[int(input(note))-1]
        except ValueError:
            print('invalid choice made try again')
            continue
        except IndexError:
            print('Invalid selection')
            continue
        return value

def dificulty_helper():
    dificulty = [['easy',20],['challenging',50],['hard',100]]
    for i,num in enumerate(dificulty,1):
        print(i,num[0])
    choice = choice_helper(dificulty,'enter the number to select dificulty\n')
    seed_run = seed_generator(choice)
    return seed_run


decision_room_note = '''\nyou see 2 identical doors ahead of you,
one on the right and one on the left\nWhich door do you enter?
[1]Left or [2]Right\n'''

options = ['left','right']
def primary_loop(seed):
    for i in range(len(seed)):
        if player_health <= 0:
            death_screen()
            return
        tmp_doors = str(seed[i])
        if tmp_doors == '99':
            winner()
            return
        print('the door locks shut behind you')
        if tmp_doors[0] != tmp_doors[-1]:
            choice = choice_helper(options,decision_room_note)
            if choice == 'left':
                door_pick(tmp_doors[0])
            if choice == 'right':
                door_pick(tmp_doors[-1])
        else:
            boss_encounters()

room_callout = [chest_room,
trapped_room,
small_monster,
health_fountan,
mimic_room,
trapped_room,
medium_monster,
dual_chests,
large_monter,
empty_room
]
def door_pick(num):
    room_function = room_callout[int(num)]
    room_function()

'''
0 = normal chest
1 = trap room
2 = small monster
3 = safe room with health fountan
4 = random encounter
5 = search room
6 = medium monster
7 = 2 chests random number for each if its number is 0-4 its safe above its trapped
8 = large monster
9 = safe room
'''



"start menu"
def start_game():
    print(starting_messege)
    print('first select dificulty')
    seed = dificulty_helper()
    print(seed)
    print('Entering the THE BRANCHING HALLS...')
    primary_loop(seed)

start_game()
print("Thanks for playing!")































'''
----------------------------------------------------------Brainstorm------------------------------------------------------------
map - branching hallway the left or right path numbers 10-98 generated difuculty is how many times(length of hallway) with the last pair being 99(exit)
combat block, attack different monsters have different attack patterns? such as 2-3 ticks before attack?

gameplay have a bar chr(9004)? as a time displayed when it reaches 0 loose?


********************************************************************************************************
Need to make:
generate a seed based on  40 digits ending in 99(exit), 60+ keep generating 40 digit chunks until a 99(exit)apears?, endless keep generating chunks to play

Core Loop:
    JSON loader / parser    <
    Main game loop
    Input router / parser
    Win / lose condition
    Player stats display (HUD)
    Event log, a rolling buffer of the last 5–8 actions displayed each turn

left or right one has a monster the other a trap or a door to progress, monster has chest to loot

0 = normal chest
1 = trap room
2 = small monster
3 = safe room with health fountan
4 = random encounter
5 = search room
6 = medium monster
7 = 2 chests random number for each if its number is 0-4 its safe above its trapped
8 = large monster
9 = safe room

2 of the same digits = Boss room
99 = win/end

Player enters room
Pull next digit(s) from sequence
Determine room type (safe/trap/monster/chest/boss/exit)
Display room description
If monster → combat loop
If safe → search option
If chest → loot
Display updated HUD
Ask for direction
Repeat

Maze Generation:
    digit sequence generator,40-easy garenteed exit,60-hard generated exit , no 99 generation endless
    easy digits 39 and 40 are 99 to exit, hard generates 60 digits
    Path direction assignment(low # = safe, high # = monster)
    Boss sequence for any pairs of numbers
    Exit injector(add 9 to the end of )
    Cleared room counter
    Index progression of the gennerated seed([0,1])first rooms/choices ([2,3]) second and so on
    Duplicate number handler(2 same = boss room)


Navigation:
    Direction display(show L / R )
    Random encounter trigger(fires on move)
    Room descriptions
    Search function
    Exit / turn around to then go to the other room
    once entering a room if theres a door to progress it locks behind the player

Combat:
    Monster type selector(6 types?)
    Combat loop
    Block attack
    Health
    Flee mechanic(time penalty + possible damage)

Items & Inventory:
    Item pickup function
    Chest / loot handler(triggered by 0 in sequence)
    Inventory
    Items (data)
    Use items

Boss / Rewards:
    Full heal on boss clear
    Time bonus on boss clear

need files for
chest,traped chest, dual chest

trap room fire,trap room spikes, trap room false fountain, trap room no exit
random encounter
monsters
safe rooms



# create all files with empty dicts — skips any that already exist
for path in all_encounters:
    if not path.exists():
        path.write_text(json.dumps({}, indent=4))
        print(f"Created: {path.name}")
    else:
        print(f"Already exists, skipping: {path.name}")




amount = int(input("how many seconds to countdown from: "))
time_bar = chr(9600)
def clear():
    os.system('cls')
print('Time start')
for i in range(amount, 0, -1):  # counts down from amount to 1
    print(time_bar * i + '\n'*10)
    #print(time_bar * i)
    time.sleep(0.1)
    clear()


shelved features for future return:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
map           - spinning maze/hallway? with different paths right left straight
gameplay loop - each room a monster or search function search has 3 levels quick skim, focus scan and check thoroughly
or random encounter, items to pickup and use for health dmg sheild or pause countdown?
combat loop   - block(parry)?, attack, action,time based

have a folder with paths assinged to a number randomly generate a maze number pull directions and rooms from file
randomly generate a number from 0-8, 42? times then another chunk of  18 with the last 3 being 999
left right straight with the lowest number being the correct path and the highest a monster
if the number is a 0 theres a chest to open and its the correct path, after 14? cleared rooms add a 9 as the exit condition number

once a 40 digit number from is generated
if numbers 123,234,345,456,567,678,789 appear its a boss room if cleared a full heal + time added + key for 3 of the same digit chest room encounter?

monster category 6 types?
bunch of random rooms / trap rooms

Maze Generation:
    40-digit sequence generator
    Path direction assignment(low # = safe, high # = monster)
    Boss sequence detector(123, 234 … 789 triggers boss)
    Exit injector(add 9 after 20 cleared rooms)
    Cleared room counter
    Index removal to progress(remove [0,1,2])
    Duplicate number handler(2 same, 3 same)
    Regex for room generation
    0 stays chest, 1–3 is a trap (damage,poison or time loss), 4–6 is safe, 7–8 is monster Makes the search more valuable

Navigation:
    Direction display(show L / R / straight)
    Random encounter trigger(fires on move)
    Room descriptions
    Search function(skim / scan / thorough)
    Exit / turn around

Combat:
    Monster type selector(6 types)
    Combat loop
    Block / parry system(Critical hit / parry window) after succsesfull parry crit
    Time system(countdown + action cost)
    Health
    Flee mechanic(time penalty + possible damage)
    Difficulty scaling?
    Difficulty modes?
    statusEffects array on the player and a tickEffects() poison,stun,slow,daze,weaken,burn?

Items & Inventory:
    Item pickup function
    Chest / loot handler(triggered by 0 in sequence)
    Inventory
    Items (data)
    Use items

Boss / Rewards:
    Key system(dropped by boss, used where?)
    Full heal on boss clear
    Time bonus on boss clear
    Shield / pause item logic

Add on's:
    Save/checkpoint system
    Score/leaderboard system
________________________________________________________________________________________________________




its action tick based or turn based to make the search function have some impact with an over arching (placeholder number) 1000 tick run time limit



yes after say a monster encounter progressing through the next progression door places the player in a separate room to then choose left or right again (the next instance of numbers) if by going through that progression door the next sequence is a number pair the boss fight begins if 99 freedom encounter executes



use the table, the low high was an old brainstorm idea



every action costs at least 1 'tick' of time more for some actions going through the progression door to the other room with choices (mentioned for the answer for question 2) then locks player is free to search both rooms at the cost of 'ticks' for the trap rooms and rooms in general player enters the door selected and is presented with a minor vague description of the room and progressing without searching activates the trap for monsters specifically after entering they are greeted with a monster who would have a varying 2tick?-5tick? attack sequence with proportional damage  with maybe an indicator as to its attack progression



difficulty easy as a 40 digit randomly generated number seed with a 99(exit) inject at the end, hard a 60 digit random seed(with no 99 pair) where every room after the main seed is a pair of random numbers generated until the 99 is generated and endless just keep generating number pairs maybe append them to a  variable showing statistics at the end



raw chaos may the RNG be in your favor



have the option to type a seed or generate one make sure minimum 40digits and check for no early 99 they could have all boss rooms if they typed it out that way



HP and DMG variables will take some testing to tune right have them in an easy spot to adjust as needed for now 500starting HP and DPH set to 30? increased with items potentially and or a chance of a critical hit? as for block its duration set to 2? ticks to give player time to line up monsters attack and block it blocking 70% of incoming damage with a 2? tick window after blocking before an action can be made to prevent repeat blocks if not timed right when an attack is successfully blocked it adds +5? ticks to the next monster attack allowing an attack chain with each attack taking 2 ticks wind up and attack if the player is hit during a wind up they are stunned for 3? ticks



HP and attack will take some balancing but for now small has 120HP deals 40DMG attacks fast 1-3Ticks but no player wind up interrupt, medium has 260HP deals 65DMG attacks 2-5 tick attacks, large has 330HP 80DMG attacks 3-6ticks, Boss has 500HP  120 dmg attacks 2-10ticks monsters drop loot only found if searched



fleeing lands you back into the decision room with the 2 doors to pick from with a chance to be attacked as you exit regardless of monster wind up bosses are locked doors no fleeing



starting time 1000? ticks will have to balance regular moving costs 1 tick any movement progression, combat ticks are mentioned in answers 8 and 9 flee costs a flat 5? boss clear grants +100? can find items that restore time time added on find



room search when in the decision room search just says there's 2 identical doors to choose from when entering a room you are either met with a monster or boss (which after slaying says something like the beast lay dead and you see a progression door if searched loots the beast ,or a room with a vague description depending on the room with the option to search for 8? ticks or proceed to the progression door if one is mentioned in the description potentially have the description mention the door and if a chest room say you spot a chest in the middle of the room with a progression door behind it random encounter have it as a mimic? for now have the search to guaranteed to find it/out if trapped and avoid them to progress 9 is the red herring its plain just an easy progression that would usually waste  search ticks with 5 being a search and find some loot behind a chair on some XYZ description of a text adventure room



for loot only stat boosts and healing items each chest rolled independently with search saying its a pair of chests both could be trapped or both have loot



each item use costs a tick opening the bag costs a tick(because healing during a fight) false fountain damages 75? instead of heals real fountains are a 1 time 200?heal with items ranging from small 25HP? medium 60hp? and large 140HP? similar to found tick time items and other varying single use items unlimited inventory



i will have you the generator and author you are free to take liberties with design's and features

before progressing to the creation is their any more questions for me?


'''






