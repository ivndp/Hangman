import random
# Read a list of words for guessing from file
word_list = []
with open("words.txt", "r") as file:
    for line in file:
        word_list.append(line.strip().lower())

# List of Hang Man arts
man = ["   _________\n   |\n   |\n   |\n   |\n   |\n   |\n  /|\\\n / | \\\n/  \
|  \\\n",
"   _________\n   |       |\n   |\n   |\n   |\n   |\n   |\n  /|\\\n / | \\\n/ \
 |  \\\n",
"   _________\n   |       |\n   |       |\n   |\n   |\n   |\n   |\n  /|\\\n / \
| \\\n/  |  \\\n",
"   _________\n   |       |\n   |       |\n   |       O\n   |\n   |\n   |\n  /\
|\\\n / | \\\n/  |  \\\n",
"   _________\n   |       |\n   |       |\n   |       O\n   |      /\n   |\n  \
 |\n  /|\\\n / | \\\n/  |  \\\n",
"   _________\n   |       |\n   |       |\n   |       O\n   |      / \\\n   |\
\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _________\n   |       |\n   |       |\n   |       O\n   |      /|\\\n   |\
\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _________\n   |       |\n   |       |\n   |       O\n   |      /|\\\n   | \
      |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _________\n   |       |\n   |       |\n   |       O\n   |      /|\\\n   | \
      |\n   |      /\n  /|\\\n / | \\\n/  |  \\\n",
"   _________\n   |       |\n   |       |\n   |       O\n   |      /|\\\n   | \
      |\n   |      / \\\n  /|\\\n / | \\\n/  |  \\\n"]

# Hang Man main function
def hangman():
    answer = random.choice(word_list)
    wrong_guess = []
    right_guess = []
    trial = 9
    i = 1
    # Welcome message with a Hangman art
    print(f"Hello, welcome to Hangman.\nTry your best to guess a word combine \
of {len(answer)} letters.\nGood Luck!\n:)\n")
    print(man[0])
    # Start looping for the guess
    while i <= trial:
        print(trial_left(trial-i+1))
        guess = input("Guess a letter: ").lower()
        # Filter out the input that is not alphabet
        if not guess.isalpha():
            print(f"'{guess}' is not a valid guess.  Please input 1 alphabet \
letter.\n")
        # Filter out the guess is more than 1 letter
        elif len(guess) > 1:
            print(f"'{guess}' is not A letter.  Please only input 1 letter.\n")
        # Tell user the guess is repeated
        elif guess in wrong_guess or guess in right_guess:
            print(f"You have tried '{guess.upper()}' before.  Try again!\n")
        # Right guess time
        elif guess in answer:
            print(f"Yes, '{guess.upper()}' is inside the word.\n")
            # Put the letter inside the list of right guesses
            right_guess.append(guess)
            right_guess.sort()
            print(guess_display(answer, right_guess))
            print(f"Right guess: {right_guess}")
            print(f"Wrong guess: {wrong_guess}\n")
            # Check if get the whole word right
            if win_check(answer, right_guess):
                print(f"Yay! The answer is {answer.capitalize()}! Well done!\
\n")
                # Ask if the user want to play again
                try_again = input("Want to try another game? (Y or N) ").lower
                if try_again == "yes" or try_again == "y":
                    hangman()
                else:
                    return
        # Wrong guess time
        else:
            print(f"Sorry, '{guess.upper()}' is not inside the word.\n")
            # Put the letter inside the list of wrong guesses
            wrong_guess.append(guess)
            wrong_guess.sort()
            # Trial -1 and print out the Hangman art
            i += 1
            print(guess_display(answer, right_guess))
            print(man[i-1])
            print(f"Right guess: {right_guess}")
            print(f"Wrong guess: {wrong_guess}\n")
    # End of while loop means out of trials, print out game over message
    print(f"Sorry, you have used up all the trials.\nThe answer is \
{answer.capitalize()}\nGood luck next time.\n")
    try_again = input("Want to try another game? (Y or N) ").lower
    if try_again == "yes" or try_again == "y":
        hangman()
    else:
        return

# Function to display the word with hints of correct letter(s)
def guess_display(answer, guessed):
    display_word = ""
    for i in answer:
        if i in guessed:
            display_word += i + " "
        else:
            display_word += "_ "
    return display_word

# Function to check if all the letters in the answer are hit
def win_check(answer, guessed):
    correct_count = 0
    for i in answer:
        for j in guessed:
            if i == j:
                correct_count += 1
    return correct_count == 7

# Function for "Trials left" message
def trial_left(num):
    if num > 1:
        phrase = f"You've got {num} trials left."
        return phrase
    else:
        phrase = f"You've got only 1 trial left.  Make your guess wisely."
        return phrase

hangman()