#import re

#print(re.findall("ab*c", "ac"))

#p#rint(re.findall("ab*c", "abcd"))

#print(re.findall("ab*c", "acc"))

#print(re.findall("ab*c", "abcac"))

#print(re.findall("ab*c", "abdc"))

#un tercer argumento con el valor re.IGNORECASE:
#print(re.findall("ab*c", "ABC", re.IGNORECASE)) 

# Punto . toma el valor
#print(re.findall("a.c", "abc"))

#print(re.findall("a.c", "abbc"))

#print(re.findall("a.c", "ac"))

#print(re.findall("a.c", "acc"))

#  .*dentro de una expresión regular 

#print(re.findall("a.*c", "abc"))

#print(re.findall("a.*c", "abbc"))

#print(re.findall("a.*c", "ac"))

#print(re.findall("a.*c", "acc"))

#match_results = re.search("ab*c", "ABC", re.IGNORECASE)
#print(match_results.group())

#le permite reemplazar el texto en una cadena que coincide con una expresión regular con texto nuevo
#string = "Everything is <replaced> if it's in <tags>."
#string = re.sub("<.*>", "ELEPHANTS", string)
#print(string)

#Coincidecia corta 
#string = "Everything is <replaced> if it's in <tags>."
#string = re.sub("<.*?>", "ELEPHANTS", string)
#print(string)

# regex_soup.py

#Expresion regulares

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

#pattern = "<title.*?>.*?</title.*?>"
#match_results = re.search(pattern, html, re.IGNORECASE)
#title = match_results.group()
#title = re.sub("<.*?>", "", title) # Remove HTML tags
#print(title)

name_index = html.find("Name:")
start_index = name_index + len("Name: ")
end_index = html.find("</h2")
name = html[start_index:end_index]
print(name)

color_index = html.find("Favorite Color: ")
start_index = color_index + len("Favorite Color: ")
end_index = html.find("</center>")
color = html[start_index:end_index]
print(color)