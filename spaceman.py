import random

guessCount = 0

launch_word = None
blank_counter = []
launch_word_list = []
def launch_word_load():
    # we'll use this one function to load, split and save our word as a whole word and a list

    f = open('word_bank.py', 'r')

    words_list = f.readlines()
    f.close()


    space_list = words_list[0].split(' ')
    #space_list = words_list.split(" ")
    space_word = random.choice(space_list)

    global launch_word
    launch_word = space_word

    for char in launch_word:
        launch_word_list.append(char)
    # this function empowers our intialization of our word as lists to be guessed into
    for char in launch_word_list:
        blank_counter.append('_')

    #global launch_word_list

    return launch_word
    return launch_word_list
    return blank_counter

# will be used to replace guesses with blanks
'''
def blankify(guessIndex, guess):

    game.blankedWord.insert(guessIndex, guess)
    print(game.blankedWord)
    #print(launch_word_list[0])
'''

def check_wordList(guessStr):
    gameList = game.launch_word_list
    listIndex = gameList.index(guessStr)
    listIndexFinish = gameList.index(guessStr, listIndex)

    if listIndexFinish > listIndex:

        print("pop two")

        #print(gameList.index(guess[indexedGuess[game.listLength - 1]]))
        # game.guessIndex.append(launch_word_list.index(guess))
        return True

    else:
        print("guess not in word")
        return False

def guess():
    global guessCount

    guessQuery = input(("What letter would you like to guess? ({}/7 guesses) ").format(guessCount))
    guessStr = str(guessQuery)

    if game.launch_word_list.count(guessStr) > 1:
        for i in range(0, game.launch_word.count(guessStr)):
            indexedGuess = int(game.safetyList.index(guessStr))
            game.launch_word_list.pop(indexedGuess)
            game.launch_word_list.insert(indexedGuess, '_')
            game.blankedWord.pop(indexedGuess)
            game.blankedWord.insert(indexedGuess, guessStr)

        print("{} is correct!".format(guessStr))
        print("{}".format(game.blankedWord))
        return True

    elif game.launch_word.count(guessStr) == 1:
        indexedGuess = int(game.safetyList.index(guessStr))
        game.blankedWord.pop(indexedGuess)
        game.blankedWord.insert(indexedGuess, guessStr)
        # guessIndex.append([1[guess]]
        return True

    else:
        guessCount += 1
        return False

class spaceGame:

    #we'll use classes to make it easer to store our chose words and test number of letters
    def __init__(self, launch_word, launch_word_list, blank_counter):
        self.name = self
        self.launch_word = launch_word
        self.launch_word_list = launch_word_list
        self.safetyList = launch_word_list
        self.blankedWord = blank_counter
        self.guess_number = 1
        self.listLength = len(launch_word_list)

#chooses a random word and sets it to our launch_word


    #def space_word_index():


def test():
    '''
    print("our launch_word is " + game.launch_word)
    print(game.launch_word_list[0])
    print(game.guessIndex)

    assert
    '''
    print(launch_word)
    print(game.blankedWord)
    return

def gameLoad():
    launch_word_load()
    print("Welcome to Spaceman. Try to guess the correct letters to launch the shuttle!")


gameLoad()

game = spaceGame(launch_word, launch_word_list, blank_counter)

while guessCount < 7:
    # test()
    guess()
