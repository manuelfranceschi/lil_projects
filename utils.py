import random

class Character:
    health = 100
    mana = 50
    strength = 10
    magic = 20
    in_guard = False
    #status = 'normal'

    def __init__(self, name, turn = True, bot = False):
        self.name = name
        self.turn = turn
        self.bot = bot

    def attack(self, objective: object):
        if objective.in_guard == True:
            objective.health = objective.health - (self.strength - random.randint(5,7))
        else:
            objective.health = objective.health - self.strength
        return objective.health
    
    def defend(self):
        self.in_guard = True
        return self.in_guard
    
    def fire(self, objective: object):
        if self.mana > 15:
            if objective.in_guard == True:
                objective.health = objective.health - (self.magic - random.randint(3,5))
                #objective.status = 'on fire'
            else:
                objective.health = objective.health - self.magic
            self.mana = self.mana - 15
        else:
            print('you ran out of mana! turn lost')
        return objective.health
    
    def heal(self):
        if self.mana > 10:
            if self.health < 100:
                self.health = self.health + 15
                if self.health > 100:
                    self.health = 100
                self.mana = self.mana - 10
            else:
                print('you are at full health!')
        else:
            print('you ran out of mana! turn lost')
        return self.health
    
    # def escape():
    #     escape_probability = random.randint(1,4)
    #     if escape_probability == 4:
    #         print('You escaped succesfully!')
    #     else:
    #         print("it didn't work well..")
    #     return escape_probability
    
def display_combat(player1, player2):
    ux = print(f'  Health: {player1.health} \t\t\t Health: {player2.health}\n  Mana: {player1.mana} \t\t\t Mana: {player2.mana} \n {"*" * 13} \t\t\t {"*" * 13} \n    {player1.name} \t\t\t      {player2.name}')
    return ux

def player_decision(player: Character, objective):
    menu = ['attack', 'defend', 'fire', 'heal']   
    if player.bot == False:
        player_decision = input(f'what would you like to do? \n{menu} ->').lower()
    else:
        player_decision = random.choice(menu)

    match player_decision:
        case 'attack':
            player.attack(objective)
        case 'defend':
            player.defend()
        case 'fire':
            player.fire(objective)
        case 'heal':
            player.heal()
        # case 'escape':
        #     player.escape()
        case _:
            print('you chose a wrong action or write it wrong. you lost your turn!')
    return player_decision