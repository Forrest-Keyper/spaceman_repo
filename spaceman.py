import random

launch_word = None
launch_word_list = None

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
    launch_word_list = space_word.split(',')

    return launch_word
    return launch_word_list

def space_word_check(space_word):
    print (space_word)

class spaceGame:

    #we'll use classes to make it easer to store our chose words and test number of letters
    def __init__(self, launch_word, launch_word_list):
        self.name = self
        self.launch_word = launch_word
        self.launch_word_list = launch_word_list
        self.guess_number = 0
        self.guesses = []

    def launch_guess(self):
        guess_wordListed = game.launch_word_list
        guessescount = game.guess_number
        guesses = game.guesses

        guesses[guessescount] = input("What letter would you like to guess? ({}/7 guesses remaining) ").format(guessescount)
        guessescount += 1

        for i in guess_wordListed:
            if guesses[guessescount] == guess_wordListed[i]:
                print("hit line 46")
                guess_output = guess_wordListed[i]

        return








#chooses a random word and sets it to our launch_word


    #def space_word_index():


def test():
    print("our launch_word is " + game.launch_word)



def gameLoad():
    load = launch_word_load()
    print("Welcome to Spaceman. Try to guess the correct letters to launch the shuttle!")


gameLoad()

game = spaceGame(launch_word, launch_word_list)
test()
launching = True

while launching:
    game.launch_guess()
