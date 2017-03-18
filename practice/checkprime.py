# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# by Michelle Yuen, for Python 2.7
# Program takes user submitted number and checks if it is or isn't prime.
# If the number is not prime, a list of divisors is returned.

num = int(raw_input("Enter a number: "))
possible = range(2, num) # generate a list of possible divisors
divisors = []
for div in possible:
    if num % div == 0:
        divisors.append(div)
if len(divisors) == 0:
    print "The number is prime."
else:
    print "The number is not prime. Here is a list of divisors: \n"
    print divisors
