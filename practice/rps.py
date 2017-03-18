# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# by Michelle Yuen, for Python 2.7
# Program simulates a 2-player game of rock, paper, scissors

# Get player names
player1 = str(raw_input("Enter Player 1's name: "))
player2 = str(raw_input("Enter Player 2's name: "))
player1score = 0 # both players start at 0 points
player2score = 0
round = 0 # start at round 0
while True:
    if round == 0:
        print "Starting game...\n"
    else:
        print "Beginning round " + str(round) + "\n"
    print "Current score for " + player1 + " is " + str(player1score) + ".\n"
    print "Current score for " + player2 + " is " + str(player2score) + ".\n"
    print "Player 1's Turn... \n"
    player1move = str(raw_input("Play rock, paper, or scissors: "))
    if player1move == "quit":
        break
    print "Player 2's Turn... \n"
    player2move = str(raw_input("Play rock, paper, or scissors: "))
    if player2move == "quit":
        break
    elif player1move == player2move:
        print "Both players chose " + player1move + ". This round ends in a tie.\n"
    elif player1move == "rock" and player2move == "scissors":
        player1score = player1score + 1
        print "Player 1 wins this round."
    elif player1move == "paper" and player2move == "rock":
        player1score = player1score + 1
        print "Player 1 wins this round."
    elif player1move == "scissors" and player2move == "paper":
        player1score = player1score + 1
        print "Player 1 wins this round."
    elif player1move == "rock" and player2move == "paper":
        player2score = player2score + 1
        print "Player 2 wins this round."
    elif player1move == "scissors" and player2move == "rock":
        player2score = player2score + 1
        print "Player 2 wins this round."
    elif player1move == "paper" and player2move == "scissors":
        player2score = player2score + 1
        print "Player 2 wins this round."
