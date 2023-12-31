# "Rock Paper Scissors" Game

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

# TODO 1: Generating a random choice of the computer:
import random
options = [rock, paper, scissors]
rand_nr = random.randint(0, 2)
choice_computer = options[rand_nr]

# TODO 2: Asking a user for an input (Rock/Paper/Scissors):
choice_human = input(
    "What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")

if choice_human == "0":
    print(options[0])

elif choice_human == "1":
    print(options[1])
else:
    print(options[2])

# TODO 3: Informing a user about a computer's choice:
print(f"Computer chose: \n {choice_computer}")

# TODO 4: Determining the winner:
if ((choice_human == "0" and rand_nr == 0) or (choice_human == "1" and rand_nr == 1) or (choice_human == "2" and rand_nr == 2)):
    print("It is a tie!")
elif choice_human == "0" and rand_nr == 1:
    print("Computer won!")
elif choice_human == "1" and rand_nr == 0:
  print("You won!")
elif choice_human == "0" and rand_nr == 2:
  print("You won!")
elif choice_human == "2" and rand_nr == 0:
  print("Computer won!")
elif choice_human == "1" and rand_nr == 2:
  print("Computer won!")
elif choice_human == "2" and rand_nr == 1:
  print("You won!")
else:
  print("Check the input data!")
