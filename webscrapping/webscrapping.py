# factory design patterns
# creational dsign patterns


import requests
import bs4


class Webscraping():

    def __init__(self, url):
        self.url = url

    def webscrape(self):

        data = requests.get(self.url, allow_redirects=True)
        bs4data = bs4.BeautifulSoup(data.text, "lxml")
        images = bs4data.find_all('img')
        f = open("file1.txt", "w+")
        x = []
        for i in images:
            x.append(i['src'])
            f.write(i['src']+"\n"+"\n")
        print(len(x))
        y = x.count('https://images.unsplash.com/photo-1676930437090-b1deb47e240f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHw%3D&w=1000&q=80')
        print(y)
        for i in x:
            print(i, "\n")

    def geticons(self):
        data = requests.get("https://unsplash.com/")
        bs4data = bs4.BeautifulSoup(data.text, "lxml")
        icons = bs4data.find_all('svg')
        f = open("file2.txt", "w+")
        x = []
        for i in icons:
            x.append(i)
        for i in x:
            f.write(str(i)+"\n" + "\n")
