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

def kick(args):

    print(', '.join(map(str,args)))



if __name__ == "__main__":
    my_team = init_players()
    self_team =  "1:3, 2:2.332, 1:4, 4.553:1.3, 3:1".split(",")
    print(self_team)

    for each, each_pos in zip(my_team, self_team):
        each.pos.x, each.pos.y = map(float, each_pos.split(":"))
    print(my_team)

    kick(do_turn(my_team))


