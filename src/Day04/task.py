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

import random

valid_input = False
while True :
    try:
        user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

        if user_input <= 2:
            break

    except ValueError:
        print("\n")
        try:
            if user_input > 2:
                print("Please enter a number between 0 and 2")
        except NameError:
            print("You must enter a number")




computer_choice = random.randint(0,2)

rock_paper_scissors = [rock, paper, scissors]

print(rock_paper_scissors[user_input])
print("Computer chose: ")
print(rock_paper_scissors[computer_choice])

if user_input == computer_choice:
    print("It's a draw!")
elif user_input == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_input == 2:
    print("Computer win!")
elif user_input > computer_choice:
    print("You win!")
elif computer_choice > user_input:
    print("Computer Win!")

