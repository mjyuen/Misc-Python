# http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# by Michelle Yuen, for Python 2.7
# Prints  a list of all divisors for a user entered number
usernum = int(raw_input("Enter a number: "))
divisors = []
nums = range(1, usernum + 1)
for num in nums:
    if usernum % num == 0:
        divisors.append(num)
print divisors
