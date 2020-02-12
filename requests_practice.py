import requests
from bs4 import BeautifulSoup
import webbrowser

# create request object
# r = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(r))
# print(r.status_code == requests.codes.ok)
# print(len(r.text))
# print(r.text[:250])

# r.raise_for_status() checks for errors

# try:
#     r.raise_for_status()
# except Exception as e:
#     print('There was an error: ' + e)

r = requests.get(
    'https://www.youtube.com', 'html.parser')
soup = BeautifulSoup(r.text, features='html.parser')
mydivs = soup.select('div[type="button"]')
print(mydivs)
