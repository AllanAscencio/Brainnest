# --------------------------------- imports ---------------------------------- #
import random
from hangman_words import word_list
from hangman_art import logo, stages
# --------------------------------- imports ---------------------------------- #

'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''

# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''

# We start printing the logo of the game
print(logo)

# We select a random choice from our list of words
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []

# We add _ for every letter in the random word we picked
for each_letter in chosen_word:
    display += "_"

# The amount of lives is hardcoded as requested
lives = 6

# Firs of all we start with a while loop, so we can come back until we ran out of lives or until we win
while '_' in display:
    # We transform the input to lower case
    guess = input("Guess a letter: ").lower()
    # Here we are checking if we already guessed the letter correctly
    if guess in display:
        print(f'You have already guessed {guess}')
    # Here we check of the position of the letter we just inputed
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # if the letter is there, we put it and replace it where the correct '_' is
        if letter == guess:
            display[position] = letter
    # If our guessed letter is not in the chosen word we tell the user, and we subtract a life
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # If we get lifes to 0 we tell the user that has lost the game
        if lives == 0:
            print(stages[lives])
            print("You lost the game! Run it again and try to win")
            break

    print(f"{' '.join(display)}")
    # if the user wins we output the result and the amount of lives the user had left
    if '_' not in display:
        print(f"You win! you had {lives} lives left")
    # Here we print the corresponding stage depending on the wins or loses the user has
    print(stages[lives])

    """ The logo and the hangman were
     taken from ascii generators"""