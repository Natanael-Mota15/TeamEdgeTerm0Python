import random
import sys 

animals = ["Chicken", "pig", "sheep", "cow"]
animals_drop = {"Chicken":1, "pig":2, "sheep":3, "cow":3}
ffoods = ["3 apples", "3 watermelon", "5 potato", "1 carrot", "nothing"]
exta = 0


class Enemy: 
    def __init__(self, name, health, attack, armor, weapon):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.weapon = weapon
    def __repr__(self):
        return f"Name: {self.name}, Health: {self.health}, Attack damage: {self.attack}, Armor: {self.armor}, Weapon: {self.weapon} "

zombie = Enemy("Zombie", 65, 10, 0, "Fists")
drowned = Enemy("Drowned", 80, 20, 1, "Trident")
ender_dragon =  Enemy("Ender Dragon", 60, 10, 10, "Fire breath")




class Player:
    def __init__(self, name, energy):
        self.day = 1
        self.name = name
        self.health = 100
        self.energy = energy
        self.armor = 0
        self.hunger = 9
        self.ooth = 9
        self.inventory  =  {}
        self.defence = 0
        self.weapons = {"fists": 4}
        self.location = "spawn"
    def __repr__(self):
        return f"Day: {self.day} ,Name: {self.name}, Health: {self.health}, Energy: {self.energy} Armor: {self.armor}, Hunger: {self.hunger}, Out of: {self.ooth}, Inventory:{self.inventory}, Defence:{self.defence}, Weapons:{self.weapons}, Location:{self.location} "


    def cry(self):
        print("You let yourself cry for a few minutes. After crying you look up and think ...")
        self.energy = self.energy - 45
        
     
    def collect_dirt(self):
        print("You go collecting dirt which shows in your inventory\nTook you 3 energy")
        self.energy = self.energy - 3
        if self.inventory.keys() == ("Dirt"):
            print ("Added to you inventory")
            ran_num = random.randrange(5, 30)
            dirt_num = player.inventory("Dirt")
            new_num = dirt_num + ran_num
            self.inventory.update({"Dirt" : new_num})
            print(self.inventory)
        elif self.inventory.keys() != ("Dirt"):
            print ("Added to you inventory")
            self.inventory.update({"Dirt":random.randrange(5, 30)})
            print(self.inventory)
            

    def kill_animals(self):
        animal_num = random.randrange(0, 4)
        self.energy = self.energy - 8
        anl = f"{animals[animal_num]}"
        adrop = (animals_drop.get(anl))
        print(f"You see a {anl}")
        weapon = input(f"What weapon will you use?\n{self.weapons}")
        while weapon in self.weapons ==  False:
            print("You dont have that")   
            weapon = input(f"What weapon will you use?\n{self.weapons}")  
        if weapon in self.weapons:
            print("You killed it.")
            self.inventory.update({anl:adrop})
        if anl in self.inventory:
            i_anl = player.inventory.get(anl)
            ran_numt = adrop
            new_numa = i_anl + ran_numt
            self.inventory.update({(anl) : new_numa})
            print(self.inventory)
            

    def look_food(self):
        numf = random.randrange(0, 5)
        print("You looked for food. You used 4 energy")
        self.energy = self.energy - 4
        print(f"You see {ffoods[numf]}")
        if numf == 0:
            answer2 = input("Do want to collect?").lower()
            if answer2 == "yes":
                if self.inventory.keys() == ("Apples"):
                    print ("Added to you inventory")
                    self.inventory.update({"Apples":int(self.inventory.get("Apples")) + 3})
                    print(self.inventory)
                elif self.inventory.keys() != ("Apples"):
                    print ("Added to you inventory")
                    self.inventory.update({"Apples": 3})
                    print(self.inventory)
                else:
                    print ("huh")
            elif answer2 == "no":
                print("Ok")
                print(self.inventory)
            else:
                print ("huh")
        elif numf == 1:
            answer3 = input("Do want to collect?").lower()
            if answer3 == "yes":
                if self.inventory.keys() == ("Watermelon"):
                    print ("Added to you inventory")
                    self.inventory.update({"Watermelon":int(self.inventory.get("Watermelon")) + 3})
                    print(self.inventory)
                elif self.inventory.keys() != ("Watermelon"):
                    print ("Added to you inventory")
                    self.inventory.update({"Watermelon": 3})
                    print(self.inventory)
                else:
                    print ("huh")
            elif answer3 == "no":
                print("Ok")
                print(self.inventory)
            else:
                print ("huh")
        elif numf == 2:
            answer4 = input("Do want to collect?").lower()
            if answer4 == "yes":
                if self.inventory.keys() == ("Potato"):
                    print ("Added to you inventory")
                    self.inventory.update({"Potato":int(self.inventory.get("Potato")) + 5})
                    print(self.inventory)
                elif self.inventory.keys() != ("Potato"):
                    print ("Added to you inventory")
                    self.inventory.update({"Potato": 5})
                    print(self.inventory)
                else:
                    print ("huh")
            elif answer4 == "no":
                print("Ok")
                print(self.inventory)
            else:
                print ("huh")
        elif numf == 3:
            answer5 = input("Do want to collect?").lower()
            if answer5 == "yes":
                if self.inventory.keys() == ("Carrrot"):
                    print ("Added to you inventory")
                    self.inventory.update({"Carrot":int(self.inventory.get("Carrot")) + 1})
                    print(self.inventory)
                elif self.inventory.keys() != ("Carrrot"):
                    print ("Added to you inventory")
                    self.inventory.update({"Carrot": 1})
                    print(self.inventory)
                else:
                    print ("huh")
            elif answer5 == "no":
                print("Ok")
                print(self.inventory)
            else:
                print ("huh")
        elif numf == 4:
            print("You found nothing")
            print(self.inventory)
        else:
            print ("huh")
         

    def wood(self):
        self.energy = self.energy - 4
        if len(self.weapons) ==  1:
            print("You collect wood")
            if "Wood" in player.inventory.keys():
                print ("Added to you inventory")
                player.inventory["inventory"]["Wood"] = player.inventory["inventory"]["Wood"] + 6
                print(player.inventory)
            elif player.inventory.keys() != ("Wood"):
                print ("Added to you inventory")
                player.inventory.update({"Wood": 6})
                print(player.inventory)
            else:
                print ("huh")
        
    def talk(self):
        vc = input("Who do you want to talk to?\nVillager1\nVillager2\nVillager3\nGolem1\nGolem2\nGolem3")
        print(f"You went to talk to {vc}")
        vnumo = 0
        vnumt = 0
        vnumth = 0
        golem_1 = 1
        golem_2 = 1
        golem_3 = 1
        if (vc == "Villager1") and (vnumo == 0):
            self.energy = self.energy - 4
            vnumo += 1
            ans = input(f"Hello, here is my info {villager1}, nice to meet you. I can give you a prize if you answer this right. What is 1 + 1?")
            if ans == "2":
                player.inventory.update({"Fish":20})
            else:
                print("That wrong")
        
        elif (vc == "Villager2") and (vnumt == 0):
            self.energy = self.energy - 4
            vnumt += 1
            ans = input(f"Hello, here is my info {villager2}, nice to meet you. I can give you a prize if you answer this right. What is BTS?")
            if ans == "Bacon Turkey Sandwitch":
                player.inventory.update({"Gold bar":30})
                player.weapons.update({"sword": 15})
                player.weapons.update({"axe":10})
                player.weapons.update({"pickaxe":8})
                player.armor += 20
                print("You got a full metal armor, a shield, sword, axe and a pickaxe")
            elif ans == "A band":
                player.inventory.update({"Gold bar":10})
                player.weapons.update("sword")
                player.armor += 10
                exta3 = player.weapons.get("fists")
                exta1 = player.weapons.get("pickaxe")
                exta0 = player.weapons.get("sword")
                exta = 4 + exta0 + exta1 +exta3
                print("You got a full leather armor, and a sword")
            else:
                print("That wrong")
        elif (vc == "Villager3") and (vnumth == 0):
            self.energy = self.energy - 4
            vnumth += 1
            ans = input(f"Hello, here is my info {villager3}, nice to meet you. I can give you a prize if you answer this right. What is x equal to?")
            if ans == "x":
                player.inventory.update({"Bread":40})
            else:
                print("That wrong")
        elif (vc == "Golem1") and (golem_1 == 1):
            self.energy = self.energy - 4
            resp = input("You go see the Iron Golem. You stand right in front of it. It glares at you with it red eyes, trying to figure if you are a threat of not. What will you do?\nAttack\nLeave\nStay a little")
            if resp == "Attack":
                print("You attacked the golem")
                print("The golem eye shines red as it lifts its arm and brings them down at you.")
                print("You die")
                sys.exit()
            elif resp == "Leave":
                print("You left")
            elif resp == "Stay" or "Stay a little":
                print("The golem face softens and gives you a flower")
                if "Flower" in player.inventory == False:
                    player.inventory.update({"Flower":1})
                elif "Flower" in player.inventory == True:
                    num1 = player.inventory.get("Flower")
                    num2 = num1 + 1
                    self.inventory.update({"Flower" : num2})
            elif (vc == "Golem2") and (golem_2 == 1):
                self.energy = self.energy - 4
                resp2 = input("You go see the Iron Golem. You stand right in front of it. It glares at you with it red eyes, trying to figure if you are a threat of not. What will you do?\nAttack\nLeave\nStay a little")
                if resp2 == "Attack":
                    print("You attacked the golem")
                    print("The golem eye shines red as it lifts its arm and brings them down at you.")
                    print("You die")
                    sys.exit()
                elif resp2 == "Leave":
                    print("You left")
                elif resp2 == "Stay" or "Stay a little":
                    print("The golem face softens and gives you a flower")
                    if "Flower" in player.inventory == False:
                        player.inventory.update({"Flower":1})
                    elif "Flower" in player.inventory == True:
                        num1 = player.inventory.get("Flower")
                        num2 = num1 + 1
                        self.inventory.update({"Flower" : num2})
                elif (vc == "Golem3") and (golem_3 == 1):
                    self.energy = self.energy - 4
                    resp3 = input("You go see the Iron Golem. You stand right in front of it. It glares at you with it red eyes, trying to figure if you are a threat of not. What will you do?Attack\nLeave\nStay a little")
                    if resp3 == "Attack":
                        print("You attacked the golem")
                        print("The golem eye shines red as it lifts its arm and brings them down at you.")
                        print("You die")
                        sys.exit()
                    elif resp3 == "Leave":
                        print("You left")
                    elif resp3 == "Stay" or "Stay a little":
                        print("The golem face softens and gives you a flower")
                        if "Flower" in player.inventory == False:
                            player.inventory.update({"Flower":1})
                        if "Flower" in player.inventory == True:
                            num1 = player.inventory.get("Flower")
                            num2 = num1 + 1
                            self.inventory.update({"Flower" : num2})


        else:
            print("Hello, you should prepare for the night.")





    def attack_zom(self):
        roundnum = 1
        
        while player.health > 0 and zombie.health > 0:
            print(f"Round {roundnum}")
            player.health -= (zombie.attack - player.defence)
            zombie.health -= (exta)
            roundnum += 1
            if player.health <= 0:
                print("The zombie Won")
                print ("You lose")
                sys.exit()
            if zombie.health <= 0:
                print("The zombie is dead")
                print ("You win")
        
    

    def attack_dro(self):
        roundnum = 1
        if drowned.health <= 0:
            print("The drowned is dead")
            print ("You win")
        while player.health > 0 and drowned.health > 0:
            print(f"Round {roundnum}")
            player.health -= (drowned.attack - player.defence)
            drowned.health -= exta
            roundnum += 1
        
    

    # def weapon_ch(self):
    #     print("You attack")
    #     print(player.weapons)
    #     if len(player.weapons) > 1:
    #         weapon_c = ("What weapon you want to use?")
    #         if weapon_c == "sword":

    #             exta0 = player.weapons.get("sword")
    #         elif weapon_c == "axe":
    #             exta1 = player.weapons.get("axe")
    #         elif weapon_c == "pickaxe":
    #             exta2 = player.weapons.get("pickaxe")
    #         elif weapon_c == "fists":
    #             exta3 = player.weapons.get("fists")
    #         exta = 4 + exta0 + exta1 +exta3
    #         pass

    def enemy_ch(self):    
        numran = random.randrange(1, 3)
        if numran  == 1:
            print("You are being attacked by a zombie")
            print(zombie)
            c =  input("Run\nAttack")
            if c == "Run":
                Player.run(player)
            elif c == "Attack":
                Player.weapon_ch(player)
                Player.attack_zom(player)
            else:
                print("You took to long to decide and it attacked you")
                print("Rip")
                sys.exit()

        elif numran == 2:
            print("You are being attacked by a drowned")
            print(drowned) 
            c =  input("Run\nAttack")
            if c == "Run":
                Player.run(player)
            elif c == "Attack":
                Player.weapon_ch(player)
                Player.attack_dro(player)
            else:
                print("You took  to long to decide and it attacked you")
                print("Rip")
                sys.exit()
        

    def run(self):
        print("You run")
        numran2 = random.randrange(1, 3)
        if numran2 == 1:
            print("You were able to escape")
            self.day += 1
        elif numran2 == 2:
            print("You weren't able to escape\nYou die")
            sys.exit()

        
        
        

