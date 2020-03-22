import random
weapon_damage = 0
player_coins = 10
health = 100
attack = 10
drag_dam = 20
drag_hp = 60

mob_list = [" Goblin ","Skeleton"," Spider ","Werewolf"]
bio_list = ["Cave","Den","Camp","Fortress","Castle"]

mob1 = mob_list[random.randrange(1,4)]
mob2 = mob_list[random.randrange(1,4)]
mob3 = mob_list[random.randrange(1,4)]
mob4 = mob_list[random.randrange(1,4)]
mob5 = mob_list[random.randrange(1,4)]
mob6 = mob_list[random.randrange(1,4)]


bio1 = bio_list[random.randrange(1,5)]
bio2 = bio_list[random.randrange(1,5)]
bio3 = bio_list[random.randrange(1,5)]
bio4 = bio_list[random.randrange(1,5)]
bio5 = bio_list[random.randrange(1,5)]
bio6 = bio_list[random.randrange(1,5)]

mob_hp1 = random.randrange(30,40)
mob_hp2 = random.randrange(30,40)
mob_hp3 = random.randrange(40,50)
mob_hp4 = random.randrange(40,50)
mob_hp5 = random.randrange(50,60)
mob_hp6 = random.randrange(50,60)

dam1 = random.randrange(10,15)
dam2 = random.randrange(10,15)
dam3 = random.randrange(15,20)
dam4 = random.randrange(15,20)
dam5 = random.randrange(15,20)
dam6 = random.randrange(15,20)
def shop(player_coins,health,attack,weapon_damage):
    merch_man = True
    while merch_man:
        merchant = input("You stumble accross a traveling merchant. What will you do?\n\nShop\nLeave\n").upper()
        if merchant == "SHOP":
            shop = True
            while shop:
                print("\n\n\n\n\n\n\n\n\n\nBrowse my wares sir!")
                print("PLAYER COINS:", player_coins)
                print("__________________________________")
                print("|Minor Health Potion +10hp: 7$   |")
                print("|Greater Health Potion +20: 12$  |")
                print("|Small Dagger        +5dmg: 10$  |")
                print("|Elvin Sword         +7dmg: 15$  |")
                print("|Claymore           +10dmg: 20$  |")
                print("|________________________________|")
                print("Type 'EXIT' to exit shop")
                item = input("What would you like to purchase?\n").upper()
                if item == "EXIT":
                    shop = False
                elif (item == "MINOR HEALTH POTION") and (player_coins >= 7):
                    health += 10
                    player_coins -= 7
                    print("Your health is now", health, "points\n")
                    print("You now have", player_coins, "coins.\n")
                    del item
                    input("\nPress ENTER to continue.\n")
                elif item == "GREATER HEALTH POTION" and (player_coins >= 12):
                    health += 20
                    player_coins -= 12
                    print("Your health is now", health, "points\n")
                    print("You now have", player_coins, "coins.\n")
                    del item
                    input("\nPress ENTER to continue.\n")
                elif item == "SMALL DAGGER" and (player_coins >= 10):
                    del weapon_damage
                    weapon_damage = 5
                    player_coins -= 10
                    print("Your attack damage is now", weapon_damage, "points\n")
                    print("You now have", player_coins, "coins.\n")
                    del item
                    input("\nPress ENTER to continue.\n")
                elif item == "ELVIN SWORD" and (player_coins >= 15):
                    del weapon_damage
                    weapon_damage = 7
                    player_coins -= 15
                    print("Your attack damage is now", weapon_damage, "points\n")
                    print("You now have", player_coins, "coins.\n")
                    del item
                    input("\nPress ENTER to continue.\n")
                elif item == "CLAYMORE" and (player_coins >= 20):
                    del weapon_damage
                    weapon_damage = 10
                    player_coins -= 20
                    print("Your attack damage is now", weapon_damage, "points\n")
                    print("You now have", player_coins, "coins.\n")
                    del item
                    input("\nPress ENTER to continue.\n")
                else:
                    input("ERROR PRESS ENTER TO CONTINUE\n")
        elif merchant == "LEAVE":
            merch_man = False
        else:
            print("Invalid")
            del merchant
    return[weapon_damage,health,player_coins]


