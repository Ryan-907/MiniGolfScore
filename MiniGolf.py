class MiniGolf:
#This class makes the course. Takes course name, number of holes, and number of players
    def __init__(self, course_name, num_holes, num_players):
        self.course_name = course_name
        self.num_holes = num_holes
        self.num_players = num_players
        self.players = []
    
    def print_scorecard(self, players):
        for hole in range(self.num_holes):
            print("--------", end = '')
        print()
        print(self.course_name, end = ' ')
        for hole in range(self.num_holes):
            print("| " + str(hole + 1) + " ", end = ' ')
        print("| Total |")
        for hole in range(self.num_holes):
            print("--------", end = '')
        print()

        for player in range(len(players)):
            print(players[player].name, end =" ")
            for hole in range(len(players[player].list_of_scores)):
                print("| " + str(players[player].list_of_scores[hole]) + " ", end = ' ')
            print("| " + str(sum(players[player].list_of_scores)) + " |" )
            for hole in range(self.num_holes):
                print("--------", end = '')
            print()

    def __repr__(self):
        return f'MiniGolf({self.name}, {self.num_holes}, {self.num_players})'
    def __str__(self):
        return f'The {self.course_name} course has {self.num_holes} holes and {self.num_players} players!'


