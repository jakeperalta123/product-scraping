from bs4 import BeautifulSoup
import requests

File = open("out.csv", "a")
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}


urls = []

with open("url.txt", "r") as file:
    for line in file:
        urls.append(line.strip())
    print(urls)

URL = urls[0]
webpage = requests.get(URL, headers=Headers)
soup = BeautifulSoup(webpage.content, "lxml")

try:
    title = soup.find("span", attrs={"id":'productTitle'})
    title_value = title.string
    title_string = title_value.strip().replace(',', '')
    print("Success! Product title = ", title_string)
except AttributeError:
    title_string = "NA"
    print("product title = ", title_string)