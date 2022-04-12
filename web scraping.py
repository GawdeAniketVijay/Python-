import requests as req
from bs4 import Beautifulsoup

website=req.get('https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi&otracker=nmenu_sub_Electronics_0_Mi')
bsoup=Beautifulsoup(website.content,'html.praser')
bsoup.prettify()#for formating the website content.
bsuop.encode('UTF-8')
#prices
mi_prices_div=bsoup.findAll('div',attrs={'class':'_30jeq3'})
mi_prices_list=[]
for div in mi_prices_div:
    mi_prices_list.append(div.text)

print(mi_prices_list)
#names
mi_names_div=bsoup.findAll('div',attrs={'class':'_4rRo1t'})
mi_names_list=[]
for div in mi_names_div:
    mi_names_list.append(div.text)
print(mi_names_list)
#to find all items names and prices together
itemlist=zip(mi_names_list,mi_prices_list)
for item in itemlist:
    print(item)
