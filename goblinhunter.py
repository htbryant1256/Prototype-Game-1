import random
health = 20
weapon_damage = 0
player_coins = 5
print("GAME START\nHealth:",health,"\nCoins:",player_coins)


#Part 1
forked_path = True
while forked_path:
    choice1 = input("You arrive at a forked path, what will you do?\n\nGo left\nGo right\n").upper()
    if choice1 == "GO LEFT":
        forked_path = False
        bandit_camp = True
        while bandit_camp:
            mob_name = "goblin"
            mob_area = "camp"
            choice2 =input("You walk down the left path and see a goblin camp with a single goblin,\nthe others seem to be off hunting but you can tell they are near by.\nWhat wil you do?\n\nFight\nSteal\n").upper()
            if choice2 == "FIGHT":
                input("\nPress any key to enter combat mode.")
                mob_health = 13
                while mob_health > 0:
                    print(
                        "     _,.\n   ,` -.)\n    ( _/-\ -._\n   /,|`--._,-^|            ,\n   \_| |`-._/||          ,'|\n     |  `-, / |         /  /\n     |     || |        /  /\n      `r-._||/   __   /  /\n  __,-<_     )`-/  `./  /\n '  \   `---'   \   /  /\n'  \   `---'   \   /  /\n    |           |./  /\n    /           //  /\n\_/' \         |/  /\n |    |   _,^-'/  /\n |    , ``  (\/  /_\n  \,.->._    \X-=/^\n  (  /   `-._//^`\n   `Y-.____(__}\n    |     {__)")
                    player_attack = (random.randrange(4, 9) + weapon_damage)
                    mob_damage = random.randrange(2, 6)
                    mob_health -= player_attack
                    health -= mob_damage
                    if player_attack >= 7:
                        print("CRITICAL HIT!")
                    print("You did", player_attack, "points of damage!\nThe " + mob_name + " hit you for", mob_damage,
                          "points of damage!\n\n" + (mob_name).upper() + " HEALTH:", mob_health, "\n\nPLAYER HEALTH:",
                          health)
                    if health <= 0:
                        print("GAME OVER")
                        exit()

                    if mob_health <= 0:
                        print((mob_name).upper() + " Defeated!")
                        random_coins = random.randrange(7, 14)
                        player_coins += random_coins
                        print("You recive", random_coins, "coins!\nYou now have", player_coins, "total coins!")
                    input("Press any key to continue.")
                bandit_camp = False
            elif choice2 == "STEAL":
                bandit_camp = False
                stolen_coins = random.randrange(3,11)
                player_coins += stolen_coins
                print("You stole ",stolen_coins," coins!\nYou now have",player_coins,"total coins!\n")
            else:
                print("INVALID RESPONSE, TYPE AGAIN.")
                del choice2
    elif choice1 == "GO RIGHT":
        forked_path = False
        spider_cave = True
        while spider_cave:
            mob_name = "spider"
            mob_area = "cave"
            choice3 =input("You walk down the right path and see a cave.\nYou enter the cave and see a treasure chest\ngaurded by a big spider. What will you do?\n\nLeave\nFight\n").upper()
            if choice3 == "FIGHT":
                input("\nPress any key to enter combat mode.")
                mob_health = 13
                while mob_health > 0:
                    print(
                        "     _,.\n   ,` -.)\n    ( _/-\ -._\n   /,|`--._,-^|            ,\n   \_| |`-._/||          ,'|\n     |  `-, / |         /  /\n     |     || |        /  /\n      `r-._||/   __   /  /\n  __,-<_     )`-/  `./  /\n '  \   `---'   \   /  /\n'  \   `---'   \   /  /\n    |           |./  /\n    /           //  /\n\_/' \         |/  /\n |    |   _,^-'/  /\n |    , ``  (\/  /_\n  \,.->._    \X-=/^\n  (  /   `-._//^`\n   `Y-.____(__}\n    |     {__)")
                    player_attack = (random.randrange(4, 9) + weapon_damage)
                    mob_damage = random.randrange(2, 6)
                    mob_health -= player_attack
                    health -= mob_damage
                    if player_attack >= 7:
                        print("CRITICAL HIT!")
                    print("You did", player_attack, "points of damage!\nThe " + mob_name + " hit you for", mob_damage,
                          "points of damage!\n\n" + (mob_name).upper() + " HEALTH:", mob_health, "\n\nPLAYER HEALTH:",
                          health)
                    if health <= 0:
                        print("GAME OVER")
                        exit()

                    if mob_health <= 0:
                        print((mob_name).upper() + " Defeated!")
                        random_coins = random.randrange(10, 16)
                        player_coins += random_coins
                        print("You recive", random_coins, "coins!\nYou now have", player_coins, "total coins!")
                    input("Press any key to continue.")
                spider_cave = False
            elif choice3 == "LEAVE":
                spider_cave = False
            else:
                print("INVALID RESPONSE, TYPE AGAIN.")
                del choice3


    else:
        print("INVALID RESPONSE, TYPE AGAIN.")
        del choice1
