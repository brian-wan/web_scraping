import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome('/Users/brianwan/Downloads/chromedriver')
browser.get(
    'https://www.youtube.com')

w = requests.get(
    'https://www.youtube.com')

soup = BeautifulSoup(w.text, 'html.parser')
search_form = soup.find_all(class_="search-form")
print(search_form.text)
