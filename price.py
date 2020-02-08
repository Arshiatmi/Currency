import requests
from bs4 import BeautifulSoup

cmd = input("""
Which One ? 

	[1] => Dollar
	[2] => Pound
	[3] => Bit Coin
	[4] => All Of Them
: """)

cmd = int(cmd)

def pound():
	r = requests.get("https://markets.eghtesadnews.com/69386/%D9%BE%D9%88%D9%86%D8%AF")
	parser = BeautifulSoup(r.text,'html.parser')
	allD = parser.find_all("span",{"class":"field-content"})
	print("Pound : " + allD[1].get_text())

def dollar():
	r = requests.get("https://markets.eghtesadnews.com/69384/%D8%AF%D9%84%D8%A7%D8%B1")
	parser = BeautifulSoup(r.text,'html.parser')
	allD = parser.find_all("span",{"class":"field-content"})
	print("Dollar : " + allD[1].get_text())

def bitCoin():
	r = requests.get("https://arzdigital.com/coins/bitcoin/")
	parser = BeautifulSoup(r.text,'html.parser')
	allD = parser.find_all("div",{"class":"arz-coin-page-data-coin-toman-price"})
	print("Bit Coin : " + allD[0].find('span').get_text())

def all():
	pound()
	dollar()
	bitCoin()

if cmd == 1:
	dollar()
elif cmd == 2:
	pound()
elif cmd == 3:
	bitCoin()
else:
	all()
