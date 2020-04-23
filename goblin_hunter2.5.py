import random
import time
diff2 = 0
start = True
while start:
    diff = input("Enter Difficulty: Normal , Hard , Brutal ").upper()
    if diff == "NORMAL":
        start = False
    elif diff == "HARD":
        diff2 = 7
        start = False
    elif diff == "BRUTAL":
        diff2 = 14
        start = False
    else:
        print("Input Error try again.")
weapon_damage = 0
player_coins = 10 + (diff2 * 1.5)
health = 100
attack = 10

drag_dam = 30 + (diff2 * .7)
drag_hp = 50 + (diff2 * 1.2)
mob_list = [" Goblin ", "Skeleton", " Spider ", "Werewolf"]
bio_list = ["Cave", "Den", "Camp", "Fortress", "Castle"]

mob1 = mob_list[random.randrange(1, 4)]
mob2 = mob_list[random.randrange(1, 4)]
mob3 = mob_list[random.randrange(1, 4)]
mob4 = mob_list[random.randrange(1, 4)]
mob5 = mob_list[random.randrange(1, 4)]
mob6 = mob_list[random.randrange(1, 4)]

bio1 = bio_list[random.randrange(1, 5)]
bio2 = bio_list[random.randrange(1, 5)]
bio3 = bio_list[random.randrange(1, 5)]
bio4 = bio_list[random.randrange(1, 5)]
bio5 = bio_list[random.randrange(1, 5)]# Goblin Hunter 2.5.5

import random
import time

# Difficulty Settings
diff2 = 0
start = True
while start:
    diff = input("Enter Difficulty: Normal , Hard , Brutal ").upper()
    if diff == "NORMAL":
        start = False
    elif diff == "HARD":
        diff2 = 7
        start = False
    elif diff == "BRUTAL":
        diff2 = 14
        start = False
    else:
        print("Input Error try again.")
weapon_damage = 0
player_coins = 10 + (diff2 * 1.5)
health = 100
attack = 10

drag_dam = 30 + (diff2 * .7)
drag_hp = 50 + (diff2 * 1.2)
# Randomized Monsters and Locations
mob_list = [" Goblin ", "Skeleton", " Spider ", "Werewolf"]
bio_list = ["Cave", "Den", "Camp", "Fortress", "Castle"]

# Semi-Randomized damages/health of monsters
mob1 = mob_list[random.randrange(1, 4)]
mob2 = mob_list[random.randrange(1, 4)]
mob3 = mob_list[random.randrange(1, 4)]
mob4 = mob_list[random.randrange(1, 4)]
mob5 = mob_list[random.randrange(1, 4)]
mob6 = mob_list[random.randrange(1, 4)]

bio1 = bio_list[random.randrange(1, 5)]
bio2 = bio_list[random.randrange(1, 5)]
bio3 = bio_list[random.randrange(1, 5)]
bio4 = bio_list[random.randrange(1, 5)]
bio5 = bio_list[random.randrange(1, 5)]
bio6 = bio_list[random.randrange(1, 5)]

mob_hp1 = random.randrange(30, 40) + diff2
mob_hp2 = random.randrange(30, 40) + diff2
mob_hp3 = random.randrange(32, 40) + (diff2 * 1.5)
mob_hp4 = random.randrange(32, 40) + (diff2 * 1.5)
mob_hp5 = random.randrange(42, 48) + (diff2 * 1.8)
mob_hp6 = random.randrange(42, 48) + (diff2 * 1.8)

dam1 = random.randrange(10, 15) + diff2
dam2 = random.randrange(10, 15) + diff2
dam3 = random.randrange(12, 18) + diff2
dam4 = random.randrange(12, 18) + diff2
dam5 = random.randrange(15, 20) + diff2
dam6 = random.randrange(15, 20) + diff2


