class Rules:
    # rewrites rules to a dict; determines winner of a round
    def __init__(self, rules: list):
        self.rules = lst_to_dict(rules)

    def winner(self, play1: str, play2: str):
        # determines winner based on given two plays
        if play1 == play2:
            # draw
            return 0
        elif play2 in self.rules.get(play1):
            # you win
            return 1
        else:
            # opponent wins
            return 2


def lst_to_dict(rules: list):
    # rewrites the list with rules to a dictionary
    rdict = {}
    for rule in rules:
        win = rule.split()[0]
        lost = rule.split()[-1]
        rdict.setdefault(win, []).append(lost)
    return rdict