print("You leave the "+mob_name+" "+mob_area+" and continue ")



#Shop
merch_man = True
while merch_man:
    merchant=input("You stumble accross a traveling merchant. What will you do?\n\nShop\nLeave\n").upper()
    if merchant == "SHOP":
        shop = True
        while shop:
            print("\n\n\n\n\n\n\n\n\n\nBrowse my wares sir!")
            print("PLAYER COINS:",player_coins)
            print("__________________________________")
            print("|Minor Health Potion +10hp: 7$   |")
            print("|Greater Health Potion +20: 12$  |")
            print("|Small Dagger        +5dmg: 10$  |")
            print("|Elvin Sword         +7dmg: 15$  |")
            print("|Claymore           +10dmg: 20$  |")
            print("__________________________________")
            print("Type 'EXIT' to exit shop")
            item=input("What would you like to purchase?\n").upper()
            if item == "EXIT":
                shop = False
            elif (item == "MINOR HEALTH POTION") and (player_coins >= 7):
                health += 10
                player_coins -= 7
                print("Your health is now",health,"points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "GREATER HEALTH POTION" and (player_coins >= 12):
                health += 20
                player_coins -= 12
                print("Your health is now",health,"points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "SMALL DAGGER" and (player_coins >= 10):
                weapon_damage += 5
                player_coins -= 10
                print("Your attack damage is now",weapon_damage,"points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "ELVIN SWORD" and (player_coins >= 15):
                weapon_damage += 7
                player_coins -= 15
                print("Your attack damage is now",weapon_damage,"points\n")
                print("You now have", player_coins, "coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            elif item == "CLAYMORE" and (player_coins >= 20):
                weapon_damage += 10
                player_coins -= 20
                print("Your attack damage is now",weapon_damage,"points\n")
                print("You now have",player_coins,"coins.\n")
                del item
                input("\nPress ENTER to continue.\n")
            else:
                input("ERROR PRESS ENTER TO CONTINUE\n")
    elif merchant == "LEAVE":
        merch_man = False
    else:
        print("Invalid")
        del merchant
#Part 2
forked_path2 = True
while forked_path2:
    choice4 = input("You arrive at a forked mountain road, what will you do?\n\nGo left\nGo right\n").upper()
    if choice4 == "GO LEFT":
        forked_path2 = False
        grave_yard = True
        while grave_yard:
            mob_name = "zombie"
            mob_area = "grave yard"
            choice5 =input("You find a grave yard. One of the graves is highly decorated.\nWhat wil you do?\n\nLoot\nLeave\n").upper()
            if choice5 == "LOOT":
                print("A zombie bursts from the grave for a suprise attack!")
                mob_damage = random.randrange(5, 8)
                health -= mob_damage
                print("The zombie hits you for",mob_damage,"points of damage!\nYou now have",health,"points of health.")
                input("\nPress any key to enter combat mode.")
                mob_health = 15
                while mob_health > 0:
                    print(
                        "     _,.\n   ,` -.)\n    ( _/-\ -._\n   /,|`--._,-^|            ,\n   \_| |`-._/||          ,'|\n     |  `-, / |         /  /\n     |     || |        /  /\n      `r-._||/   __   /  /\n  __,-<_     )`-/  `./  /\n '  \   `---'   \   /  /\n'  \   `---'   \   /  /\n    |           |./  /\n    /           //  /\n\_/' \         |/  /\n |    |   _,^-'/  /\n |    , ``  (\/  /_\n  \,.->._    \X-=/^\n  (  /   `-._//^`\n   `Y-.____(__}\n    |     {__)")
                    player_attack = (random.randrange(4, 9) + weapon_damage)
                    mob_damage = random.randrange(6, 11)
                    mob_health -= player_attack
                    health -= mob_damage
                    if player_attack >= 7:
                        print("CRITICAL HIT!")
                    print("You did", player_attack, "points of damage!\nThe " + mob_name + " hit you for", mob_damage,
                          "points of damage!\n\n" + (mob_name).upper() + " HEALTH:", mob_health, "\n\nPLAYER HEALTH:",
                          health)
                    if health <= 0:
                        print("GAME OVER")
                        exit()

                    if mob_health <= 0:
                        print((mob_name).upper() + " Defeated!")
                        random_coins = random.randrange(15,20)
                        player_coins += random_coins
                        print("You recive", random_coins, "coins!\nYou now have", player_coins, "total coins!")
                    input("Press any key to continue.")
                grave_yard = False
            elif choice5 == "STEAL":
                bandit_camp = False
                stolen_coins = random.randrange(3,11)
                player_coins += stolen_coins
                print("You stole ",stolen_coins," coins!\nYou now have",player_coins,"total coins!\n")
            else:
                print("INVALID RESPONSE, TYPE AGAIN.")
                del choice5
    elif choice4 == "GO RIGHT":
        forked_path2 = False
        birds_nest = True
        while birds_nest:
            mob_name = "gaint bird"
            mob_area = "nest"
            input("You walk down the right path and see a giant birds nest.\nYou approach the nest and a gaint bird flys down!")

            input("\nPress any key to enter combat mode.")
            mob_health = 20
            while mob_health > 0:
                print(
                    "     _,.\n   ,` -.)\n    ( _/-\ -._\n   /,|`--._,-^|            ,\n   \_| |`-._/||          ,'|\n     |  `-, / |         /  /\n     |     || |        /  /\n      `r-._||/   __   /  /\n  __,-<_     )`-/  `./  /\n '  \   `---'   \   /  /\n'  \   `---'   \   /  /\n    |           |./  /\n    /           //  /\n\_/' \         |/  /\n |    |   _,^-'/  /\n |    , ``  (\/  /_\n  \,.->._    \X-=/^\n  (  /   `-._//^`\n   `Y-.____(__}\n    |     {__)")
                player_attack = (random.randrange(4, 9) + weapon_damage)
                mob_damage = random.randrange(10, 14)
                mob_health -= player_attack
                health -= mob_damage
                if player_attack >= 7:
                    print("CRITICAL HIT!")
                print("You did", player_attack, "points of damage!\nThe " + mob_name + " hit you for", mob_damage,
                      "points of damage!\n\n" + (mob_name).upper() + " HEALTH:", mob_health, "\n\nPLAYER HEALTH:",
                      health)
                if mob_health <= 0:
                    print((mob_name).upper() + " Defeated!")
                    random_coins = random.randrange(7, 14)
                    player_coins += random_coins
                    print("You found", random_coins, "coins!\nYou now have", player_coins, "total coins!")
                input("Press any key to continue.")
                birds_nest = False


    else:
        print("INVALID RESPONSE, TYPE AGAIN.")
        del choice3
print("\nYou leave the "+mob_name+" "+mob_area+" and continue ")

print("\n\nEND OF DEMO THANKS FOR PLAYING")
