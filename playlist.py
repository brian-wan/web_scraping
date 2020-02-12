import requests
from bs4 import BeautifulSoup
from selenium import webdriver
"""
browser = webdriver.Chrome('/Users/brianwan/Downloads/chromedriver')
browser.get(
    'https://www.youtube.com/playlist?list=PLLQoVBhB1DQVTMAfpjfJEMAdMqOFv0IGJ')
"""
w = requests.get(
    'https://www.youtube.com/playlist?list=PLLQoVBhB1DQVTMAfpjfJEMAdMqOFv0IGJ')

soup = BeautifulSoup(w.text, 'html.parser')

shuffle = soup.find_all("button")
print(shuffle)
