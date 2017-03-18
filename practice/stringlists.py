# http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# By Michelle Yuen, for Python 2.7
# Program asks the user for a string and confirms whether it's a palindrome or not

userIn = str(raw_input("Enter a string: "))
revuserIn = userIn[::-1]
if userIn == revuserIn:
    print "The string " + userIn + " is a palindrome."
else:
    print "The string " + userIn + " is not a palindrome."
