import ttt

def versus(player1, player2, match_count=1000):
    """plays match_count games between given players, player1 (x) starts"""
    stats = {'x': 0, 'o': 0, 'tie': 0}
    g = ttt.game()
    for i in range(match_count):
        while not g.winner:
            player1.move(g)
            player2.move(g)
        stats[g.winner] += 1
        g.reset()
    x_score = stats['x'] + stats['tie']*0.5
    o_score = stats['o'] + stats['tie']*0.5
    x_per = x_score / (x_score + o_score) * 100
    o_per = o_score / (x_score + o_score) * 100
    print("{}: {:.2f}%".format(player1.name, x_per))
    print("{}: {:.2f}%".format(player2.name, o_per))
    return stats


def argmax(iterable):
    maxi = 0
    for i in range(len(iterable)):
        if iterable[i] > iterable[maxi]:
            maxi = i
    return maxi