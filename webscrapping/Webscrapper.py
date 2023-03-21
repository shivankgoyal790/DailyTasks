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


class FactoryScrape():
    def __init__(self, choice, url):
        self.ch = choice
        self.url = url

    def factorymethod(self):
        if (self.ch == '1'):
            Image = ImageScrapper(self.url)
            return Image.WebScrapping()
        elif (self.ch == '2'):
            Icons = IconScrapper(self.url)
            return Icons.WebScrapping()


class FactoryStore():
    def factorymethod(self, ch, listofscrapedurl):
        if (ch == '1'):
            x = input("Enter File Name")
            fileobj = StoreInFile(x)
            fileobj.StoreData(listofscrapedurl)
        else:
            print("thank You")


def main():

    url = input("Enter The URL To scrap")
    url = checker(url)

    print("1. For Image Scrapping")
    print("2 for icon Scrapping")
    ch = input("which type of scrapping you want to do")

    fact_obj = FactoryScrape(ch, url)
    listofscrapedurl = fact_obj.factorymethod()

    print("Enter 1 to write in a file or 2 to exit")
    ch = input()

    fact_fileobj = FactoryStore()
    fact_fileobj.factorymethod(ch, listofscrapedurl)


main()