def shop(player_coins1, health1, attack1, weapon_damage1):
    # Shop Program/ Traveling merchant
    shop1 = True
    while shop1:
        merchant = input("You stumble across a traveling merchant. What will you do?\n\nShop\nLeave\n").upper()

        if merchant == "SHOP":
            print("\n\n\n\n\n\n\n\n\n\nBrowse my wares sir!")

            print(" _____________________________________________________________________________")
            print("|     PLAYER COINS:", player_coins1, "                                                |")
            print("|                                                                             |")
            print("|     [1] Minor Health Potion   +10hp: 7$                                     |")
            print("|     [2] Greater Health Potion +20hp: 12$                                    |")
            print("|     [3] Small Dagger          +5dmg: 10$                                    |")
            print("|     [4] Elvin Sword           +7dmg: 15$                                    |")
            print("|     [5] Claymore             +10dmg: 20$                                    |")
            print("|     [6] Diamond Sword        +15dmg: 35$                                    |")
            print("|     [7] Enchanted Sword      +20dmg: 45$                                    |")
            print("|     [8] Attack Potion    +5 PermDMG: 20$                                    |")
            print("|     [9] Mega Potion           +40hp: 22$                                    |")
            print("|                                                                             |")
            print("|                                                                             |")
            print("|                                                                             |")
            print("|                                                                             |")
            print("|_____________________________________________________________________________|")
            print("Type 'EXIT' to exit shop")
            item = input("What would you like to purchase?\n").upper()
            if item == "EXIT":
                shop1 = False
            elif (item == "1") and (player_coins1 >= 7):
                health1 += 10
                player_coins1 -= 7
                print("Your health is now", health1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "2" and (player_coins1 >= 12):
                health1 += 20
                player_coins1 -= 12
                print("Your health is now", health1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "3" and (player_coins1 >= 10):
                del weapon_damage1
                weapon_damage1 = 5
                player_coins1 -= 10
                print("Your attack damage is now", weapon_damage1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "4" and (player_coins1 >= 15):
                del weapon_damage1
                weapon_damage1 = 7
                player_coins1 -= 15
                print("Your attack damage is now", weapon_damage1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "5" and (player_coins1 >= 20):
                del weapon_damage1
                weapon_damage1 = 10
                player_coins1 -= 20
                print("Your attack damage is now", weapon_damage1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "6" and (player_coins1 >= 35):
                del weapon_damage1
                weapon_damage1 = 15
                player_coins1 -= 35
                print("Your attack damage is now", weapon_damage1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "7" and (player_coins1 >= 45):
                del weapon_damage1
                weapon_damage1 = 20
                player_coins1 -= 45
                print("Your attack damage is now", weapon_damage1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "8" and (player_coins1 >= 20):
                attack1 += 5
                player_coins1 -= 20
                print("Your attack is now", attack1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif (item == "9") and (player_coins1 >= 22):
                health1 += 40
                player_coins1 -= 22
                print("Your health is now", health1, "points\n")
                print("You now have", player_coins1, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            else:
                input("ERROR PRESS ENTER TO CONTINUE\n")
        elif merchant == "LEAVE":
            shop1 = False
    return [weapon_damage1, health1, player_coins1]


def combat(health2, attack2, mob, dam, mob_hp, weapon_damage2, player_coins2):
    # Combat Program, Compares two random numbers 0-10 and chooses who attacks first

    mob_roll = random.randrange(0, 10)
    player_roll = random.randrange(0, 10)

    player_turn = True
    while player_turn:
        player_attack = attack2 + random.randrange(0, 7) + weapon_damage2
        mob_dam = dam + random.randrange(0, 7)

        if player_roll > mob_roll:

            mob_hp -= player_attack

            input("Press Enter to Continue")

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(" _____________________________________________________________________________")
            print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health2),
                  "]                  |")
            print("|  ____________________________________     |\             //                 |")
            print("| |    You did", player_attack, "points of damage!     |   \ \           _!_                 |")
            print("| |                                     |    \ \         /___\                |")
            print("| |                                     |     \ \        [+++]                |")
            print("| |_____________________________________|      \ \    _ _\^^^/_ _             |")
            print("|                                               \ \/ (    '-'  ( )            |")
            print("|                                                 /( \/ | {&}   /\ \          |")
            print("|                                                   \  / \     / _> )         |")
            print("|                                                    *` > ::: ; -'`""'- .       |")
            print("|                                                        /:::/         \      |")
            print("|                                                       /  /||   {&}   |      |")
            print("|                                                      (  / (\         /      |")
            print("|                                                      / /   \ -.___.-'       |")
            print("|                                                    _/ /     \ \             |")
            print("|                                                   /___|    /___|            |")
            print("|_____________________________________________________________________________|")
            if health2 <= 0:
                print("GAME OVER")
                exit()
            if mob_hp <= 0:
                player_turn = False
            else:
                health2 -= mob_dam

                input("Press Enter to Continue")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print(" _____________________________________________________________________________")
                print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health2),
                      "]                  |")
                print("|  ____________________________________     |\             //                 |")
                print("| |                                     |   \ \           _!_                 |")
                print("| |      The " + mob + " hit you for", mob_dam, "   |    \ \         /___\                |")
                print("| |          points of damage!          |     \ \        [+++]                |")
                print("| |_____________________________________|      \ \    _ _\^^^/_ _             |")
                print("|                                               \ \/ (    '-'  ( )            |")
                print("|                                                 /( \/ | {&}   /\ \          |")
                print("|                                                   \  / \     / _> )         |")
                print("|                                                    *` > ::: ; -'`""'- .       |")
                print("|                                                        /:::/         \      |")
                print("|                                                       /  /||   {&}   |      |")
                print("|                                                      (  / (\         /      |")
                print("|                                                      / /   \ -.___.-'       |")
                print("|                                                    _/ /     \ \             |")
                print("|                                                   /___|    /___|            |")
                print("|_____________________________________________________________________________|")
                if health2 <= 0:
                    print("GAME OVER")
                    exit()
                if mob_hp <= 0:
                    player_turn = False

        else:
            if health2 <= 0:
                print("GAME OVER")
                exit()
            if mob_hp <= 0:
                player_turn = False
            health2 -= mob_dam

            input("Press Enter to Continue")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(" _____________________________________________________________________________")
            print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health2), "]           |")
            print("|  ____________________________________     |\             //                 |")
            print("| |                                     |   \ \           _!_                 |")
            print("| |      The " + mob + " hit you for", mob_dam, "   |    \ \         /___\                |")
            print("| |          points of damage!          |     \ \        [+++]                |")
            print("| |_____________________________________|      \ \    _ _\^^^/_ _             |")
            print("|                                               \ \/ (    '-'  ( )            |")
            print("|                                                 /( \/ | {&}   /\ \          |")
            print("|                                                   \  / \     / _> )         |")
            print("|                                                    *` > ::: ; -'`""'- .       |")
            print("|                                                        /:::/         \      |")
            print("|                                                       /  /||   {&}   |      |")
            print("|                                                      (  / (\         /      |")
            print("|                                                      / /   \ -.___.-'       |")
            print("|                                                    _/ /     \ \             |")
            print("|                                                   /___|    /___|            |")
            print("|_____________________________________________________________________________|")
            if health2 <= 0:
                print("GAME OVER")
                exit()
            if mob_hp <= 0:
                player_turn = False

            else:
                mob_hp -= player_attack

                input("Press Enter to Continue")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print(" _____________________________________________________________________________")
                print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health2),
                      "]                      |")
                print("|  ____________________________________     |\             //                 |")
                print("| |    You did", player_attack, "points of damage!     |   \ \           _!_                 |")
                print("| |                                     |    \ \         /___\                |")
                print("| |                                     |     \ \        [+++]                |")
                print("| |_____________________________________|      \ \    _ _\^^^/_ _             |")
                print("|                                               \ \/ (    '-'  ( )            |")
                print("|                                                 /( \/ | {&}   /\ \          |")
                print("|                                                   \  / \     / _> )         |")
                print("|                                                    *` > ::: ; -'`""'- .       |")
                print("|                                                        /:::/         \      |")
                print("|                                                       /  /||   {&}   |      |")
                print("|                                                      (  / (\         /      |")
                print("|                                                      / /   \ -.___.-'       |")
                print("|                                                    _/ /     \ \             |")
                print("|                                                   /___|    /___|            |")
                print("|_____________________________________________________________________________|")
                if health2 <= 0:
                    print("GAME OVER")
                    exit()
                if mob_hp <= 0:
                    player_turn = False

    print(mob.upper() + " Defeated!")
    random_coins = random.randrange(12, 17) + (diff2 * 2)
    player_coins2 += random_coins
    print("You receive", random_coins, "coins!\nYou now have", player_coins2, "total coins!")
    input("Press Enter to continue.")
    return health2, player_coins2


def scene(health3, attack3, mob, bio, dam, mob_hp, weapon_damage3, player_coins3):
    # Initializes the next combat scene

    print("You arrive at the " + mob, bio)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" _____________________________________________________________________________")
    print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health3), "]                  |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                    [You arrive at the " + mob, bio + "]                      |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                     [Press Enter to Start Combat]                           |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|_____________________________________________________________________________|")
    list10 = combat(health3, attack3, mob, dam, mob_hp, weapon_damage3, player_coins3)
    return list10


