# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# by Michelle Yuen, for Python 2.7
# Program plays a guessing game with the user
import random
ceil = int(raw_input("How high can I go? "))
numguess = 0 # number of guesses
ans = random.randint(1, ceil + 1)
while True:
    guess = (raw_input("Guess a number: "))
    if str(guess) == "quit":
        print "Quitting..."
        break
    elif int(guess) == ans:
        print "You're right!"
        break
    elif int(guess) < ans:
        print "Too low..."
    elif int(guess) > ans:
        print "Too high..."
