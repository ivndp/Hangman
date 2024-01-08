import random
# List of words for guessing
word_list = ['ability', 'cabinet', 'absence', 'balance', 'calibre', 'academy', 'account', 'barrier', 'capable', 'accused', 'battery', 'capital', 'achieve', 'captain', 'acquire', 'caption', 'address', 'because', 'capture', 'advance', 'bedroom', 'careful', 
'adverse', 'believe', 'carrier', 'advised', 'beneath', 'caution', 'adviser', 'benefit', 'against', 'besides', 'central', 'airline', 'between', 'centric', 'airport', 'billion', 'century', 'alcohol', 'certain', 'alleged', 'brother', 'chamber', 'already', 'brought', 'channel', 'analyst', 'chapter', 'ancient', 'charity', 'another', 'decided', 'charlie', 'anxiety', 'decline', 'charter', 'anxious', 'default', 'checked', 'anybody', 'defence', 'chicken', 'applied', 'deficit', 'chronic', 'arrange', 'deliver', 'circuit', 'arrival', 'density', 'classes', 'article', 'deposit', 'classic', 'assault', 'desktop', 'climate', 'assumed', 'despite', 'assured', 'destroy', 'closure', 'attempt', 'develop', 'clothes', 'attract', 'devoted', 'collect', 'auction', 'diamond', 'college', 'average', 'digital', 'combine', 'eastern', 'discuss', 'comfort', 'economy', 'disease', 'command', 'edition', 'display', 
'comment', 'elderly', 'dispute', 'compact', 'element', 'distant', 'company', 'engaged', 'diverse', 'compare', 'enhance', 'divided', 'compete', 'essence', 'complex', 'concept', 'evident', 'dynamic', 'concern', 'exactly', 'factory', 'concert', 'examine', 'faculty', 'conduct', 'example', 'confirm', 'excited', 'failure', 'connect', 'exclude', 'fashion', 'consent', 'exhibit', 'feature', 'consist', 'expense', 'federal', 'contact', 'explain', 'contain', 'explore', 'fiction', 'content', 'express', 'fifteen', 'contest', 'extreme', 'context', 'gallery', 'finance', 'control', 'gateway', 'convert', 'general', 'correct', 'genetic', 'fitness', 'council', 'genuine', 'foreign', 'counsel', 'gigabit', 'forever', 'counter', 'greater', 'formula', 'country', 'fortune', 'crucial', 'forward', 'crystal', 'healthy', 'founder', 'culture', 'freedom', 'current', 'heavily', 'further', 'helpful', 'illegal', 
'jointly', 'illness', 'journal', 'herself', 'imagine', 'journey', 'highway', 'justice', 'himself', 'improve', 'justify', 'history', 'include', 'initial', 'holiday', 'inquiry', 'insight', 'kitchen', 'however', 'install', 'hundred', 'instant', 'machine', 'husband', 'instead', 'manager', 'intense', 'married', 'largely', 'interim', 'massive', 'involve', 'maximum', 'natural', 'learned', 'neither', 'measure', 'leisure', 'nervous', 'medical', 'liberal', 'network', 'liberty', 'neutral', 'mention', 'library', 'notable', 'message', 'license', 'million', 'limited', 'nowhere', 'mineral', 'nuclear', 'minimal', 'logical', 'minimum', 'loyalty', 'pacific', 'obvious', 'package', 'mission', 'offence', 'painted', 'mistake', 'officer', 'mixture', 'partial', 'monitor', 'partner', 'monthly', 'operate', 'passage', 'opinion', 'musical', 'optical', 'passion', 'mystery', 'organic', 'passive', 'portion', 
'outcome', 'patient', 'poverty', 'outdoor', 'pattern', 'precise', 'outlook', 'payable', 'predict', 'outside', 'payment', 'premier', 'overall', 'penalty', 'premium', 'proudly', 'prepare', 'project', 'pension', 'present', 'promise', 'prevent', 'promote', 'perfect', 'primary', 'protect', 'perform', 'printer', 'protein', 'perhaps', 'privacy', 'protest', 'phoenix', 'private', 'provide', 'problem', 'publish', 'picture', 'proceed', 'purpose', 'pioneer', 'process', 'plastic', 'produce', 'qualify', 'pointed', 'product', 'quality', 'popular', 'profile', 'quarter', 'section', 'success', 'radical', 'segment', 'suggest', 'railway', 'serious', 'summary', 'readily', 'service', 'support', 'suppose', 'reality', 'session', 'supreme', 'realise', 'surface', 'receipt', 'seventh', 'surgery', 'receive', 'several', 'surplus', 'recover', 'shortly', 'survive', 'reflect', 'suspect', 'regular', 'silence', 
'sustain', 'related', 'silicon', 'teacher', 'release', 'similar', 'telecom', 'remains', 'removal', 'sixteen', 'tension', 'removed', 'skilled', 'theatre', 'replace', 'therapy', 'request', 'society', 'thereby', 'require', 'somehow', 'thought', 'reserve', 'someone', 'through', 'resolve', 'speaker', 'tonight', 'respect', 'special', 'totally', 'respond', 'species', 'touched', 'restore', 'sponsor', 'towards', 'retired', 'station', 'traffic', 'revenue', 'storage', 'trouble', 'reverse', 'strange', 'rollout', 'stretch', 'typical', 'routine', 'student', 'uniform', 'studied', 'unknown', 'satisfy', 'subject', 'unusual', 'science', 'succeed', 'upgrade', 'whether', 'upscale', 'utility', 'variety', 'warrant', 'without', 'various', 'witness', 'vehicle', 'weather', 'venture', 'webcast', 'version', 'website', 'written', 'veteran', 'western', 'victory', 'weekend', 'whereas', 'welcome', 'whereby', 
'village', 'welfare', 'virtual', 'violent', 'visible']

# List of Hang Man arts
man = ["   _ _ _ _ _\n   |\n   |\n   |\n   |\n   |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |\n   |\n   |\n   |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |       |\n   |\n   |\n   |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |       |\n   |       O\n   |\n   |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |       |\n   |       O\n   |      /\n   |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |       |\n   |       O\n   |      / \\\n   |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |       |\n   |       O\n   |      /|\\\n   |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |       |\n   |       O\n   |      /|\\\n   |       |\n   |\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |       |\n   |       O\n   |      /|\\\n   |       |\n   |      /\n  /|\\\n / | \\\n/  |  \\\n",
"   _ _ _ _ _\n   |       |\n   |       |\n   |       O\n   |      /|\\\n   |       |\n   |      / \\\n  /|\\\n / | \\\n/  |  \\\n"]

# Hang Man main function
def hangman():
    answer = random.choice(word_list)
    wrong_guess = []
    right_guess = []
    trial = 9
    i = 1
    # Welcome message with a Hangman art
    print(f"Hello, welcome to Hangman.\nTry your best to guess a word combine of {len(answer)} letters.\nGood Luck!\n:)\n")
    print(man[0])
    # Start looping for the guess
    while i <= trial:
        print(trial_left(trial-i))
        guess = input("Guess a letter: ").lower()
        # Filter out the input that is not alphabet
        if not guess.isalpha():
            print(f"'{guess}' is not a valid guess.  Please input 1 alphabet letter.\n")
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
                print(f"Yay! The answer is {answer.capitalize()}! Well done!\n")
                # Ask if the user want to play again
                try_again = input("Want to try another game? (Y or N)").lower
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
    print(f"Sorry, you have used up all the trials.\nThe answer is {answer.capitalize()}\nGood luck next time.\n")
    try_again = input("Want to try another game? (Y or N)").lower
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