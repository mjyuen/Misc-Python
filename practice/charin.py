# Program asks a user to enter their name and age,
# Prints out a personal message with the year they will turn 100 y/o
# by Michelle Yuen, using Python 2.7
# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
copies = int(raw_input("How many copies would you like? "))
year = (100 - age) + 2017
print (name + ", you will be 100 in the year " + str(year) + '\n') * copies
