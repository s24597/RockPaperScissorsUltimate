from Enemy import Enemy
from Player import Player

save = ''
name = ''
hp = 100


def save_file(player):
    with open('save.txt', 'w') as file:
        file.write(player.name + ',' + str(len(player.defeated_enemies)) + ',' + str(player.hp))


def clear_file():
    with open('save.txt', 'w') as file:
        file.write('')


def reduce_health(target, damage=5):
    if damage > target.hp:
        target.hp = 0
    else:
        target.hp += -damage


def player_lost():
    print("You lost!")
    clear_file()
    exit()


def player_won():
    print("You won!")
    decision = input("Do you want to restart game? (Y/N)")
    while decision != 'Y' and decision != 'N':
        print("Error! Choose (Y/N)")
        decision = input("Do you want to restart game? (Y/N)")
    if decision == 'N':
        print("Thank you for playing!")
        exit()
    if decision == 'Y':
        print("Thank you for playing! Your progress will be restarted. Please start game again")
        clear_file()
        exit()


def establish_winner(player_symbol, enemy_symbol):
    print("Your choice is: " + player_symbol + ' | Enemy choice: ' + enemy_symbol)
    if enemy_symbol == 'Dodge':
        print('Enemy dodged the atack')
        return 'Draw'
    if player_symbol == 'Rock':
        if enemy_symbol == 'Scissors':
            return 'Player Won'
        elif enemy_symbol == 'Paper':
            return 'Enemy Won'
        else:
            return 'Draw'
    elif player_symbol == 'Paper':
        if enemy_symbol == 'Rock':
            return 'Player Won'
        elif enemy_symbol == 'Scissors':
            return 'Enemy Won'
        else:
            return 'Draw'
    elif player_symbol == 'Scissors':
        if enemy_symbol == 'Paper':
            return 'Player Won'
        elif enemy_symbol == 'Rock':
            return 'Enemy Won'
        else:
            return 'Draw'


def match(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        incorrect_symbol = True
        player_symbol = ''
        while incorrect_symbol:
            player_symbol = input('Choose your symbol from: Rock, Paper, Scissors: ')
            if player_symbol == 'Rock' or player_symbol == 'Paper' or player_symbol == 'Scissors':
                incorrect_symbol = False

        enemy_symbol = enemy.get_symbol()
        enemy.copy = player_symbol
        winner = establish_winner(player_symbol, enemy_symbol)
        if winner == 'Player Won':
            print('The enemy\'s HP will be reduced')
            reduce_health(enemy)
        elif winner == 'Enemy Won':
            print('The player\'s HP will be reduced')
            reduce_health(player, enemy.damage)
        else:
            print("Its a draw")
        print("Your HP after this round: " + str(player.hp))
        print("Enemy HP after this round " + str(enemy.hp))
    if player.hp == 0:
        return player
    else:
        return enemy


def game():
    global save
    global hp
    global name
    try:
        with open('save.txt', 'r') as file:
            save = file.read()
    except FileNotFoundError:
        clear_file()

    if save == '':
        print("Welcome in game Rock Paper Scissors Ultimate!")
        name = input("Your name: ")
        while len(name) > 30 or name.strip() == '':
            print("Error! Name has to be shorter than 30 characters and cannot be empty.")
            name = input("Your name: ")
    else:
        name = save.split(',')[0]
        hp = int(save.split(',')[2])

    player = Player(name, hp)

    if save != '':
        player.defeated_enemies = Enemy.retrieve_defeated_enemies(int(save.split(',')[1]))
    while len(player.defeated_enemies) < len(Enemy.enemies):
        enemy_name = Enemy.enemies[len(player.defeated_enemies)]
        print(enemy_name)
        enemy = Enemy(enemy_name)
        print(enemy.hp)
        looser = match(player, enemy)
        if isinstance(looser, Player):
            player_lost()
        else:
            player.defeated_enemies.append(enemy.name)
            save_file(player)
    player_won()
