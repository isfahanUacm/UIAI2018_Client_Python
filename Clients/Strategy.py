from Clients.client import *
#from Clients.Game import Game

def init_players():
    players = [Player(name = "player_%d" % i) for i in range(5)]

    return players

def do_turn(game):
    player_id, angle, power = 0, 0, 0
    """
    code your strategies here and fill:
        'player_id' to select player to shoot,
        'angle' to specify which angle to shoot,
        'power' to specify power of shoot
    """
    return player_id, angle, power