class Location:
    def __init__(self, name, energy, description, actions, items):
        self.name = name
        self.energy = energy
        self.description = description
        self.actions = actions
        self.items = items
    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}, Actions: {self.actions}, Items you can get: {self.items} "
    
    def move():
        inp = input("Where do you want to move?")
        if inp != player.location:
            if inp == "village":
                Location.enter(player, inp)
            elif inp == "water":
                Location.enter(player, inp)
            elif inp == "spawn":
                Location.enter(player, inp)
            elif inp == "forest":
                Location.enter(player, inp)
            else:
                print("huh")
                Location.move()
        else:
            print("huh")
            Location.move()
    def enter(player, inp):
        player.location = inp



class Village_people:
    def __init__(self, name, types, attack, weapon):
        self.name = name
        self.types = types
        self.attack = attack
        self.weapon = weapon
    def __repr__(self):
        return f"Name: {self.name}, Type: {self.types} Attack damage: {self.attack}, Weapon: {self.weapon}"

villager1 = Village_people("Bill", "Fisher", 6, "Fishing pole")
villager2 = Village_people("Bob", "Blacksmith", 20, "Axes")
villager3 = Village_people("Joe", "Farmer/Baker", 5, "Hoe")
golem1 = Village_people("Golem", "Protector", 35, "Fists")
golem2 = Village_people("Golem", "Protector", 35, "Fists")
golem3 = Village_people("Golem", "Protector", 35, "Fists")

