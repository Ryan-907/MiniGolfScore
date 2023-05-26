class MiniGolf:
#This class makes the course. Takes course name, number of holes, and number of players
    def __init__(self, course_name, num_holes, num_players):
        self.course_name = course_name
        self.num_holes = num_holes
        self.num_players = num_players
        self.players = []
    
    def print_scorecard(self, players):
        print("------------", end = '')
        for hole in range(8):
            print("--------", end = '')
        print()
        print(f'{self.course_name:<10}', end = ' ')
        for hole in range(self.num_holes):
            print(f"|{hole + 1:>2}", end = '')
        print(f'{"| Total |":>9}')
        print("------------", end = '')
        for hole in range(8):
            print("--------", end = '')
        print()

        for player in range(len(players)):
            print(f'{players[player].name:<10}', end = ' ')
            for hole in range(len(players[player].list_of_scores)):
                print(f"|{players[player].list_of_scores[hole]:>2}", end = '')
            print(f"|{sum(players[player].list_of_scores):^7}|" )
            print("------------", end = '')
            for hole in range(8):
                print("--------", end = '')
            print()

    def __repr__(self):
        return f'MiniGolf({self.name}, {self.num_holes}, {self.num_players})'
    def __str__(self):
        return f'The {self.course_name} course has {self.num_holes} holes and {self.num_players} players!'


