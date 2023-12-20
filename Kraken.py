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
        count = 1
        for item in beverage_list:
            bev_string += f"\n{count} - {item.name} .. ${item.price}"
            count += 1
        bev = int(input(f'{self.name} - Do you want:' + bev_string + '\n?: '))
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
        print ('\n')

    def play_pool(self):
        wager = int(input(f"How much would you like to wager, {self.name}?: $"))
        while wager > self.wallet or type(wager) !=int:
            wager = int(input(f"Oops, please enter a valid amount. You have ${self.wallet} in your wallet: $"))
        fifty_per = random.choice([True, False])
        if fifty_per is True:
            print("You won!")
            self.wallet += wager
            response = input("Would you like to play again? y or n: ")
            while response != 'y' and response !='n':
                response = input("Please choose 'y' or 'n' and press enter: ")
            if response == 'y':
                self.time += 2
                self.play_pool()
            elif response == 'n':
                print(f'Oh well, see ya around pal.\nYou have ${self.wallet} in your wallet.')
        else:
            self.wallet -= wager
            print(f"You lost! Pay up sucka'\nYou have ${self.wallet} left in your wallet.")
        self.time += 2
        print ('\n')

    def dance(self):
        choice = input(f'{self.name} - Do you want to dance\n(a) fast\n..or..\n(b) slow\n?: ')
        while choice != 'a' and choice != 'b':
            choice = input('Choose\n(a) fast\n..or..\n(b) slow')
        if choice == 'a':
            if self.energy >= 10:
                print(f"{self.name}: 'Woooooweeeeee yeahhhhhhh!!'")
                self.energy -= 10
                self.time += 3
            else:
                print(f"You don't have enough (10) energy to dance fast.\nYou have {self.energy} energy.")
                self.dance()
        else:
                print("Ooo yeah baby, come in a little closer.")
                self.energy -= 5
                self.time += 2
        print ('\n')
    
    def sell_crack(self):
        prob = random.randrange(0, (self.alc + 1))
        if prob < 3:
            self.wallet += 10
            print(f"{self.name} - You sold crack!\nYou now have ${self.wallet} in your wallet!\nDon't you just love crack, {self.name}?")
        elif prob >=3:
            print('''You drunk idiot! You went to the bathroom and DID crack. *__*''')
            self.energy *=2
        print ('\n')
    

                
            



num_of_players = int(input("How many players will be playing?\nEnter a number 1-4: "))
while num_of_players < 1 or num_of_players > 4:
    num_of_players = int(input("Enter a number 1-4: "))

player_dict = {}
for player in range(1, num_of_players + 1):
    player_dict[player] = Player(input(f'Enter player {player} name: '))

### Test Methods ###
player_dict[1].drink()
player_dict[2].play_pool()
player_dict[3].dance()
player_dict[4].sell_crack()