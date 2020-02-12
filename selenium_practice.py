from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://google.com')
emailElem = browser.find_element_by_name('q')
emailElem.send_keys('soup')
