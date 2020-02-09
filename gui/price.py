import requests
from bs4 import BeautifulSoup

def pound():
	r = requests.get("https://markets.eghtesadnews.com/69386/%D9%BE%D9%88%D9%86%D8%AF")
	parser = BeautifulSoup(r.text,'html.parser')
	allD = parser.find_all("span",{"class":"field-content"})
	return allD[1].get_text() + " T"

def dollar():
	r = requests.get("https://markets.eghtesadnews.com/69384/%D8%AF%D9%84%D8%A7%D8%B1")
	parser = BeautifulSoup(r.text,'html.parser')
	allD = parser.find_all("span",{"class":"field-content"})
	return allD[1].get_text() + " T"

def bitCoin():
	r = requests.get("https://arzdigital.com/coins/bitcoin/")
	parser = BeautifulSoup(r.text,'html.parser')
	allD = parser.find_all("div",{"class":"arz-coin-page-data-coin-toman-price"})
	return allD[0].find('span').get_text() + " T"
