from Rules import Rules
from Player import Player

rps_rules = [
    "paper beats rock",
    "scissors beats paper",
    "rock beats scissors"
]

rpsls_rules = [
    "paper beats rock",
    "scissors beats paper",
    "rock beats scissors",
    "spock beats scissors",
    "lizard beats spock",
    "rock beats lizard",
    "paper beats spock",
    "scissors beats lizard",
    "spock beats rock",
    "lizard beats paper"
]


class GameInterface:
    # determines players, loops through game rounds until there is a winner
    def __init__(self, game_rules, nwins: int = 3):
        self.game_rules = game_rules
        self.p1 = Player(list(self.game_rules.rules.keys()))
        self.p2 = Player(list(self.game_rules.rules.keys()))
        self.nwins = int(nwins)

    def round(self):
        # mimics 1 round of the game, let players pick their play and give points to the winner
        self.p1.free_play()
        self.p2.cpu_play()

        result = self.game_rules.winner(self.p1.play, self.p2.play)
        if result == 0:
            print("Draw, play another round")
        elif result == 1:
            print("You won this round")
            self.p1.wins += 1
        elif result == 2:
            print("You lost this round")
            self.p2.wins += 1
        else:
            print("Result not possible")
            raise ValueError

    def game(self):
        # plays the given rounds for the game and prints overall winner of the game
        while max(self.p1.wins, self.p2.wins) < self.nwins:
            self.round()
            print("Standings: you " + str(self.p1.wins) + ", CPU " + str(self.p2.wins))
        if self.p1.wins > self.p2.wins:
            print("you win!")
        else:
            print("you lose :'(")


def pick_game():
    # lets the player pick the game they want to play, sets the rules
    print("Which game do you want to play?")
    print("[1] Rock, Paper, Scissors")
    print("[2] Rock, Paper, Scissors, Lizard, Spock")
    while True:
        try:
            game_rules = int(input("Please pick type 1 or 2: "))
            if game_rules == 1:
                game_rules = Rules(rps_rules)
                print_rules(game_rules.rules)
                return game_rules
            elif game_rules == 2:
                game_rules = Rules(rpsls_rules)
                print_rules(game_rules.rules)
                return game_rules
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice")


def pick_target_wins():
    # let player pick the target number of rounds to win
    while True:
        try:
            nwins = int(input("Target number of wins: "))
            if nwins < 1:
                raise ValueError
            else:
                return nwins
        except ValueError:
            print("Please pick a positive integer number")


def print_rules(game_rules: dict):
    # prints the rules if player would like to read them
    read_rules = input("Would you like to read the rules? [y/n]: ")
    while read_rules not in ["yes", "y", "Y", "Yes", "no", "No", "n", "N"]:
        read_rules = input("Please pick a valid input. Would you like to read the rules? [y/n]: ")
    if read_rules in ["yes", "y", "Y", "Yes"]:
        print("")
        print("The rules to this game are:")
        for k, v in game_rules.items():
            print(f'{str(k):<8} beats ' + ', '.join(str(x) for x in v))
        print("")


def main():
    rules = pick_game()
    nwins = pick_target_wins()
    game = GameInterface(rules, nwins)
    game.game()


if __name__ == "__main__":
    main()
