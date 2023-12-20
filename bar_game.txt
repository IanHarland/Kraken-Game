import random
import math
the_time = 0

class Bartender:
  def __init__(self, name, gender_male, experience, overworked = False, time_worked = 1, drinks_served = 0):
    self.name = name
    self.gender_male = gender_male
    self.experience = experience
    self.overworked = overworked
    self.time = time_worked
    self.drinks = drinks_served

  def pour_drink(self):
    self.drinks += 1
    if self.drinks >= self.time:
      self.overworked = True
    if self.overworked == False:
      self.time += .2
      if random_drinker.is_drunk == False:
        print(self.name + ": Here you go.")
    if self.overworked == True:
      self.time += .3

    self.get_snappy()
    print("(You've had " + str(random_drinker.drinks_had) + " drinks in {} hours)".format(random_drinker.time_spent))

  def get_snappy(self):
    bitter_phrases = ["'Fuckin' hell'", "'This prick'", "'Get me out of here'"]
    random_bitter = random.choice(bitter_phrases)
    if self.overworked == True:
      print("{name} mutters: {bitter} and hands you your drink.".format(name=self.name, bitter=random_bitter))
  
  def clean_bar(self):
    self.time += .25
    print(self.name + " cleans the bar.")

class Drinker:
  def __init__(self, name, drinks_had = 0, time_spent = 1):
    self.name = name
    self.drinks_had = drinks_had
    self.time_spent = time_spent
    self.is_drunk = False
  
  def order_drink(self, bartender):
    starter_question = input('{} -- do you want to drink? y/n: '.format(self.name))
    if starter_question == 'y':
      drink = input("{}: What do you want {}? ".format(random_bartender.name, self.name))
      if self.drinks_had < 2*self.time_spent and bartender.gender_male == True:
        print(self.name + ": Hey man, can I get a {}, please".format(drink))
        self.drinks_had += 1
      elif self.drinks_had < 2*self.time_spent and bartender.gender_male == False:
        print(self.name + ": Excuse me ma'am, can I get a {}, please".format(drink))
        self.drinks_had += 1
      elif self.drinks_had >= 2*self.time_spent and bartender.gender_male == True:
        print(self.name + ": Hey motherfucker, get me a {}, will ya?".format(drink))
        print(bartender.name + ": Take this and get the hell away from my bar!")
        print("--" + self.name + " takes a big gulp and stumbles off")
        self.drinks_had += 1
      elif self.drinks_had >= 2 and bartender.gender_male == False:
        print(self.name + ": Hey sexy, bring those tits over here with a nice cold {}".format(drink))
        print(bartender.name + ": This is your last for now scumbag. Go fuck yourself.")
        print("--" + self.name + " laughs and stumbles off.")
        self.drinks_had += 1
    elif starter_question == 'n':
      return
    else:
      print("Type 'y' or 'n' then Enter")
      self.order_drink(random_bartender)
    
    if self.drinks_had/self.time_spent >2:
      self.is_drunk = True
    if self.is_drunk == True:
      print("(You're drunk)")
    bartender.pour_drink()

  def play_pool(self):
    choose_pool = input("Want to play pool, {}? y/n: ".format(self.name))
    while choose_pool == "y":
      self.time_spent += .25
      pool_list = ["You won! Play again?", "You lost, too bad."]
      random_pool_outcome = random.choice(pool_list)
      print(random_pool_outcome)
      if random_pool_outcome == "You won! Play again?":
        choose_pool = input("y/n: ")
      else:
        return
      if choose_pool != 'y' and choose_pool != 'n':
          print("oops, type 'y' or 'n' then press Enter")
          choose_pool = ("y/n")
    if choose_pool == 'n':
      return
    else:
      print("please type 'y' or 'n' then press Enter")
      self.play_pool()
  
  def dance(self):
    choose_dance = input("Want to dance, {}? y/n: ".format(self.name))
    if choose_dance == "y":
      self.time_spent += .25
      dance_moves = ['The Coaster', 'The Twist', 'The Two Step']
      print(self.name + " goes to the dancefloor and dances " + random.choice(dance_moves))
    elif choose_dance == 'n':
      return
    else:
      print("please type 'y' or 'n' then press Enter")
      self.dance()

bartender_1 = Bartender("Sarah", False, 15)
bartender_2 = Bartender("Vinnie", True, 5)
bartenders = [bartender_1, bartender_2]

drinker_1 = Drinker(input("Player 1 name: "))
drinker_2 = Drinker(input("Player 2 name: "))
drinkers = [drinker_1, drinker_2]
random_drinker = random.choice(drinkers)
drunk_jail = []
drunk_jail_names = []

index = 0

while len(drinkers) > 0:
    
  random_drinker = random.choice(drinkers)
  random_bartender = random.choice(bartenders)
  random_number = random.choice(range(3))

  if index%3 == 2 and random_bartender.overworked == False:
    random_bartender.clean_bar()
  index += 1
  
  if random_number == 0:
    random_drinker.order_drink(random_bartender)
  elif random_number == 1:
    random_drinker.play_pool()
  else:
    random_drinker.dance()

  if random_drinker.is_drunk == True:
    drunk_jail.append(random_drinker)
    if len(drunk_jail) != 0:
      drunk_jail_names.append(drunk_jail[-1].name)
  if random_drinker.is_drunk == True:
    drinkers.pop(drinkers.index(random_drinker))
      
for i in drunk_jail_names:
  print(i + " is in drunk jail.")