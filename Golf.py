import pyinputplus as pyip
#This class makes the course. Takes course name, number of holes, and number of players
class MiniGolf:

    def __init__(self, course_name, num_holes, num_players):
        self.course_name = course_name
        self.num_holes = num_holes
        self.num_players = num_players
        self.players = []

    #String method for proper printout
    def __str__(self):
        return f'{self.course_name} has {self.num_holes} holes! There are {self.num_players} playing!'
    
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

#Child class that add players
class Player(MiniGolf):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.list_of_scores = []

    #Printout
    def __str__(self):
        return f'{self.name} has a score of {self.score}'
        
    #Updatescore of player
    def update_par(self, par):
        self.score += par
    def update_list(self, par):
        self.list_of_scores.append(par)

if __name__ == "__main__":
    #Getting inputs for course
    crs_name = input("Enter the course name: ")
    nm_holes = pyip.inputInt("Enter number of holes: ")
    nm_players = pyip.inputInt("Enter number of plyers: ")
    #Creating course with inputs
    course = MiniGolf(crs_name, nm_holes, nm_players)

    #Getting player names, turning them into instances of players, and then addding those objects to players list
    for player in range(course.num_players):
        new_player = input(f'Enter player {player + 1} name: ')
        add = Player(new_player, 0)
        course.players.append(add)

    #Getting par for each player at each hole
    for hole in range(course.num_holes):
        for player in range(course.num_players):
            par = pyip.inputInt(f"Please enter {course.players[player].name}'s score for hole {hole + 1}: ")
            course.players[player].update_list(par)
            course.players[player].update_par(par)
        course.print_scorecard(course.players)

    #Printing out final scores for each player
    for player in range(course.num_players):
        print(f'{course.players[player].name} has a score of {course.players[player].score}')



