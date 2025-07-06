# Rock, paper, scissors

Implementation of the game rock, paper, scissors; and the extension with spock and lizard.

Rules.py\\
The rules are rewritten from a list to a dictionary in "lst_to_dict" and determines the winning move of that round in "winner"

Player.py\\
class where a player is defined. Saves the number of wins in the game, and lets the player play a move (given in options). The "cpu_player" plays a random move from the available options; a free play is picked by the (human) player in "free_play" and "fixed_play" always plays the first option in the options list.

Game_interface.py\\
GameInterface mimics 1 round of the game in "round" and gives a point to the winner of that round; in "game", "round" is called until one of the players won the game.\\
"pick_game" lets the (human) player pick which game and rules they want to play\\
"pick_target_wins" lets the (human) player pick the target number of rounds to win\\
"print_rules" lets the (human) player decide whether or not to print the game rules\\
"main" runs the game
