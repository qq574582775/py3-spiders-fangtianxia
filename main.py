import requests
from bs4 import BeautifulSoup

res=requests.get('http://cd.esf.fang.com/house-a016418/')
#print(res.text)
soup = BeautifulSoup(res.text,"html.parser")