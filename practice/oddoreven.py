# http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Program asks the user for a number and determines if it's even or odd
# by Michelle Yuen, for Python 2.7
# Extra 2, see original at the bottom in comment
num = int(raw_input("Enter a number: "))
check = int(raw_input("Enter a number to divide by: "))
if num % check == 0:
    print "The number " + str(check) + " divides evenly into " + str(num)
else:
    print "The number " + str(check) + " does not divide evenly into " + str(num)


# Beginning part of problem
#if num % 2 == 0: # Even number
#    if num % 4 == 0: # multiple of 4
#        print "The number " + str(num) + " is a multiple of four."
#    else:
#        print "The number " + str(num) + " is even."
#else: # odd number
#    print "The number " + str(num) + " is odd."
