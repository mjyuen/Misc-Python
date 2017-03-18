# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
# by Michelle Yuen, for Python 2.7
# Function takes a series of words from the user and returns the reverse
def reverseWord(line):
    words = line.split(" ")
    res = words[::-1]
    return " ".join(res)
line = str(raw_input("Type some words: "))
print reverseWord(line)
