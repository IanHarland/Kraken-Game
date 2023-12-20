import math
import random

class Beverage:
    def __init__(self, name, alc, price, energy):
        self.name = name
        self.alc = alc
        self.price = price
        self.energy = energy

beverage_list = []
def add_beverage(bev_instance):
    beverage_list.append(bev_instance)
add_beverage(Beverage('beer', 1, 6, 5))
add_beverage(Beverage('shot', 1.5 , 6, 10))
add_beverage(Beverage('mixed drink', 2, 10, 10))

class Player:
    def __init__(self, name):
        self.name = name
        self.time = 1
        self.alc = 0
        self.wallet = 20
        self.aids = 0
        self.energy = 10
    
    def choose_action(self):
        pass
    
    def drink(self):
        bev_string = ""
        for item in beverage_list:
            count = 1
            bev_string += f"\n{count} - {item.name} .. ${item.price}"
            count += 1
        bev = int(input('Do you want:' + bev_string + '\n?: '))
        while bev not in range(1, 1 + len(beverage_list)):
            bev = int(input(f"Oops, choose a number from 1 to {len(beverage_list)}: "))
        beverage = beverage_list[bev - 1]
        if beverage.price > self.wallet:
            print(f"You only have ${self.wallet} in your wallet. Pick a different drink")
            self.drink()
        else:
            self.wallet -= beverage.price
            self.alc += beverage.alc
            self.energy += beverage.energy
        print(f"Your total alcohol consumed is {self.alc} and you have ${self.wallet} in your wallet. You have {self.energy} energy.")
        self.time += 1

    def play_pool(self, wager):
        fifty_per = random.choice([True, False])
        if fifty_per is True:
            print("You won!")
            self.wallet += wager
            response = input("Would you like to play again? y or n: ")
            while response != 'y' or response !='n':
                response = input("Please choose 'y' or 'n' and press enter: ")
            if response == 'y':
                self.time += 2
                new_wager = input(f'How much do you want to wager?You have ${self.wallet} in your wallet.')
                while type(new_wager) != int or new_wager > self.wallet:
                    new_wager = input('Oops, please enter a number of dollars to wager.') 
                self.play_pool(new_wager)
            elif response == 'n':
                print('Oh well, see ya around pal.')
        else:
            print("You lost! Pay up sucka'")
            self.wallet -= wager
        self.time += 2

player1 = Player(input("Player 1: "))
player2 = Player(input("Player 2: "))

player1.drink()