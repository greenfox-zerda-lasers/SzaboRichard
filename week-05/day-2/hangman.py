import hangmantext
import random
# 5. Hangman
#
# The Goal: Despite the name, the actual “hangman” part isn’t necessary. The main goal here is to create a sort of “guess the word” game. The user needs to be able to input letter guesses. A limit should also be set on how many guesses they can use. This means you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list. No need to get too fancy.) You will also need functions to check if the user has actually inputted a single letter, to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.
#
# Concepts to keep in mind:
#
# Random
# Variables
# Boolean
# Input and Output
# Integer
# Char
# String
# Length
# Print
# Likely the most complex project on this list (well, depending on just how intense you went with the adventure text game), the Hangman project compiles the prior concepts and takes them a step further. Here, outcomes are not only determined based on user-inputted data, that data needs to be parsed through, compared, and then either accepted or rejected. If you want to take this project a step further, set up a hangman image that changes!
class Player1:
    def __init__(self):
        self.name = ''

class Game:

    def __init__(self, player):
        self.guesses = 7
        self.player = player
        self.g_words = ["kutyafajat","rekt", "greenfox", "silverwolf", "hooli"]
        self.g_word = random.choice(self.g_words)

        print("Welcome in your hanging MWUHAHAHAHA, so what was your name?")
        self.loop_for_init()



    def start_game(self):
        print(hangmantext.indent['lines'])
        print(hangmantext.text_start['intro'])
        print(hangmantext.text_start['wordlength'].format(len(self.g_word)))
        print(hangmantext.indent['lines2'])
        print("".join(self.word_draw()))
        self.game_loop()

    def game_loop(self):
        while self.guesses > 0:
            print()
            wordipp = self.string_getter_with_1_char()
            guesses_minus = self.char_check_in_g_word(wordipp)
            if guesses_minus == True:
                self.guesses -= 1
                print(hangmantext.texts_mid['-1guess'].format(self.guesses))
                print(hangmantext.graphics['case'+ str(7-self.guesses)])
            else:
                print("".join(self.wordvisual))
        if self.guesses == 0:
            self.game_restart()

    def game_restart(self):
        self.guesses = 7
        print("{0} DIED MWUHAHAHAHA".format(self.player.name))
        print("Do you want to continue as another deathsentenced inmate? (y) (n)")
        self.to_hang_or_not_to_hang()

    def char_check_in_g_word(self, tipp):
        failed_tip = True
        for char in range(len(self.g_word)):
            if self.g_word[char] == tipp:
                self.wordvisual[char] = tipp
                failed_tip = False
        return failed_tip

    def word_draw(self):
        self.wordvisual = []
        for letter in self.g_word:
            self.wordvisual.append(" _ ")
        return self.wordvisual

    def loop_for_init(self):
        try:
            self.player.name = self.string_getter()
            self.start_game()
        except ValueError:
            print("Ohh man your name cannot be a number...")
            self.loop_for_init()

    def to_hang_or_not_to_hang(self):
        failedInput = True
        while failedInput:
            userInput = self.string_getter_with_1_char()
            if userInput == 'y':
                failedInput = False
                self.start_game()
            elif userInput == 'n':
                print("So long, rest in peace!!! :D")
                failedInput = False
            else:
                print("y or n you dumb skeleton")

    def string_getter(self):
        numbers = "0123456789"
        string = input()
        for i in numbers:
            if i in string:
                raise ValueError
        return string

    def string_getter_with_1_char(self):
        while True:
            try:
                userInput = self.string_getter()
                if len(userInput) == 1:
                    break
                else:
                    print("Please enter only one character!")
            except ValueError:
                print("Wrong value give me chars!!!!")
        return userInput.lower()

new_player = Player1()
new_game = Game(new_player)
