import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# set the pictures in a list
images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

# input validation if user does not type in 0, 1, or 2
if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number, you lose.")
else:
  # random choice for the computer
  computer_choice = random.randint(0,2)
  # show image of user's choice
  print(images[player_choice])
  # output computer's choice along with image
  print("Computer chose:\n")
  print(images[computer_choice])
  # check who wins
  if player_choice == computer_choice:
    print("It's a tie.")
  elif player_choice == 0 and computer_choice == 2 or player_choice == 1 and computer_choice == 0 or player_choice == 2 and computer_choice == 1:
    print("You win.")
  elif player_choice == 0 and computer_choice == 1 or player_choice == 1 and computer_choice == 2 or player_choice == 2 and computer_choice == 0:
    print("You lose.")
