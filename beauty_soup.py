# Extraer datos 

from urllib.request import urlopen
from bs4 import BeautifulSoup

url_base = "http://olympus.realpython.org"
url = url_base + "/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

links = soup.find_all('a')

for link in links:
    print(url_base + link['href'])

