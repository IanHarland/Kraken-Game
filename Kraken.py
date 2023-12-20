import math
import random

print('\nWELCOME TO THE KRAKEN, the greatest bar ever!\n\nWe play a little game here at the Kraken called "Getting really drunk!"\nThe object of the game is to get as drunk as possible!\nBut be careful, or you might find yourself in trouble!\n\n* Note: If anything strange happens in the terminal or you want to quit, type "control^ + c" to EXIT, then "clear" to CLEAR the terminal. \n\n')
total_time_elapsed = 1

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
add_beverage(Beverage('shot', 1 , 8, 10))
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
            if self.aids >= 3:
                print("You're dead from AIDS.")
                return
            available_methods = []
            if self.alc * 2 <= self.time and self.wallet >= 6:
                available_methods.append('drink')
            if self.wallet > 0:
                available_methods.append('play pool')
            if self.energy >= 10:
                available_methods.append('dance')
            if self.energy >= 5 and total_time_elapsed >= 1:
                available_methods.append('sell crack')
            if self.time > 3 and self.energy >= 20:
                available_methods.append('suck dick')
            available_methods.append('go to work')
            user_choice_string = ""
            count = 1
            for item in available_methods:
                user_choice_string += f'\n{count} - ' + item
                count += 1
            user_choice_index = input(f"({total_time_elapsed}) {self.name} - choose one of the following actions:{user_choice_string}\n: ")
            if user_choice_index.isdigit() == False:
                self.choose_action()
            user_choice_index = int(user_choice_index)
            if user_choice_index not in range(1, len(available_methods) + 1):
                self.choose_action()
            if available_methods[user_choice_index - 1] == 'drink':
                self.drink()
            elif available_methods[user_choice_index - 1] == 'play pool':
                self.play_pool()
            elif available_methods[user_choice_index - 1] == 'dance':
                self.dance()
            elif available_methods[user_choice_index - 1] == 'sell crack':
                self.sell_crack()
            elif available_methods[user_choice_index - 1] == 'suck dick':
                self.suck_dick()
            elif available_methods[user_choice_index - 1] == 'go to work':
                self.go_to_work()
        
        
    
    def drink(self):
        bev_string = ""
        count = 1
        for item in beverage_list:
            bev_string += f"\n{count} - {item.name} .. ${item.price}"
            count += 1
        bev = int(input(f'\n{self.name} - Do you want:' + bev_string + '\n?: '))
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
                print ('\n')
                self.play_pool()
            elif response == 'n':
                print(f'Oh well, see ya around pal.\nYou have ${self.wallet} in your wallet.')
                print ('\n')
        else:
            self.wallet -= wager
            print(f"You lost! Pay up sucka'\nYou have ${self.wallet} left in your wallet.")
            print ('\n')
        self.time += 1
        

    def dance(self):
        choice = input(f'{self.name} - Do you want to dance\n(a) fast\n..or..\n(b) slow\n?: ')
        while choice != 'a' and choice != 'b':
            choice = input('Choose\n(a) fast\n..or..\n(b) slow\n: ')
        if choice == 'a':
            if self.energy >= 10:
                print(f"\n{self.name}: 'Woooooweeeeee yeahhhhhhh!!'")
                self.energy -= 10
                self.time += 1
            else:
                print(f"You don't have enough (10) energy to dance fast.\nYou have {self.energy} energy.")
                self.dance()
        else:
                print("Ooo yeah baby, come in a little closer.")
                self.energy -= 5
                self.time += 1
        print ('\n')
    
    def sell_crack(self):
        prob = random.randrange(0, (self.alc + 1))
        if prob < 1:
            self.wallet += 10
            self.energy -= 10
            print(f"\n{self.name} - You sold crack!\nYou now have ${self.wallet} in your wallet!\nDon't you just love crack, {self.name}?")
        else:
            print('''\nYou drunk idiot! You went to the bathroom and DID crack. *__*''')
            self.energy *=2
        self.time += 3
        print ('\n')
    
    def suck_dick(self):
        prob = random.randrange(0, (self.alc + 1))
        if prob < 2:
            self.wallet += 50//(self.alc/2 + 1)
            print(f"\nCongratulations! You sucked dick in the bathroom, {self.name}. You're doing great for yourself!\nYour Wallet: ${self.wallet}")
            if random.choice([1,2]) == 1:
                self.aids += 1
                print(f"Oh no! You got an AIDS.\nYou have a total of {self.aids} AIDS.")
        else:
            print("\nYou poor lonely soul. You went to the bathroom and tried (unsuccessfully) to suck your own dick.")
        self.time += 3
        self.energy -= 20
        print ('\n')

    def go_to_work(self):
        self.wallet += 20
        self.time += 6


    

                
            

num_of_players = int(input("How many players will be playing?\nEnter a number 1-5: "))
while num_of_players < 1 or num_of_players > 5:
    num_of_players = int(input("Enter a number 1-5: "))

player_dict = {}
for player in range(1, num_of_players + 1):
    player_dict[player] = Player(input(f'Enter player {player} name: '))

player_choice_length_of_game = input('How long would you like the game to be?\nEnter a numer less than 100: ')
while (player_choice_length_of_game.isdigit() == False) or (int(player_choice_length_of_game) < 1):
    player_choice_length_of_game = input('How long would you like the game to be?\nEnter a number less than 100: ')

while total_time_elapsed <= int(player_choice_length_of_game):
    players_list_times = []
    for player in range(1, num_of_players + 1):
        players_list_times.append(player_dict[player].time)
    min_time = min(players_list_times)
    min_time_index = players_list_times.index(min_time)
    current = player_dict[min_time_index + 1]
    print(f"\n{current.name} Stats:\nTime Spent: {current.time} hours\nAlcohol Intake: {current.alc}\nWallet: ${current.wallet}\nEnergy: {current.energy} Energies\nAids: {current.aids}\n")
    current.choose_action()
    total_time_elapsed += 1


players_alc_list = []
for player in range(1, num_of_players + 1):
        players_alc_list.append(player_dict[player].alc)
max_alc = max(players_alc_list)
winners = []
for player in player_dict.items():
    if player[1].alc == max_alc:
        winners.append(player[1].name)
for winner in winners:
    print(f"\n{winner} won! They drank {max_alc} total alcohols!\nWe should all try to be more like {winner} and drink more!")
print("/n\nGAME OVER\n\nThanks for playing!")


### Test Methods ###
# player_dict[1].drink()
# player_dict[2].play_pool()
# player_dict[3].dance()
# player_dict[4].sell_crack()
# player_dict[5].suck_dick()
# player_dict[1].choose_action()
    
