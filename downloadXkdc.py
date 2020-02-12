import requests
import os
from bs4 import BeautifulSoup

url = 'http://xkcd.com'  # starting url
os.mkdir('xkcd')  # store comics in ./xkcd

while not url.endswith('#'):
    # download page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text)

    # find url of the image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Couldn't find any comic images")
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

    # download image
        print('Downloading image %s' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    # save image to ./xkcd
        imageFile = open(os.path.join(
            'xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get the prev buttons url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done')
