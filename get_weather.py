import requests
from bs4 import BeautifulSoup

w = requests.get('https://darksky.net/forecast/29.7858,-95.8244/us12/en')

soup = BeautifulSoup(w.text, 'html.parser')

current_temp = soup.find("span", {"class": "summary swap"})
high = soup.find("span", {"class": "summary-high-low"})

print("The current weather in katy is " + str(current_temp.text))
print("Summary: " + str(high.text))


#select(# for id, . for class)
"""
browser.quit()
browser.refresh()
browser.back + forward
element.click()
browser.send_keys(sends input)
