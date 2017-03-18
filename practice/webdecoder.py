# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# By Michelle Yuen, for Python 2.7
# prints out a list of all article titles from the NYT homepage
# Program practices using BeautifulSoup and requests packages
import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "html.parser")
for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        line = str(story_heading.a).split(">")
        finline = str(line).split("<")
        res = str(finline).split(",")
        print res[len(res) - 3]
    else:
        line = str(story_heading).split(">")
        finline = str(line).split("<")
        print res[(len(res) - 2)]
