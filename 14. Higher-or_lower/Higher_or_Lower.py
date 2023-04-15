from game_data import data
import random

"""Choose a winner"""
def winner(choice1,choice2):
  choice1_scr = choice1["follower_count"]
  choice2_scr= choice2["follower_count"]
  if choice1_scr > choice2_scr:
    if guess == "a":
      return True
    else:
      return False
  else:
    if guess == "b":
      return True
    else:
      return False

"""Get data from dictionary"""
def name_format(choice):
  name = choice["name"]
  description = choice["description"]
  country = choice["country"]
  return f"{name}, a {description}, from {country}"

game_continue = True
score = 0
choice2 = random.choice(data) #Giving B's position to A'
while game_continue:
  choice1 = choice2
  choice2 = random.choice(data)
  if choice1 == choice2:
    choice2= random.choice(data)
  print(f"Compare A: {name_format(choice1)}")
  print(f"Compare B: {name_format(choice2)}")
  guess = input("Who has more followers? Type A or B?:\n").lower() 
  is_correct = winner(choice1,choice2)
  """Give feedback & keep score"""
  if is_correct:
    score += 1
    print(f"Thats correct, Your score is {score}")
  else:
    game_continue = False
    print(f"Thats wrong, You final Score is {score}")
  