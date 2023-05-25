My first git project! Minigolf! (This is my first readme and idk what I’m doing!!! Gotta start somewhere, though!)
This project imports pyinputplus as pyip to ensure integer inputs only accept ints!
This simple project uses two classes: MiniGolf() and a child class, Payer(MiniGolf).
The simple overview is that the project takes in information about the Min Golf course. The name, number of holes, and number of people. It also stores a list of players. 
The MiniGolf class has three methods
1. Print_scorecard() this method takes one argument, a list containing objects of the “Player” child class and derives information from each object to print out a visually pleasing score card with totals. 
2. A typical __repr__method
3. A typical __str__ method
The child class, Player(MiniGolf) takes the players name. It has three methods:
1. Typical __str__ method
2. Update_par which takes the users score for a particular hole and updates their total score
3. Update_list which keeps a list of scores for each hole
The main program takes user input for vars needed for MiniGolf, then uses the num_players to ask for names and create enough Player objects for each player. It then asks for scores and displays the scorecard as the game progresses!
