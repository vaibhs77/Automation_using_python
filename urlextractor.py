import os
import bs4
from sys import *
import requests
from urllib.request import urlopen


def urlScrapper(url):
    connection = urlopen(url)
    raw_html = connection.read()
    connection.close()
    page_soup = bs4.BeautifulSoup(raw_html, 'lxml')
    container = page_soup.findall("a", {"class": "link-a-normal a-text-normal"})
    return container


def main():
    print("----vaibhav misal---")
    print("appliction name : " + argv[0])
    if (len(argv) == 2):
        if (argv[1] == "-h") or (argv[1] == '-H'):
            print ("usage: the script is fetching url")
            exit()
            if (argv[1] == "-u") or (argv[1] == "-U"):
                print ("usage: Application name")
                exit()

    try:
        url = "https://www.amazon.in/s?k=mackbook&ref=nb_sb_noss"
        listout = urlScrapper(url)
        print("url from website is:")
        for element in listout:
            print(element["href"])
            print()
    except Exception as E:
        print ("Error : invalied input", E)


if __name__ == "__main__":
    main()