def night():
    print ("It is night time")
    if player.day == 1:
        print ("A villager hurries to you.")
        print ("Hurry, before the monsters come, I let you stay in my house tonight, tomorrow you are on your on.")
        print ("You hurry to his house and rest")
        player.day += 1
        player.energy += 45
        prompt()
    else: 
        Player.enemy_ch(player)









def prompt():
    print (player)
    loc = player.location
    if loc == "village":
        village = Location("Village", 5, "You are at the village, you see three villagers and three iron golems.", {"Move", "Talk to villagers"}, []) 
        print(village.actions)
    elif loc == "water":
        water = Location("Stream", 3, "You see a vass ocean with no other sign of life in sight", ["Cry", "Move"], [] ) 
        print(water.actions)
    elif loc == "forest":
        forest = Location("Forest", 5, "You enter the small forest, where there are many trees.", ["Cry", "Collect dirt", "Kill animals", "Look for food", "Get wood", "Move"], ["Food", "Wood"] ) 
        print(forest.actions)
    elif loc == "spawn":
        spawn = Location("Spawn", 1, "You find yourself in a small clearing", ["Cry",  "Collect dirt", "Kill animals", "Look for food", "Move"], ["Dirt", "Food"]) 
        print(spawn.actions)
    decision = input("What do you want to do?")
    if decision == "Cry":
        Player.cry(player)    
    elif decision == "Collect dirt":
        Player.collect_dirt(player)
    elif decision == "Kill animals":
        Player.kill_animals(player)
    elif decision == "Look for food":
        Player.look_food(player)
    elif decision == "Get wood":
        Player.wood(player)
    elif decision == "Move":
        Location.move()
    elif decision == "Talk to villagers" or "Talk" and player.location == "village":
        Player.talk(player)
    else:
        prompt()
    if int(player.energy) <= 0:
        night()




name = input("Hello, you wake up in the middle of an island in minecraft. \nThere is a village near by and a small forest. \nYou know you have to get ready of night fall. \nBefore you start, are you Alex or Steve or someone else?\n(There is no name changing. Choose wisely)")
player = Player(name, 45)
prompt()



while int(player.energy) >= 0:
    prompt()

while player.health >= 0:
    print("You died")
    sys.exit()