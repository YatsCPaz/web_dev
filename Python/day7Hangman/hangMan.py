#Step 5

# from replit import clear
import random
import hangMan_art, hangMan_words

# import importlib, importlib.util
 
# def module_directory(name_module, path):
#     P = importlib.util.spec_from_file_location(name_module, path)
#     import_module = importlib.util.module_from_spec(P)
#     P.loader.exec_module(import_module)
#     return import_module
 
# art_hangman = module_directory("art_hangman", "../artz/hangMan_art.py")
# word_hanman = module_directory("word_hanman", "../artz/hangMan_words.py")
 
# print(result.sub(3,2))
# print(result.lower_case('SaFa'))

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangMan_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangMan_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clear()
    print("\x1B[2J")

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You already guess: {guess} ... :P")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed: {guess}, that's not in the word, you loose a live ({lives}) :( ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangMan_art.stages[lives])