import my_hand
import random


user_choice = int(input("What do you choose? 0 - rock, 1 - paper or 2 - scissors. \n"))
computer = random.randint(0,2)

if user_choice < 0 or user_choice >=3:
    print("You chose wrong, you lose !!")
else:
    print(my_hand.hand[user_choice])
    print(f"\nComputer chose: {computer}\n")
    print(my_hand.hand[computer])

    if user_choice < 0 or user_choice >=3:
        print("You chose wrong, you lose !!")
    elif user_choice == 0 and computer == 2:
        print ("You Win !!")
    elif computer == 0 and user_choice == 2:
        print ("You lose ...")
    elif computer > user_choice:
        print("You lose ...")
    elif user_choice > computer:
        print("You Win !!")
    elif computer == user_choice:
        print ("It's a draw ...")



