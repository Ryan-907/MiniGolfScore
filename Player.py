import MiniGolf

#Child class that add players
class Player(MiniGolf.MiniGolf):

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.list_of_scores = []

    #Printout
    def __str__(self):
        return f'{self.name} has a score of {self.score}'
    def __repr__(self):
        return f'Player({self.name})'
        
    #Updatescore of player
    def update_par(self, par):
        self.score += par
    def update_list(self, par):
        self.list_of_scores.append(par)