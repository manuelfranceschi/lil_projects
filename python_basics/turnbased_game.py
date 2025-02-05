import time
from utils import Character, display_combat, player_decision

print('welcome! This is a mini turn based game, where you can play against a bot. Here I am testing some python basics so as OOP structure. \n')
time.sleep(3)

name = input('lest play! tell me your name ->')
player = Character(name)
bot = Character('Bot',turn= False, bot= True)
round = 1
while player.health > 0 and bot.health > 0:
    display_combat(player, bot)
    print(f'Round: {round}')
    
    if player.turn == True:
        player.in_guard = False
        print('your turn!')
        decision = player_decision(player, bot)
        print(f'{player.name} chose {decision}!')
        player.turn = False
        bot.turn = True
        time.sleep(2)

    elif bot.turn == True:
        bot.in_guard = False
        print(f"{bot.name}'s turn!")
        decision = player_decision(bot, player)
        print(f'{bot.name} chose {decision}!')
        player.turn = True
        bot.turn = False
        time.sleep(2)

    round = round + 1
display_combat(player, bot)

if player.health < 0:
    print(f"{bot.name} Wins!")
elif bot.health < 0: 
    print(f"{player.name} Wins!")