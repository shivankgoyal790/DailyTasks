from webscrapping import Webscraping
import requests

original_url = input("enter URL")
response = requests.head(original_url, allow_redirects=True)
print(response)
if response.is_redirect:
    print("Redirecting")
    w = Webscraping(response.headers["Location"])
    w.webscrape()
    w.geticons()
else:
    print("Not redirecting")
    w = Webscraping(original_url)
    w.webscrape()
    w.geticons()
