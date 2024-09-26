import random



class Person: 
    def __init__(self, name, health, power, attack, attack_stat, defence, defence_stat, vehicle) :
        self.name = name
        self.health = health
        self.power = power
        self.attack = attack
        self.attack_stat = attack_stat
        self.defence  =  defence
        self.defence_stat = defence_stat
        self.vehicle = vehicle
    def __repr__(self):
        return f"Name: {self.name}, Health: {self.health}, Power: {self.power}, Attack: {self.attack}, Attack damage: {self.attack_stat}, Defence: {self.defence}, Defence stat: {self.defence_stat}, Vehicle: {self.vehicle} "



superhero1 = Person("Bobby", 435, "magnetic", "metal throw", 99, "metal defence", 120, "plane")
villian = Person("Jack", 540, "elements", "Element attack", 140, "element shield", 65, "none")        



print(superhero1)
print(villian)

def sf():
    answer = (input("Should the fight start?")).lower()
    if answer == "yes":
        fight()
    elif answer == "no":
        sf()


va = int(villian.attack_stat) - int(superhero1.defence_stat)
sha = int(superhero1.attack_stat) - int(villian.defence_stat)


def hero_health():
    superhero1.health = int(superhero1.health) - int(va)

def villian_health():
    villian.health = int(villian.health) - int(sha)

def villian_attack():
    hero_health()
    print(f"{villian.name} attacks!\n{villian.name} does {va} damage!\n{superhero1.name} has {superhero1.health}")

def superhero_attack():
    villian_health()
    print(f"{superhero1.name} attacks!\n{superhero1.name} does {va} damage!\n{villian.name} has {villian.health}")

def one():
    superhero_attack()
    villian_attack()

def two():
    villian_attack()
    superhero_attack()


def fight():
    print("fight")
    roundnum = 1

    while superhero1.health > 0 and villian.health > 0:
        print(f"Round {roundnum}")
        turn = random.randrange(1, 3)
        if turn ==  1:
            one()
        elif turn ==2:
            two()
        roundnum += 1

sf()