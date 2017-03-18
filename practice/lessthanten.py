# http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# by Michelle Yuen, for Python 2.7
# Program prints out elements of the list a that are less than n

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] # from webpage
n = int(raw_input("Enter a number: "))
list = []
for elem in a:
    if elem < n:
        list.append(elem)
print list
