import random

launch_word = None
blank_counter = []
launch_word_list = []
def launch_word_load():
    # we'll use this one function to load, split and save our word as a whole word and a list

    f = open('word_bank.py', 'r')

    words_list = f.readlines()
    f.close()

    word_generate = words_list[0].split(' ')
    space_word = random.choice(word_generate)

    global launch_word
    launch_word = space_word

    global launch_word_list

    for letter in launch_word:
            launch_word_list.extend(letter)

    for blank in launch_word_list:
        blank_counter.append('_')

    return launch_word
    return launch_word_list
    return blank_counter

# will be used to replace guesses with blanks

def blankify(guessIndex, guess):

    game.launch_word_list[0][guessIndex] = guess

    print(launch_word_list[0])

def check_wordList(guess):

    if  guess in launch_word_list:
        # game.guessIndex.append(launch_word_list.index(guess))
        print("game.guessIndex: ")
        print(game.guessIndex)
        print("global launch_word_list")
        print(launch_word_list)
        return True
        #return True

    else:
        return False

def guess():
    launch_word = game.launch_word
    launch_word_list = game.launch_word_list

    prev_guessCount = game.guess_number
    new_guessCount = game.guess_number + 1

    guessIndex = game.guessIndex
    blankedGuesses = game.blankedWord

    guessNumber = prev_guessCount - 1

    print(guessIndex)

    guessWrong = 0

    while guessWrong <= 7:

            guessQuery = input(("What letter would you like to guess? ({}/7 guesses) ").format(prev_guessCount))
            guess = str(guessQuery)
            indexedGuess = int(game.launch_word_list.index(guess))
            print(guess)


            if check_wordList(guess) == True:

                game.guess_number = prev_guessCount
                blankedGuesses[indexedGuess].append(guess)
                print("Correct!")
                blankify(indexedGuess, guess)
                game.launch_word_list.pop(indexedGuess)


            else:
                print(("{} is incorrect").format(guess))
                # guessIndex.append([1[guess]])
                game.guess_number = new_guessCount
                guessWrong += 1



class spaceGame:

    #we'll use classes to make it easer to store our chose words and test number of letters
    def __init__(self, launch_word, launch_word_list, blank_counter):
        self.name = self
        self.launch_word = launch_word
        self.launch_word_list = launch_word_list
        self.blankedWord = blank_counter
        self.guess_number = 1
        self.guessIndex = []
'''
    def launch_guess(self):
        guess_wordList = game.launch_word_list
        guessCount = game.guess_number
        guessIndex = guessCount - 1
        guesses = game.guesses

        print(guessIndex)
        print(guesses)
        guess = input(("What letter would you like to guess? ({}/7 guesses) ").format(guessCount))

print(guess)

for i in guess_wordList:
    if guess == guess_wordList[i]:
        print("hit line 46")
        guess_output = guess_wordList[i]
'''
#chooses a random word and sets it to our launch_word


    #def space_word_index():


def test():
    print("our launch_word is " + game.launch_word)
    print(game.launch_word_list)
    print(game.blankedWord)
'''
    assert
'''


def gameLoad():
    load = launch_word_load()
    print("Welcome to Spaceman. Try to guess the correct letters to launch the shuttle!")


gameLoad()

game = spaceGame(launch_word, launch_word_list, blank_counter)



launching = True

while launching:
    test()
    guess()
