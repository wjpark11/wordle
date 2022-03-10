from random import choice
import re

WORD_FILE = '5letter_dict.txt'


def read_input(prompt: str, dictionary: list) -> str:
    """Read user word input"""
    pattern = re.compile(r'^[A-Za-z]{5}$')

    while True:
        line = input(prompt).upper()
        if pattern.match(line) and line in dictionary:
            return line
        else:
            print ("Invalid Input")
        

class Game:
    def __init__(self, file):
        self.attempts = 0
        with open(file, 'r') as f:
            word_list = [word.strip() for word in f.readlines()]
            word = choice(dict)
        self.dictionary = word_list
        self.answer = word



if __name__ == '__main__':
    game = Game(file=WORD_FILE)

    print(game.answer)
    read_input("enter your guess : ", game.dictionary)
    