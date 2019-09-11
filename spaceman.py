import random

launch_word = []

def space_word_load():

    f = open('word_bank.py', 'r')

    words_list = f.readlines()
    f.close()

    word_generate = words_list[0].split(' ')
    space_word = random.choice(word_generate)
    launch_word = list(space_word)

    return space_word

class spaceGame:

    #we'll use classes to make it easer to store our chose words and test number of letters
    def __init__(self, launch_word):
        self.name = self
        self.launch_word = launch_word




#chooses a random word and sets it to our launch_word


    #def space_word_index():


def test():
    print(space_word_load())
    print("our launch_word is " + launch_word)


test()

game = spaceGame(launch_word)
