#! /usr/bin/python3
# Program to automatically play popular game 2048 based on pattern: move up, right, down, left until the end
# Usage: ./ch_11_2048.py

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get("https://play2048.co/")
htmlElem = browser.find_element_by_tag_name('html')

while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    # add argument which will display score at the end