import random

launch_word = None
blank_counter = 0
launch_word_list = [blank_counter]
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

    for item in launch_word:
        for letter in item:
            global blank_counter
            blank_counter += 1
            launch_word_list.append(letter)

    return launch_word
    return launch_word_list
    return blank_counter



def check_wordList(guess):

    if  guess in launch_word_list:
        guessIndex = [launch_word_list.append(guess)]
        return True
        #return True

    else:
        return False

check_wordList
def guess():
    launch_word = game.launch_word
    launch_word_list = game.launch_word_list

    prev_guessCount = game.guess_number
    new_guessCount = game.guess_number + 1

    guessIndex = prev_guessCount - 1
    guesses = game.guesses

    print(guessIndex)
    print(guesses)

    guessing = True

    while guessing == True:

        guessQuery = input(("What letter would you like to guess? ({}/7 guesses) ").format(prev_guessCount))
        guess = guessQuery
        guesses.append(guess)

        #print(guess)

        if check_wordList(guess) == True:
            print("hit line 46")
            game.guess_number = prev_guessCount
            print("Correct!")

        else:
            print("incorrect")
            game.guess_number = new_guessCount

        print(guess)
        guessing = False

class spaceGame:

    #we'll use classes to make it easer to store our chose words and test number of letters
    def __init__(self, launch_word, launch_word_list, blanks):
        self.name = self
        self.launch_word = launch_word
        self.launch_word_list = launch_word_list
        self.blanks = blanks
        self.guess_number = 1
        self.guesses = []
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



def gameLoad():
    load = launch_word_load()
    print("Welcome to Spaceman. Try to guess the correct letters to launch the shuttle!")


gameLoad()

game = spaceGame(launch_word, launch_word_list, blank_counter)



launching = True

while launching:
    test()
    guess()
