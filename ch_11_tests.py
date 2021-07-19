#! /usr/bin/python3

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://xkcd.com/')

try:
    elem = browser.find_element_by_link_text('< Prev')
    elem.click()
except:
    print('Was not able to find an element with that name.')