# Start Screen of Game

input("Press Enter to Start Program")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|     ______      __    ___          __  __            __               ___   |")
print("|    / ____/___  / /_  / (_)___     / / / /_  ______  / /____  _____   |__ \  |")
print("|   / / __/ __ \/ __ \/ / / __ \   / /_/ / / / / __ \/ __/ _ \/ ___/   __/ /  |")
print("|  / /_/ / /_/ / /_/ / / / / / /  / __  / /_/ / / / / /_/  __/ /      / __/   |")
print("|  \____/\____/_.___/_/_/_/ /_/  /_/ /_/\__,_/_/ /_/\__/\___/_/      /____/   |")
print("|                                                                             |")
print("|                          [Press Enter to Begin]                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")
input()

# For Choosing which initial buff you want to select.

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|   |\             //                 [Health:", health, "]                          |")
print("|   \ \           _!_                 [Attack Damage:", attack, "]                    |")
print("|    \ \         /___\                                                        |")
print("|     \ \        [+++]                ______________________________          |")
print("|      \ \    _ _\^^^/_ _             | [What god do you worship?]  |         |")
print("|       \ \/ (    '-'  ( )            |                             |         |")
print("|         /( \/ | {&}   /\ \          |God of War: +5 Attack Damage |         |")
print("|           \  / \     / _> )         |God of Vitality: +25 Health  |         |")
print("|            *` > ::: ; -'`""'- .       |_____________________________|         |")
print("|                /:::/         \                                              |")
print("|               /  /||   {&}   |                                              |")
print("|              (  / (\         /                                              |")
print("|              / /   \ -.___.-'                                               |")
print("|            _/ /     \ \                                                     |")
print("|           /___|    /___|                                                    |")
print("|_____________________________________________________________________________|")
god = True
while god:
    god_choice = input("Type 'WAR' or 'VITALITY'\n").upper()
    if god_choice == "WAR":
        attack += 5
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(" _____________________________________________________________________________")
        print("|                                                                             |")
        print("|   |\             //                 [Health:", health, "]                          |")
        print("|   \ \           _!_                 [Attack Damage:", attack, "]                    |")
        print("|    \ \         /___\                                                        |")
        print("|     \ \        [+++]                _________________________________       |")
        print("|      \ \    _ _\^^^/_ _             | You pray to the God of War and |      |")
        print("|       \ \/ (    '-'  ( )            |        gain strength.          |      |")
        print("|         /( \/ | {&}   /\ \          |                                |      |")
        print("|           \  / \     / _> )         | [PRESS ENTER TO START JOURNEY] |      |")
        print("|            *` > ::: ; -'`""'- .       |________________________________|      |")
        print("|                /:::/         \                                              |")
        print("|               /  /||   {&}   |                                              |")
        print("|              (  / (\         /                                              |")
        print("|              / /   \ -.___.-'                                               |")
        print("|            _/ /     \ \                                                     |")
        print("|           /___|    /___|                                                    |")
        print("|_____________________________________________________________________________|")
        input()
        god = False
    elif god_choice == "VITALITY":
        health += 25
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(" _____________________________________________________________________________")
        print("|                                                                             |")
        print("|   |\             //                 [Health:", health, "]                          |")
        print("|   \ \           _!_                 [Attack Damage:", attack, "]                    |")
        print("|    \ \         /___\                                                        |")
        print("|     \ \        [+++]                _________________________________       |")
        print("|      \ \    _ _\^^^/_ _             | You pray to the God of Vitality|      |")
        print("|       \ \/ (    '-'  ( )            |        and gain strength.      |      |")
        print("|         /( \/ | {&}   /\ \          |                                |      |")
        print("|           \  / \     / _> )         | [PRESS ENTER TO START JOURNEY] |      |")
        print("|            *` > ::: ; -'`""'- .       |________________________________|      |")
        print("|                /:::/         \                                              |")
        print("|               /  /||   {&}   |                                              |")
        print("|              (  / (\         /                                              |")
        print("|              / /   \ -.___.-'                                               |")
        print("|            _/ /     \ \                                                     |")
        print("|           /___|    /___|                                                    |")
        print("|_____________________________________________________________________________|")
        input()
        god = False
    else:
        print("Please try again.")

