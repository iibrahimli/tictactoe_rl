import ttt

def versus(player1, player2, match_count=1000):
    """plays match_count games between given players, player1 (x) starts"""
    stats = {'x': 0, 'o': 0, 'tie': 0}
    tg = ttt.game()
    for i in range(match_count):
        while not tg.winner:
            player1.move(tg)
            player2.move(tg)
        stats[tg.winner] += 1
        tg.reset()
    x_score = stats['x'] + stats['tie']*0.5
    o_score = stats['o'] + stats['tie']*0.5
    x_per = x_score / (x_score + o_score) * 100
    o_per = o_score / (x_score + o_score) * 100
    print("x: {:.2f}%, o: {:.2f}%".format(x_per, o_per))
    return stats