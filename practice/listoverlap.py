# http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# by Michelle Yuen, for Python 2.7
# Program generates two random lists of random lengths and finds their intersection
import random
a = random.sample(range(1, 1000),random.randint(1, 100))
b = random.sample(range(1, 1000),random.randint(1, 100))
print a
print b
common = []
if len(a) >=  len(b): # if a is longer than b
    for num in a:
        if num in b:
            common.append(num)
elif len(a) < len(b): # if b is longer than a
    for num in b:
        if num in a:
            common.append(num)
print common
