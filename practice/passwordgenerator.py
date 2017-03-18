# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
# By Michelle Yuen, for Python 2.7
# Generates a password based on level of strength determined by user
import string, random

stralldata = string.ascii_letters + string.digits + "@#$&*_-:;',.?/"

def password_generator(useroption):
    if useroption == 1:
        weaksize = random.randint(3,5)
        genpwd = "".join(random.sample(stralldata,weaksize))
    if useroption == 2:
        weaksize = random.randint(6,8)
        genpwd = "".join(random.sample(stralldata,weaksize))
    if useroption == 3:
        weaksize = random.randint(9,14)
        genpwd = "".join(random.sample(stralldata,weaksize))
    print("\n\t\tYour generated password is: " + genpwd)


correctdata = False
while not correctdata:
    print("1. Weak [3 to 5 letters]")
    print("2. Medium [6 to 8 letters]")
    print("3. String [9 to 14 letters]")
    useroption = int(raw_input("Hello please pick the type of your password form the above:"))
    if (useroption == 1) ^ (useroption == 2) ^ (useroption == 3):
        correctdata = True
    else:
        print("You have selected the wrong option. Please select from the below displayed list!!!")

password_generator(useroption)
