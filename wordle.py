from random import choice
from colorama import Fore, Back, Style

WORD_FILE = '5letter_dict.txt'


def read_input(prompt: str, dictionary: list) -> str:
    """Read user word input"""    

    while True:
        line = input(prompt).upper()
        if line in dictionary:
            return line
        else:
            print ("Invalid Input, try again")


def get_colored_text(match_zip: list) -> str:
    colored_text = ''
    for item in match_zip:
        if item[1] == 'o':
            colored_text += Back.GREEN + Fore.BLACK + item[0] + Style.RESET_ALL
        elif item[1] == '*':
            colored_text += Back.CYAN + Fore.BLACK + item[0] + Style.RESET_ALL
        elif item[1] == '?':
            colored_text += Fore.LIGHTWHITE_EX + item[0] + Style.RESET_ALL
        else:
            colored_text += item[0]

    return colored_text        

class Game:
    def __init__(self, file: str) -> None:
        self.attempts = 0
        self.solved = False
        with open(file, 'r') as f:
            word_list = [word.strip() for word in f.readlines()]
            word = choice(word_list)
        self.dictionary = word_list
        self.answer = word
        self.history = []
        self.keyboard = {item:'?' for item in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

    def user_guess(self, input: str) -> None:
        self.attempts += 1
        answer = self.answer

        if answer == input:
            self.solved = True
        
        answer_list = [letter for letter in answer]
        input_list = [letter for letter in input]
        match = ['x' for _ in range(5)]

        for i in range(5):
            if answer_list[i] == input_list[i]:
                answer_list[i] = '_'
                input_list[i] = '_'
                match[i] = 'o'
                self.keyboard[answer_list[i]] = 'o'
        
        for i in range(5):
            if input_list[i] == '_':
                pass
            elif input_list[i] in answer_list:
                match[i] = '*'
                answer_list[answer_list.index(input_list[i])] = '_'
                if self.keyboard[input_list[i]] != 'o':
                    self.keyboard[input_list[i]] = '*'
            else:
                self.keyboard[input_list[i]] = 'x'

        self.history.append(list(zip(input,match)))


def main(file: str) -> None:
    game = Game(file=file)

    while game.attempts < 6:
        game.user_guess(read_input('Enter your guess: ', game.dictionary))
        for history in game.history:            
            print(get_colored_text(history))
        print('-------------------------------------------')
        print('keyboard')
        print(get_colored_text([(k,v) for k,v in game.keyboard.items()]))
        if game.solved:
            break
        
    if game.solved:
        print(f"You win! attempt = {game.attempts}")
    else:
        print(f"failed, answer was {game.answer}")



if __name__ == '__main__':
    main(file=WORD_FILE)
    
