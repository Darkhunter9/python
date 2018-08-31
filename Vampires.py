# Taken from mission The Defenders

class Warrior:
    def __init__(self):
        self.healthmax = 50
        self.health = 50
        self.attack = 5
        self.defend = 0
        self.vampirism = 0
        self.is_alive = True

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.healthmax = 60
        self.health = 60
        self.attack = 3
        self.defend = 2

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.healthmax = 40
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5

def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        if unit_1.attack >= unit_2.defend:
            unit_2.health -= (unit_1.attack-unit_2.defend)
            unit_1.health += (unit_1.attack-unit_2.defend)*unit_1.vampirism
            unit_1.health = min(unit_1.healthmax,unit_1.health)
            if unit_2.health <= 0:
                unit_2.is_alive = False
                return True
        if unit_2.attack >= unit_1.defend:
            unit_1.health -= (unit_2.attack-unit_1.defend)
            unit_2.health += (unit_2.attack-unit_1.defend)*unit_2.vampirism
            unit_2.health = min(unit_2.health,unit_2.healthmax)
            if unit_1.health <= 0:
                unit_1.is_alive = False
                return False

class Army:
    def __init__(self):
        self.group = []
    
    def add_units(self,role,n):
        for i in range(n):
            self.group.append(role())

class Battle:
    def fight(self,army1,army2):
        while army1.group and army2.group:
            a = fight(army1.group[0],army2.group[0])
            if a:
                army2.group.pop(0)
                if not army2.group:
                    return True
            else:
                army1.group.pop(0)
                if not army1.group:
                    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
