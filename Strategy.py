import math
import random

from client import *


def init_players():
    '''
    Here you can set each of your player's name and your team formation.
    In case of setting wrong position, server will set default formation for your team.
    '''

    players = [Player(name="player_1", first_pos=Pos(-6.5, 0)),
               Player(name="player_2", first_pos=Pos(-2, 1)),
               Player(name="player_3", first_pos=Pos(-5, -2)),
               Player(name="player_4", first_pos=Pos(-5, 2)),
               Player(name="player_5", first_pos=Pos(-2, -1))]
    return players


def do_turn(game):
    act = Triple()
    '''
    Write your code here
    At the end you have to set 3 parameter:
        player id -> act.setPlyerID()
        angle -> act.setAngle()
        power -> act.setPower()
    '''

    # Sample code for shooting a random player in the ball direction with the maximum power:

    player_id = random.randint(0, 4)
    act.setPlayerID(player_id)

    x1 = game.getMyTeam().getPlayer(player_id).getPosition().getX()
    y1 = game.getMyTeam().getPlayer(player_id).getPosition().getY()
    x2 = game.getBall().getPosition().getX()
    y2 = game.getBall().getPosition().getY()
    angle = math.fabs(math.degrees(math.atan((y2 - y1) / (x2 - x1))))
    # Calculate the angle from the chosen player to the ball
    if x2 > x1:
        if y2 < y1:
            angle = 360 - angle
    else:
        if y2 < y1:
            angle += 180
        else:
            angle = 180 - angle
    act.setAngle(angle)

    act.setPower(100)

    return act
