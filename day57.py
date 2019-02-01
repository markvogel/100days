import pprint


def tally(a: str):
    players = ('a', 'b', 'c', 'd', 'e')
    return {i: calc_player_score(i, a) for i in players}


def calc_player_score(player: str, score: str):
    return score.count(player) - score.count(player.upper())


def print_scores(raw_scores: str):
    pprint.pprint(tally(raw_scores), width=1)


if __name__ == '__main__':
    print_scores('EbAAdbBEaBaaBBdAccbeebaec')
