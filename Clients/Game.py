from Clients.client import *
from Clients import Strategy
import socket





class Game:


    def __init__(self, inet_address, port):
        self.field = Field()
        self.ball = Ball()
        self.my_team = Team()
        self.opp_team = Team()
        self.__cycle_no = 0
        self.__server_address = (inet_address, port)
        self.__input = None
        self.__output = None

    def connect_to_server(self):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.connect(self.__server_address)
            self.__input = self.__socket.makefile(encoding ='utf-8', mode='r')
            self.__output = self.__socket.makefile(encoding='utf-8', mode='w')
        except Exception as e:
             print(e)
             return False
        return True

    def start(self, team_name, team_logo):
        lines = []
        lines.append("register %s" % team_name)
        #TODO write team_logo
        lines.append("logo null")

        self.my_team.players = Strategy.init_players()
        x = ", ".join(str(each) for each in self.my_team.players)
        formation = "formation %s" % x
        lines.append(formation)

        print("writing register commands:")
        for each in lines:
            print(each)

        try:
            self.__output.writelines(lines)
            self.__output.flush()
        except Exception as e:
            print(e)

        print("writing register commands successfully")
        while True:
            print("waiting for response")
            try:
                lines = []
                lines.append(self.__input.readline())
                lines.append(self.__input.readline())
                lines.append(self.__input.readline())
                lines.append(self.__input.readline())
                print("response:")
                for each in lines:
                    print(each)

                self.play_round(lines)
            except Exception as e:
                print("problem in getting response from server:")
                print('\t', e)
                return

    def play_round(self, lines):
        self_team = lines[0].split(',')
        opp_team = lines[1].split(',')
        for each, each_pos in zip(self.my_team, self_team):
            each.pos.x, each.pos.y = map(float, each_pos.split(":"))

        for each, each_pos in zip(self.opp_team, opp_team):
            each.pos.x, each.pos.y = map(float, each_pos.split(":"))

        self.ball.pos.x, self.ball.pos.y = map(float, lines[2].split(":"))

        self.my_team.score, self.opp_team.score, self.__cycle_no = map(int, lines[3].split(','))

        self.kick(Strategy.do_turn(self))

    def kick(self, args):
        print("writing kick commands:")
        print('\t', args)
        self.__input.write(', '.join(map(str, args)))
        self.__input.flush()
        print("kick command sent")


    @property
    def my_team(self):
        return self.__my_team

    @my_team.setter
    def my_team(self, my_team):
        self.__my_team = my_team

    @property
    def opp_team(self):
        return self.__opp_team

    @opp_team.setter
    def opp_team(self, opp_team):
        self.__opp_team = opp_team

    @property
    def cycle_no(self):
        return self.__cycle_no


    @property
    def ball(self):
        return self.__ball

    @ball.setter
    def ball(self, ball):
        if not ball:
            self.__ball = Ball(Pos(0, 0))
        elif isinstance(ball, Ball):
            self.__ball = ball
        else:
            raise ValueError('ball must be a client.Ball instance')



if __name__ == "__main__":
    game = Game('127.0.0.1', 9595)
    game.connect_to_server()
    game.start('Team1', None)
