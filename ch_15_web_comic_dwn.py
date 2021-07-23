#! /usr/bin/python3
# Program that will check once a day if there is a new comic available to download 
#   from certain website and then save it on the desktop
# 
# In order to run this program you can launch it using command below:
#   nohup (python3) ch_15_web_comic_dwn.py

import schedule, time, subprocess, requests, os, bs4, re

os.makedirs('comics', exist_ok=True)    # store comics in ./xkcd

# Run a program once a day
def job():
    # Download the page.
    res = requests.get('http://www.lunarbaboon.com/')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('.full-image-block img')
    if comicElem == []:
        print('Could not find comic image')
    else:
    # Find the URL of the comic image
        comicUrl = comicElem[0].get('src')
        comicUrl = re.sub('\?__SQUARESPACE_CACHEVERSION=.*$', '', comicUrl)

    # Check if image already exists
    # if no -> download the image
        if not os.path.isfile('./comics/' + os.path.basename(comicUrl)):
            res = requests.get('http://www.lunarbaboon.com' + comicUrl)
            res.raise_for_status()
            
    # Save the image to certain folder
            imageFile = open(os.path.join('comics', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    return

schedule.every().day.at("07:50").do(job)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute

