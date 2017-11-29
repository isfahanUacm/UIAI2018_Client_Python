

class Pos:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return "%f:%f" % (self.x, self.y)

    def __repr__(self):
        return "%f:%f" % (self.x, self.y)



class Ball:
    def __init__(self, pos=None):
        self.pos = pos

    @property
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self, pos):
        if not pos:
            self.__pos = Pos(0,0)
        elif isinstance(pos, Pos):
            self.__pos = pos
        else:
            raise ValueError('position must be a client.Pos instance')

class Field:
    def __init__(self, ball=None):
        self.ball = ball



class Player:

    __nextID = 0

    def __init__(self, id = 0, name='', first_pos = Pos(0, 0)):
        self.id = id
        self.name = name
        self.first_pos = first_pos
        self.pos = first_pos
        self.scores = 0


    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        if not id:
            self.__id = Player.__nextID
            Player.__nextID += 1
        self.__id = id


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def first_pos(self):
        return self.__first_pos
    @first_pos.setter
    def first_pos(self, pos):
        if not isinstance(pos, Pos):
            raise ValueError('first position of player must be a client.Pos instance')
        else:
            self.__first_pos = pos

    @property
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self, pos):
        if not isinstance(pos, Pos):
            raise ValueError('current position of player must be a client.Pos instance')
        else:
            self.__pos = pos

    @property
    def scores(self):
        return self.__scores
    @scores.setter
    def scores(self, scores):
        self.__scores = scores

    def __str__(self):
        return "%s:%s" % (self.name, self.pos)
    def __repr__(self):
        return "%s:%s" % (self.name, self.pos)


class Team:

    def __init__(self):
        self.players = list(5)
        self.score = 0

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def players(self):
        return list(self.__players)
    @players.setter
    def players(self, players):
        assert isinstance(players, (list, tuple)), "players must be a list of client.Player instances"
        for each in players:
            assert isinstance(each, Player), "each instance in players list must be a client.Player instance"
        self.__players = players

    def add_player(self, player):
        if len(self.__players) > 5:
            raise Exception('Team can not have more than 5 players')
        else:
            assert isinstance(player, Player), 'player must be a client.Player instance'
            self.__players.append(player)

    def __iter__(self):
        for each in self.__players:
            yield each




if __name__ == '__main__':
    p = Pos(1,2.6)
    print("sth %s"% (p) )