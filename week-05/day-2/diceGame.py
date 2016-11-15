import random
import dicetexts
# The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.
#
# Concepts to keep in mind:
#
# Random
# Integer
# Print
# While Loops

class Player:
    def __init__(self):
        self.name = ''
        self.money = 0

    # def player_buy_coin(self):


class Game:
    def __init__(self, player):
        self.player = player
        self.is_running = False
        self.bottom_range = 1
        self.top_range = 6
        self.random_number = -1
        self.number_of_rolls = 10
        self.player_score = 0
        self.bot_score = 0
        #

        print(dicetexts.intro['intro_msg'])
        print(dicetexts.intro['name'])
        self.player.name = str(input())
        # print('Please set your coins!')
        # self.player.money = int(input())

        self.start()

    def start(self):
        print(dicetexts.game_on['game_q'])
        self.to_play_or_not_to_play()
        print(dicetexts.game_on['welcom_msg'].format(self.player.name))



    def gameloop(self):
        while self.is_running:
            player_roll = self.roll_funct()
            pc_roll = self.roll_funct()
            self.score_sum(player_roll, pc_roll)
            if self.rolls == 0:
                print(dicetexts.end['end_g'])
                self.compare()
                print(dicetexts.game_on['more_game'])
                self.to_play_or_not_to_play()
            else:
                self.rolls -= 1
                print("Let's roll.......: \n {0} - {1} \n \n Bot - {2}\n".format(self.player.name,player_roll, pc_roll))
                if self.player_score > self.bot_score:
                    print("{0} Wins this round!\n {1}".format(self.player.name, self.player_score))
                else:
                    print("Bot Wins this round!\n {0}".format(self.bot_score))
                    # print("Hah I won this round - sent by your PC\n")


    def score_sum(self, player_roll, pc_roll):
        self.player_score += player_roll
        self.bot_score += pc_roll

        return self.player_score, self.bot_score

    def compare(self):
        if self.player_score > self.bot_score:
            print('{0} Won the game!!!'.format(self.player.name))
        else:
            print(dicetexts.game['pc_roll3'].format(self.bot_score))

    def roll_funct(self):
        return random.randint( self.bottom_range, self.top_range)

    def coin_buying(self):
        # self.player_buy_coin
        print('Please buy your coins!')
        self.rolls = int(input())

    def to_play_or_not_to_play(self):
        invalid_input = True
        while invalid_input:
            choice = str(input())
            if choice.lower() == 'y':
                print(dicetexts.game_on['first_choice_y'])
                self.is_running = True
                self.coin_buying()
                self.gameloop()
                invalid_input = False
            elif choice.lower() == 'n':
                self.is_running = False
                invalid_input = False
            else:
                print('Are you stupid??? Give me valid answer!!!! - Hint y or n!!')





new_player = Player()
game = Game(new_player)
