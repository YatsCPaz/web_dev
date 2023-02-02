from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#
## Creamos nuestra lista del 1 al 100.
think_number = []
for num in range(1,101):
    think_number.append(num)
# print(think_number)
#
## We chose a random number.
answer = random.choice(think_number)
print(f"Pssst, the correct answer is {answer}")
#
## Choose a difficulty level.
difficulty = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
# print(difficulty)
attempts = 5
if difficulty == "easy":
    attempts = 10
#
## Guessing the number
game_over = False
while not game_over:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    # if guess == answer:
    #     print("YOU WIN !!")
    #     attempts = 0
    if guess > answer:
        print("Too high.")

    elif guess < answer:
        print("Too low.")

    else:
        print("YOU WIN !!")
        game_over = True

    attempts -= 1
    if attempts < 1:
        game_over = True
        print("You've run out of guesses, YOU LOSE !!")
    else:
        print("Guess again.")



