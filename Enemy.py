import random


class Enemy:
    enemies = ['vilager', 'cave man', 'cat', 'faker', 'X']
    def __init__(self, name):
        self.name = name
        if name == 'vilager':
            self.play_style = 'npc'
            self.damage = 2
            self.hp = 10
        elif name == 'cave man':
            self.play_style = 'rock'
            self.damage = 4
            self.hp = 15
        elif name == 'cat':
            self.play_style = 'copy cat'
            self.damage = 8
            self.hp = 20
        elif name == 'faker':
            self.play_style = 'fake'
            self.damage = 16
            self.hp = 20
        else:
            self.play_style = 'scam'
            self.damage = 20
            self.hp = 25
    def get_symbol(self):
        if(self.play_style == 'npc'):
            random_number = random.randint(1, 3)
            if random_number == 1:
                return "Rock"
            elif random_number == 2:
                return "Paper"
            else:
                return "Scissors"

        elif(self.play_style == 'rock'):
            random_number = random.randint(1, 10)
            if random_number<=6:
                return "Rock"
            elif random_number <= 8:
                return "Paper"
            else:
                return "Scissors"

        elif (self.play_style == 'faker'):
            random_number = random.randint(1, 3)
            random_number_dodge = random.randint(1, 100)
            if(random_number_dodge <=10):
                return "Dodge"
            if random_number == 1:
                return "Rock"
            elif random_number == 2:
                return "Paper"
            else:
                return "Scissors"

    @staticmethod
    def retrieve_defeated_enemies(num):
        return Enemy.enemies[:num]