# Calls the Shop Script and then changes all the in game variables after the shop
list1 = shop(player_coins, health, attack, weapon_damage)
weapon_damage = list1[0]
health = list1[1]
player_coins = list1[2]

# First Act

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|                [You leave your town and start your quest]                   |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                      [You arrive at a forked path]                          |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                       [Enter 'LEFT' or 'RIGHT']                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")

act1 = True
while act1:
    choice1 = input().upper()
    if choice1 == "LEFT":
        list0 = scene(health, attack, mob1, bio1, dam1, mob_hp1, weapon_damage, player_coins)
        health = list0[0]
        player_coins = list0[1]
        act1 = False
    elif choice1 == "RIGHT":
        list0 = scene(health, attack, mob2, bio2, dam2, mob_hp2, weapon_damage, player_coins)
        health = list0[0]
        player_coins = list0[1]
        act1 = False
    else:
        print("Please try again.\n")
# Calls the Shop Script and then changes all the in game variables after the shop

list2 = shop(player_coins, health, attack, weapon_damage)
weapon_damage = list2[0]
health = list2[1]
player_coins = list2[2]

# Second Act

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|               [You find yourself lost in a dense forrest.]                  |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                      [You arrive at a forked path]                          |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                       [Enter 'LEFT' or 'RIGHT']                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")

act2 = True
while act2:
    choice2 = input().upper()
    if choice2 == "LEFT":
        list4 = scene(health, attack, mob3, bio3, dam3, mob_hp3, weapon_damage, player_coins)
        health = list4[0]
        player_coins = list4[1]
        act2 = False
    elif choice2 == "RIGHT":
        list4 = scene(health, attack, mob4, bio4, dam4, mob_hp4, weapon_damage, player_coins)
        health = list4[0]
        player_coins = list4[1]
        act2 = False
    else:
        print("Please try again.\n")
# Calls the Shop Script and then changes all the in game variables after the shop

list3 = shop(player_coins, health, attack, weapon_damage)
weapon_damage = list3[0]
health = list3[1]
player_coins = list3[2]

# Third Act

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|               [You find yourself wandering in a desert.]                    |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                      [You arrive at a forked path]                          |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                       [Enter 'LEFT' or 'RIGHT']                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")

