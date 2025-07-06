import random as rnd


class Player:
    # creates players, let them pick a play and saves wins from each player
    def __init__(self, options: list):
        self.wins = 0
        self.play = ""
        self.options = options

    def cpu_play(self):
        # player gets random play
        self.play = self.options[rnd.randint(0, len(self.options)-1)]
        print("CPU's play is " + self.play)

    def free_play(self):
        # play of choice
        print("Play options, please pick from " + str(self.options))
        self.play = input("Type your play: ")
        while self.play not in self.options:
            self.play = input("Invalid choice, please pick from " + str(self.options) + ": ")

    def fixed_play(self):
        # fixed play for de-bugging or CPU
        self.play = self.options[0]
        print("Fixed play is " + self.play)
