import ttt

def versus(player1, player2, match_count=1000):
    """plays match_count games between given players, player1 starts"""
    stats = {'x': 0, 'o': 0, 'tie': 0}
    tg = ttt.game()
    for i in range(match_count):
        while not tg.winner:
            player1.move(tg)
            player2.move(tg)
        stats[tg.winner] += 1
        tg.reset()
    return stats