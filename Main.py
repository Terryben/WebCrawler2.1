#Ben Terry
#05/25/2016
#program to learn how to grab text from a website
#push test change

import requests
from selenium import webdriver
from bs4 import BeautifulSoup

test_url = "https://en.wikipedia.org/wiki/Friedrich_Johann_Graf_von_Medem"

def getWebPage(wp_url):
    try:
        r = requests.get(wp_url)
        return r
    except Exception as e:
        print(e)
        return e

def getWebPageSel(wp_url):
    try:
        r = requests.get(wp_url)
        return r
    except Exception as e:
        print(e)
        return e



if __name__ == '__main__':
    contents = getWebPage(test_url).content
    soup = BeautifulSoup(contents, "html.parser")
    #print(test_url)
    #print(soup)

    #make a browser driver. Part of the selenium package. I like Chrome
    ChromeDriver = webdriver.Chrome()

    #get the webpage
    ChromeDriver.get(test_url)