act3 = True
while act3:
    choice3 = input().upper()
    if choice3 == "LEFT":
        list5 = scene(health, attack, mob5, bio5, dam5, mob_hp5, weapon_damage, player_coins)
        health = list5[0]
        player_coins = list5[1]
        act3 = False
    elif choice3 == "RIGHT":
        list5 = scene(health, attack, mob6, bio6, dam6, mob_hp6, weapon_damage, player_coins)
        health = list5[0]
        player_coins = list5[1]
        act3 = False
    else:
        print("Please try again.\n")
# Calls the Shop Script and then changes all the in game variables after the shop

list5 = shop(player_coins, health, attack, weapon_damage)
weapon_damage = list5[0]
health = list5[1]
player_coins = list5[2]
# Final Act Dragon Fight
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|                       [You found the dragons lair!]                         |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                           [Press Enter to fight]                            |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")
# Dragon Combat
combat(health, attack, "dragon", drag_dam, drag_hp, weapon_damage, player_coins)

# Scrolling End Screen

for x in range(18):
    list6 = [" _____________________________________________________________________________",
             "|                                                                             |",
             "|                                                                             |",
             "|                   ________  ________   _______   ______                     |",
             "|                  /_  __/ / / / ____/  / ____/ | / / __ \                    |",
             "|                   / / / /_/ / __/    / __/ /  |/ / / / /                    |",
             "|                  / / / __  / /___   / /___/ /|  / /_/ /                     |",
             "|                 /_/ /_/ /_/_____/  /_____/_/ |_/_____/                      |",
             "|                                                                             |",
             "|                                                                             |",
             "|                                                                             |",
             "|                                                                             |",
             "|                           [CONGRATULATIONS!]                                |",
             "|                                                                             |",
             "|                                                                             |",
             "|                                                                             |",
             "|                                                                             |",
             "|_____________________________________________________________________________|\n", ]
    print(list6[x])
    time.sleep(.3)

bio6 = bio_list[random.randrange(1, 5)]

mob_hp1 = random.randrange(30, 40) + diff2
mob_hp2 = random.randrange(30, 40) + diff2
mob_hp3 = random.randrange(32, 40) + (diff2 * 1.5)
mob_hp4 = random.randrange(32, 40) + (diff2 * 1.5)
mob_hp5 = random.randrange(42, 48) + (diff2 * 1.8)
mob_hp6 = random.randrange(42, 48) + (diff2 * 1.8)

dam1 = random.randrange(10, 15) + diff2
dam2 = random.randrange(10, 15) + diff2
dam3 = random.randrange(12, 18) + diff2
dam4 = random.randrange(12, 18) + diff2
dam5 = random.randrange(15, 20) + diff2
dam6 = random.randrange(15, 20) + diff2


def shop(player_coins, health, attack, weapon_damage):

    shop = True
    while shop:
        merchant = input("You stumble across a traveling merchant. What will you do?\n\nShop\nLeave\n").upper()

        if merchant == "SHOP":
            print("\n\n\n\n\n\n\n\n\n\nBrowse my wares sir!")

            print(" _____________________________________________________________________________")
            print("|     PLAYER COINS:", player_coins, "                                                |")
            print("|                                                                             |")
            print("|     [1] Minor Health Potion   +10hp: 7$                                     |")
            print("|     [2] Greater Health Potion +20hp: 12$                                    |")
            print("|     [3] Small Dagger          +5dmg: 10$                                    |")
            print("|     [4] Elvin Sword           +7dmg: 15$                                    |")
            print("|     [5] Claymore             +10dmg: 20$                                    |")
            print("|     [6] Diamond Sword        +15dmg: 35$                                    |")
            print("|     [7] Enchanted Sword      +20dmg: 45$                                    |")
            print("|     [8] Attack Potion    +5 PermDMG: 20$                                    |")
            print("|     [9] Mega Potion           +40hp: 22$                                    |")
            print("|                                                                             |")
            print("|                                                                             |")
            print("|                                                                             |")
            print("|                                                                             |")
            print("|_____________________________________________________________________________|")
            print("Type 'EXIT' to exit shop")
            item = input("What would you like to purchase?\n").upper()
            if item == "EXIT":
                shop = False
            elif (item == "1") and (player_coins >= 7):
                health += 10
                player_coins -= 7
                print("Your health is now", health, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "2" and (player_coins >= 12):
                health += 20
                player_coins -= 12
                print("Your health is now", health, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "3" and (player_coins >= 10):
                del weapon_damage
                weapon_damage = 5
                player_coins -= 10
                print("Your attack damage is now", weapon_damage, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "4" and (player_coins >= 15):
                del weapon_damage
                weapon_damage = 7
                player_coins -= 15
                print("Your attack damage is now", weapon_damage, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "5" and (player_coins >= 20):
                del weapon_damage
                weapon_damage = 10
                player_coins -= 20
                print("Your attack damage is now", weapon_damage, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "6" and (player_coins >= 35):
                del weapon_damage
                weapon_damage = 15
                player_coins -= 35
                print("Your attack damage is now", weapon_damage, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "7" and (player_coins >= 45):
                del weapon_damage
                weapon_damage = 20
                player_coins -= 45
                print("Your attack damage is now", weapon_damage, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "8" and (player_coins >= 20):
                attack += 5
                player_coins -= 20
                print("Your attack is now", attack, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif (item == "9") and (player_coins >= 22):
                health += 40
                player_coins -= 22
                print("Your health is now", health, "points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            else:
                input("ERROR PRESS ENTER TO CONTINUE\n")
        elif merchant == "LEAVE":
            shop = False
    return [weapon_damage, health, player_coins]


def combat(health, attack, mob, dam, mob_hp, weapon_damage, player_coins):
    mob_roll = random.randrange(0, 10)
    player_roll = random.randrange(0, 10)

    player_turn = True
    while player_turn:
        player_attack = attack + random.randrange(0, 7) + weapon_damage
        mob_dam = dam + random.randrange(0, 7)

        if player_roll > mob_roll:

            mob_hp -= player_attack

            input("Press Enter to Continue")

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(" _____________________________________________________________________________")
            print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health),
                  "]                  |")
            print("|  ____________________________________     |\             //                 |")
            print("| |    You did", player_attack, "points of damage!     |   \ \           _!_                 |")
            print("| |                                     |    \ \         /___\                |")
            print("| |                                     |     \ \        [+++]                |")
            print("| |_____________________________________|      \ \    _ _\^^^/_ _             |")
            print("|                                               \ \/ (    '-'  ( )            |")
            print("|                                                 /( \/ | {&}   /\ \          |")
            print("|                                                   \  / \     / _> )         |")
            print("|                                                    *` > ::: ; -'`""'- .       |")
            print("|                                                        /:::/         \      |")
            print("|                                                       /  /||   {&}   |      |")
            print("|                                                      (  / (\         /      |")
            print("|                                                      / /   \ -.___.-'       |")
            print("|                                                    _/ /     \ \             |")
            print("|                                                   /___|    /___|            |")
            print("|_____________________________________________________________________________|")
            if health <= 0:
                print("GAME OVER")
                exit()
            if mob_hp <= 0:
                player_turn = False
            else:
                health -= mob_dam

                input("Press Enter to Continue")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print(" _____________________________________________________________________________")
                print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health),
                      "]                  |")
                print("|  ____________________________________     |\             //                 |")
                print("| |                                     |   \ \           _!_                 |")
                print("| |      The " + mob + " hit you for", mob_dam, "   |    \ \         /___\                |")
                print("| |          points of damage!          |     \ \        [+++]                |")
                print("| |_____________________________________|      \ \    _ _\^^^/_ _             |")
                print("|                                               \ \/ (    '-'  ( )            |")
                print("|                                                 /( \/ | {&}   /\ \          |")
                print("|                                                   \  / \     / _> )         |")
                print("|                                                    *` > ::: ; -'`""'- .       |")
                print("|                                                        /:::/         \      |")
                print("|                                                       /  /||   {&}   |      |")
                print("|                                                      (  / (\         /      |")
                print("|                                                      / /   \ -.___.-'       |")
                print("|                                                    _/ /     \ \             |")
                print("|                                                   /___|    /___|            |")
                print("|_____________________________________________________________________________|")
                if health <= 0:
                    print("GAME OVER")
                    exit()
                if mob_hp <= 0:
                    player_turn = False

        else:
            if health <= 0:
                print("GAME OVER")
                exit()
            if mob_hp <= 0:
                player_turn = False
            health -= mob_dam

            input("Press Enter to Continue")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(" _____________________________________________________________________________")
            print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health), "]             |")
            print("|  ____________________________________     |\             //                 |")
            print("| |                                     |   \ \           _!_                 |")
            print("| |      The " + mob + " hit you for", mob_dam, "   |    \ \         /___\                |")
            print("| |          points of damage!          |     \ \        [+++]                |")
            print("| |_____________________________________|      \ \    _ _\^^^/_ _             |")
            print("|                                               \ \/ (    '-'  ( )            |")
            print("|                                                 /( \/ | {&}   /\ \          |")
            print("|                                                   \  / \     / _> )         |")
            print("|                                                    *` > ::: ; -'`""'- .       |")
            print("|                                                        /:::/         \      |")
            print("|                                                       /  /||   {&}   |      |")
            print("|                                                      (  / (\         /      |")
            print("|                                                      / /   \ -.___.-'       |")
            print("|                                                    _/ /     \ \             |")
            print("|                                                   /___|    /___|            |")
            print("|_____________________________________________________________________________|")
            if health <= 0:
                print("GAME OVER")
                exit()
            if mob_hp <= 0:
                player_turn = False

            else:
                mob_hp -= player_attack

                input("Press Enter to Continue")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print(" _____________________________________________________________________________")
                print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health),
                      "]                      |")
                print("|  ____________________________________     |\             //                 |")
                print("| |    You did", player_attack, "points of damage!     |   \ \           _!_                 |")
                print("| |                                     |    \ \         /___\                |")
                print("| |                                     |     \ \        [+++]                |")
                print("| |_____________________________________|      \ \    _ _\^^^/_ _             |")
                print("|                                               \ \/ (    '-'  ( )            |")
                print("|                                                 /( \/ | {&}   /\ \          |")
                print("|                                                   \  / \     / _> )         |")
                print("|                                                    *` > ::: ; -'`""'- .       |")
                print("|                                                        /:::/         \      |")
                print("|                                                       /  /||   {&}   |      |")
                print("|                                                      (  / (\         /      |")
                print("|                                                      / /   \ -.___.-'       |")
                print("|                                                    _/ /     \ \             |")
                print("|                                                   /___|    /___|            |")
                print("|_____________________________________________________________________________|")
                if health <= 0:
                    print("GAME OVER")
                    exit()
                if mob_hp <= 0:
                    player_turn = False

    print(mob.upper() + " Defeated!")
    random_coins = random.randrange(12, 17) + (diff2 * 2)
    player_coins += random_coins
    print("You receive", random_coins, "coins!\nYou now have", player_coins, "total coins!")
    input("Press Enter to continue.")
    return health, player_coins


def scene(health, attack, mob, bio, dam, mob_hp, weapon_damage, player_coins):
    print("You arrive at the " + mob, bio)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" _____________________________________________________________________________")
    print("|             [Enemy Health:", int(mob_hp), "]             [Health:", int(health), "]                  |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                    [You arrive at the " + mob, bio + "]                      |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                     [Press Enter to Start Combat]                           |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|_____________________________________________________________________________|")
    list0 = combat(health, attack, mob, dam, mob_hp, weapon_damage, player_coins)
    return list0


