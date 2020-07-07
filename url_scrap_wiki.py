import os
import bs4
import requests
import lxml
from sys import *
import webbrowser

def Link_display(url):
    res = requests.get(url)
    print(type(res))
    soup = bs4.BeautifulSoup(res.text,'lxml')
    print(type(res))
    links = soup.find_all("a",href=True)
    return links
def main():
    print("-------vaibhav infosystem------------")

    url = "https://en.wikipedia.org/wiki/python_(programming_language)"
    arr = Link_display(url)
    print("Link are")
    for element in arr:
        if "#"not in element["href"]:
            print(element["href"])

if __name__=="__main__":
    main()
