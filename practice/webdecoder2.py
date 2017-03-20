# http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
# by Michelle Yuen, for Python 2.7
# Program prints a full article from VanityFair
import requests
import bs4

res = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
soup = bs4.BeautifulSoup(res.text, "html.parser")
for line in soup.find_all('p'):
    print str(line)