input("Press Enter to Start Program")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|     ______      __    ___          __  __            __               ___   |")
print("|    / ____/___  / /_  / (_)___     / / / /_  ______  / /____  _____   |__ \  |")
print("|   / / __/ __ \/ __ \/ / / __ \   / /_/ / / / / __ \/ __/ _ \/ ___/   __/ /  |")
print("|  / /_/ / /_/ / /_/ / / / / / /  / __  / /_/ / / / / /_/  __/ /      / __/   |")
print("|  \____/\____/_.___/_/_/_/ /_/  /_/ /_/\__,_/_/ /_/\__/\___/_/      /____/   |")
print("|                                                                             |")
print("|                          [Press Enter to Begin]                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")
input()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|   |\             //                 [Health:", health, "]                          |")
print("|   \ \           _!_                 [Attack Damage:", attack, "]                    |")
print("|    \ \         /___\                                                        |")
print("|     \ \        [+++]                ______________________________          |")
print("|      \ \    _ _\^^^/_ _             | [What god do you worship?]  |         |")
print("|       \ \/ (    '-'  ( )            |                             |         |")
print("|         /( \/ | {&}   /\ \          |God of War: +5 Attack Damage |         |")
print("|           \  / \     / _> )         |God of Vitality: +25 Health  |         |")
print("|            *` > ::: ; -'`""'- .       |_____________________________|         |")
print("|                /:::/         \                                              |")
print("|               /  /||   {&}   |                                              |")
print("|              (  / (\         /                                              |")
print("|              / /   \ -.___.-'                                               |")
print("|            _/ /     \ \                                                     |")
print("|           /___|    /___|                                                    |")
print("|_____________________________________________________________________________|")
god = True
while god:
    god_choice = input("Type 'WAR' or 'VITALITY'\n").upper()
    if god_choice == "WAR":
        attack += 5
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(" _____________________________________________________________________________")
        print("|                                                                             |")
        print("|   |\             //                 [Health:", health, "]                          |")
        print("|   \ \           _!_                 [Attack Damage:", attack, "]                    |")
        print("|    \ \         /___\                                                        |")
        print("|     \ \        [+++]                _________________________________       |")
        print("|      \ \    _ _\^^^/_ _             | You pray to the God of War and |      |")
        print("|       \ \/ (    '-'  ( )            |        gain strength.          |      |")
        print("|         /( \/ | {&}   /\ \          |                                |      |")
        print("|           \  / \     / _> )         | [PRESS ENTER TO START JOURNEY] |      |")
        print("|            *` > ::: ; -'`""'- .       |________________________________|      |")
        print("|                /:::/         \                                              |")
        print("|               /  /||   {&}   |                                              |")
        print("|              (  / (\         /                                              |")
        print("|              / /   \ -.___.-'                                               |")
        print("|            _/ /     \ \                                                     |")
        print("|           /___|    /___|                                                    |")
        print("|_____________________________________________________________________________|")
        input()
        god = False
    elif god_choice == "VITALITY":
        health += 25
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(" _____________________________________________________________________________")
        print("|                                                                             |")
        print("|   |\             //                 [Health:", health, "]                          |")
        print("|   \ \           _!_                 [Attack Damage:", attack, "]                    |")
        print("|    \ \         /___\                                                        |")
        print("|     \ \        [+++]                _________________________________       |")
        print("|      \ \    _ _\^^^/_ _             | You pray to the God of Vitality|      |")
        print("|       \ \/ (    '-'  ( )            |        and gain strength.      |      |")
        print("|         /( \/ | {&}   /\ \          |                                |      |")
        print("|           \  / \     / _> )         | [PRESS ENTER TO START JOURNEY] |      |")
        print("|            *` > ::: ; -'`""'- .       |________________________________|      |")
        print("|                /:::/         \                                              |")
        print("|               /  /||   {&}   |                                              |")
        print("|              (  / (\         /                                              |")
        print("|              / /   \ -.___.-'                                               |")
        print("|            _/ /     \ \                                                     |")
        print("|           /___|    /___|                                                    |")
        print("|_____________________________________________________________________________|")
        input()
        god = False
    else:
        print("Please try again.")

