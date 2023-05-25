import pyinputplus as pyip
import MiniGolf 
import Player

if __name__ == "__main__":
    #Getting inputs for course
    crs_name = input("Enter the course name: ")
    nm_holes = pyip.inputInt("Enter number of holes: ", min = 1)
    nm_players = pyip.inputInt("Enter number of plyers: ", min = 1)
    #Creating course with inputs
    course = MiniGolf.MiniGolf(crs_name, nm_holes, nm_players)

    #Getting player names, turning them into instances of players, and then addding those objects to players list
    for player in range(course.num_players):
        new_player = input(f'Enter player {player + 1} name: ')
        add = Player.Player(new_player)
        course.players.append(add)

    #Getting par for each player at each hole
    for hole in range(course.num_holes):
        for player in range(course.num_players):
            par = pyip.inputInt(f"Please enter {course.players[player].name}'s score for hole {hole + 1}: ", min = 1)
            course.players[player].update_list(par)
            course.players[player].update_par(par)
        course.print_scorecard(course.players)

    #Printing out final scores for each player
    for player in range(course.num_players):
        print(f'{course.players[player].name} has a score of {course.players[player].score}')



