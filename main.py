import requests
from bs4 import BeautifulSoup

res=requests.get('http://cd.esf.fang.com/house-a016418/')
#print(res.text)
soup = BeautifulSoup(res.text,"html.parser")
houses = soup.select(".shop_list.shop_list_4 dl")
#print(houses)
#域名
domain = "http://cd.esf.fang.com"
for house in houses:
    try:
        print(domain+house.select(".clearfix a")[0]['href'])
        #getHouseInfo(domain+house.select(".clearfix a")[0]['href'])
    except Exception as e:
        print("----->",e)


#https://ke.qq.com/webcourse/index.html#cid=303312&term_id=100359427&taid=2117521956446416&vid=k142628kka6