list1 = shop(player_coins, health, attack, weapon_damage)
weapon_damage = list1[0]
health = list1[1]
player_coins = list1[2]

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|                [You leave your town and start your quest]                   |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                      [You arrive at a forked path]                          |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                       [Enter 'LEFT' or 'RIGHT']                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")

act1 = True
while act1:
    choice1 = input().upper()
    if choice1 == "LEFT":
        list0 = scene(health, attack, mob1, bio1, dam1, mob_hp1, weapon_damage, player_coins)
        health = list0[0]
        player_coins = list0[1]
        act1 = False
    elif choice1 == "RIGHT":
        list0 = scene(health, attack, mob2, bio2, dam2, mob_hp2, weapon_damage, player_coins)
        health = list0[0]
        player_coins = list0[1]
        act1 = False
    else:
        print("Please try again.\n")

list2 = shop(player_coins, health, attack, weapon_damage)
weapon_damage = list2[0]
health = list2[1]
player_coins = list2[2]

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|               [You find yourself lost in a dense forrest.]                  |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                      [You arrive at a forked path]                          |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                       [Enter 'LEFT' or 'RIGHT']                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")

act2 = True
while act2:
    choice2 = input().upper()
    if choice2 == "LEFT":
        list4 = scene(health, attack, mob3, bio3, dam3, mob_hp3, weapon_damage, player_coins)
        health = list4[0]
        player_coins = list4[1]
        act2 = False
    elif choice2 == "RIGHT":
        list4 = scene(health, attack, mob4, bio4, dam4, mob_hp4, weapon_damage, player_coins)
        health = list4[0]
        player_coins = list4[1]
        act2 = False
    else:
        print("Please try again.\n")

list3 = shop(player_coins, health, attack, weapon_damage)
weapon_damage = list3[0]
health = list3[1]
player_coins = list3[2]

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|               [You find yourself wandering in a desert.]                    |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                      [You arrive at a forked path]                          |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                       [Enter 'LEFT' or 'RIGHT']                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")

act3 = True
while act3:
    choice3 = input().upper()
    if choice3 == "LEFT":
        list5 = scene(health, attack, mob5, bio5, dam5, mob_hp5, weapon_damage, player_coins)
        health = list5[0]
        player_coins = list5[1]
        act3 = False
    elif choice3 == "RIGHT":
        list5 = scene(health, attack, mob6, bio6, dam6, mob_hp6, weapon_damage, player_coins)
        health = list5[0]
        player_coins = list5[1]
        act3 = False
    else:
        print("Please try again.\n")

list5 = shop(player_coins, health, attack, weapon_damage)
weapon_damage = list5[0]
health = list5[1]
player_coins = list5[2]

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|                       [You found the dragons lair!]                         |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                           [Press Enter to fight]                            |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")

combat(health, attack, "dragon", drag_dam, drag_hp, weapon_damage, player_coins)

for x in range(18):

    list6 = [" _____________________________________________________________________________",
             "|                                                                             |",
             "|                                                                             |",
             "|                   ________  ________   _______   ______                     |",
             "|                  /_  __/ / / / ____/  / ____/ | / / __ \                    |",
             "|                   / / / /_/ / __/    / __/ /  |/ / / / /                    |",
             "|                  / / / __  / /___   / /___/ /|  / /_/ /                     |",
             "|                 /_/ /_/ /_/_____/  /_____/_/ |_/_____/                      |",
             "|                                                                             |",
             "|                                                                             |",
             "|                                                                             |",
             "|                                                                             |",
             "|                           [CONGRATULATIONS!]                                |",
             "|                                                                             |",
             "|                                                                             |",
             "|                                                                             |",
             "|                                                                             |",
             "|_____________________________________________________________________________|\n", ]
    print(list6[x])
    time.sleep(.3)
