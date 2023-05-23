#This class makes the course. Takes course name, number of holes, and number of players
class MiniGolf:

    def __init__(self, course_name, num_holes, num_players):
        self.course_name = course_name
        self.num_holes = num_holes
        self.num_players = num_players

    #String method for proper printout
    def __str__(self):
        return f'{self.course_name} has {self.num_holes} holes! There are {self.num_players} playing!'
    
    def print_scorecard(self):
        for hole in range(self.num_holes):
            print("--------", end = '')
        print()
        print(self.course_name, end = ' ')
        for hole in range(self.num_holes):
            print("|  " + str(hole + 1) + " ", end = ' ')
        print("|")
        for hole in range(self.num_holes):
            print("--------", end = '')
        print()

#Child class that add players
class Player(MiniGolf):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    #Printout
    def __str__(self):
        return f'{self.name} has a score of {self.score}'
        
    #Updatescore of player
    def update_par(self, par):
        self.score += par
            

#List of players to use later
players = []

#Getting inputs for course
crs_name = input("Enter the course name: ")
nm_holes = int(input("Enter number of holes: "))
nm_players = int(input("Enter number of plyers: "))
#Creating course with inputs
course = MiniGolf(crs_name, nm_holes, nm_players)

#Getting player names, turning them into instances of players, and then addding those objects to players list
for player in range(course.num_players):
    new_player = input(f'Enter player {player + 1} name: ')
    add = Player(new_player, 0)
    players.append(add)

#Getting par for each player at each hole
for hole in range(course.num_holes):
    for player in range(course.num_players):
        par = int(input(f"Please enter {players[player].name}'s score for hole {hole + 1}: "))
        players[player].update_par(par)

#Printing out final scores for each player
for player in range(course.num_players):
    print(f'{players[player].name} has a score of {players[player].score}')

course.print_scorecard()

