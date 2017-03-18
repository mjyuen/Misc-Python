# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# by Michelle Yuen, for Python 2.7
# Program is an exercise in list comprehension
# Prints even elements of the list a

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evens = [num for num in a if num % 2 == 0]
print evens
