#! /usr/bin/python3
# Program that will download n number of images from certain category/keyword from photo site (at this moment work with https://imgur.com)
# Usage: ./ch_11_img_download.py <photo website> <category> <num of imgs>

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys, requests, bs4, os


# TODO: validate input args
if len(sys.argv) != 4:
    print("Usage: ./ch_11_img_download.py <photo website> <category> <num of imgs>")
    sys.exit()

os.makedirs('downloaded', exist_ok=True)

# TODO: open certain website
browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get(sys.argv[1])

# TODO: search for category

    # TODO: implement clicking on pop window with cookies
# delay = 10 # seconds
# try:
#     myElem = WebDriverWait(browser, delay).until(EC.element_to_be_clickable((By.XPATH,'Accept All'))).click()
#     print("Page is ready!")
# except TimeoutException:
#     print("Loading took too much time!")

try:
    inputBox = browser.find_element_by_tag_name("input[value]")
    inputBox.send_keys(sys.argv[2])
    inputBox.submit()
except:
    print('Was not able to find an element with that name.')

# TODO: find imgs
# TODO: Download the page.
print("Current URL: " + browser.current_url)
res = requests.get(browser.current_url)
res.raise_for_status()

soup = bs4.BeautifulSoup(browser.page_source, "html.parser")

#Find the URL of the images
imgElem = WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".image-list-link [src]")))

if imgElem == []:
    print("Could not find requested image")
else:
    for i in range(min(int(sys.argv[3]), len(imgElem))):
        imgUrl = imgElem[i].get_attribute("src")
        print("Img URL: " + imgUrl)
        # Download the image.
        print('Downloading image %s...' % (imgUrl))
        res = requests.get(imgUrl)
        res.raise_for_status()

        # Save the image
        imageFile = open(os.path.join('downloaded', os.path.basename(imgUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()