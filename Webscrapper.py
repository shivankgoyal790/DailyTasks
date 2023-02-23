import abc
import bs4
import requests


def checker(url):
    response = requests.head(url, allow_redirects=True)
    if response.is_redirect:
        return response.headers["Location"]
    else:
        return url


class WebScapper():

    def __init__(self):
        pass

    @abc.abstractmethod
    def WebScrapping():
        raise "not implemented"


class ImageScrapper(WebScapper):
    def __init__(self, url):
        url = checker(url)
        self.url = url

    def WebScrapping(self):

        data = requests.get(self.url)
        bs4data = bs4.BeautifulSoup(data.text, "lxml")
        images = bs4data.find_all('img')
        x = []
        for i in images:
            x.append(i['src'])
        return x


class IconScrapper(WebScapper):
    def __init__(self, url):
        url = checker(url)
        self.url = url

    def WebScrapping(self):
        data = requests.get(self.url)
        bs4data = bs4.BeautifulSoup(data.text, "lxml")
        icons = bs4data.find_all('svg')
        x = []
        for i in icons:
            x.append(i)


class StoreInFile():
    def __init__(self, filename):
        self.filename = filename

    def StoreData(self, listofurl):
        f = open(self.filename, "w+")
        for i in listofurl:
            f.write(i+"\n"+"\n")


def main():
    url = input("Enter The URL To scrap")
    print("1. For Image Scrapping")
    print("2 for icon Scrapping")
    ch = input("which type of scrapping you want to do")
    listofscrapedurl = []
    if (ch == '1'):
        Image = ImageScrapper(url)
        listofscrapedurl = Image.WebScrapping()
    elif (ch == '2'):
        Icons = IconScrapper(url)
        listofscrapedurl = Icons.WebScrapping()

    print("Enter 1 to write in a file or 2 to exit")
    ch = input()
    if (ch == '1'):
        x = input("Enter File Name")
        fileobj = StoreInFile(x)
        fileobj.StoreData(listofscrapedurl)
    else:
        print("thank You")


main()