def combat(health,attack,mob,bio,dam,mob_hp,weapon_damage,player_coins):
    input("\nPress Enter to start combat mode.")
    while mob_hp > 0:
        print("TEST",weapon_damage)
        player_attack = attack + random.randrange(0,7) + weapon_damage
        mob_dam = dam + random.randrange(0,7)
        mob_hp -= player_attack
        health -= mob_dam
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(" _____________________________________________________________________________")
        print("|             [Enemy Health:",mob_hp,"]             [Health:",health,"]                  |")
        print("|  ____________________________________     |\             //                 |")
        print("| |    You did", player_attack, "points of damage!     |   \ \           _!_                 |")
        print("| |      The " + mob + " hit you for", mob_dam,"   |    \ \         /___\                |")
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
            print((mob).upper() + " Defeated!")
            random_coins = random.randrange(10, 14)
            player_coins += random_coins
            print("You recive", random_coins, "coins!\nYou now have", player_coins, "total coins!")
        input("Press Enter to continue.")
    return(health,player_coins)

def scene(health,attack,mob,bio,dam,mob_hp,weapon_damage,player_coins):
    print("You arrive at the "+ mob , bio)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" _____________________________________________________________________________")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                    [You arrive at the "+ mob , bio +"]                      |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                     [Press Enter to Start Combat]                           |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|                                                                             |")
    print("|_____________________________________________________________________________|")
    list = combat(health,attack,mob,bio,dam,mob_hp,weapon_damage,player_coins)
    return(list)

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

list1 = shop(player_coins,health,attack,weapon_damage)
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
        list = scene(health,attack,mob1,bio1,dam1,mob_hp1,weapon_damage,player_coins)
        health = list[0]
        player_coins = list[1]
        act1 = False
    elif choice1 == "RIGHT":
        list = scene(health, attack, mob1, bio1, dam1, mob_hp1, weapon_damage, player_coins)
        health = list[0]
        player_coins = list[1]
        act1 = False
    else:
        print("Please try again.\n")

list2 = shop(player_coins,health,attack,weapon_damage)
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
        list4 = scene(health, attack, mob1, bio1, dam1, mob_hp1, weapon_damage, player_coins)
        health = list[0]
        player_coins = list[1]
        act1 = False
    elif choice2 == "RIGHT":
        list4 = scene(health, attack, mob1, bio1, dam1, mob_hp1, weapon_damage, player_coins)
        health = list[0]
        player_coins = list[1]
        act2 = False
    else:
        print("Please try again.\n")

list3 = shop(player_coins,health,attack,weapon_damage)
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
        list5 = scene(health, attack, mob1, bio1, dam1, mob_hp1, weapon_damage, player_coins)
        health = list[0]
        player_coins = list[1]
        act3 = False
    elif choice3 == "RIGHT":
        list5 = scene(health, attack, mob1, bio1, dam1, mob_hp1, weapon_damage, player_coins)
        health = list[0]
        player_coins = list[1]
        act3 = False
    else:
        print("Please try again.\n")


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

input("\nPress Enter to start combat mode.")
while drag_hp > 0:
    print("TEST",weapon_damage)
    player_attack = attack + random.randrange(0,7) + weapon_damage
    boss_dam = drag_dam + random.randrange(0,7)
    drag_hp -= player_attack
    health -= boss_dam
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(" _____________________________________________________________________________")
    print("|             [Enemy Health:",drag_hp,"]             [Health:",health,"]                  |")
    print("|  ____________________________________     |\             //                 |")
    print("| |    You did", player_attack, "points of damage!     |   \ \           _!_                 |")
    print("| |      The Dragon hit you for",drag_dam,"     |    \ \         /___\                |")
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
    if drag_hp <= 0:
        print("Dragon Defeated!")
        random_coins = random.randrange(10, 14)
        player_coins += random_coins
        print("You recive", random_coins, "coins!\nYou now have", player_coins, "total coins!")
    input("Press Enter to continue.")

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" _____________________________________________________________________________")
print("|                                                                             |")
print("|                                                                             |")
print("|                   ________  ________   _______   ______                     |")
print("|                  /_  __/ / / / ____/  / ____/ | / / __ \                    |")
print("|                   / / / /_/ / __/    / __/ /  |/ / / / /                    |")
print("|                  / / / __  / /___   / /___/ /|  / /_/ /                     |")
print("|                 /_/ /_/ /_/_____/  /_____/_/ |_/_____/                      |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                           [CONGRATULATIONS!]                                |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|                                                                             |")
print("|_____________________________________________________________________________|")


