import requests
from bs4 import BeautifulSoup

r = requests.get("https://markets.eghtesadnews.com/69386/%D9%BE%D9%88%D9%86%D8%AF")

parser = BeautifulSoup(r.text,'html.parser')
allD = parser.find_all("span",{"class":"field-content"})
print("Pound : " + allD[1].get_text())

r = requests.get("https://markets.eghtesadnews.com/69384/%D8%AF%D9%84%D8%A7%D8%B1")

parser = BeautifulSoup(r.text,'html.parser')
allD = parser.find_all("span",{"class":"field-content"})
print("Dollar : " + allD[1].get_text())
