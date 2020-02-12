import sys
import webbrowser
import requests
from bs4 import BeautifulSoup

print('Googling...')

r = requests.get('http://google.cz/search?q=' + ''.join(sys.argv[1:]))


# retrieve top search result links
soup = BeautifulSoup(r.text)


# open a browser tab for each result
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
