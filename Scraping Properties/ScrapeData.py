from turtle import pd
import requests as r #to interact with webpages
from bs4 import BeautifulSoup as bs #to parse html code
import pandas as pd #to store outcome in dataframe
import re 

URL="https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/krakow?distanceRadius=0&market=ALL&ownerTypeSingleSelect=ALL&page=1&limit=12247&locations=%5Bcities_6-38%5D"
page=r.get(URL)

#open the website#
soup=bs(page.content,"html.parser")

#each property is tagged article with the class below so we assign it to a object#
property_list=soup.find_all("article")

single_property=[] #Will store here details of one property#
all_properties=[] #Will store here details of all properties#

#we find each article and extrac titles, prices and details in 2 loops#
for property in property_list:
    title1=property.find("h3").text
    subtitle=property.find("span").text
    tot_price=''.join([n for n in (property.find("p", class_="css-5kmdsl es62z2j19").text) if n.isdigit()])  #join n for n extracts all digigts and makes from it one string
    rooms_no=''.join([n for n in (property.find("p",class_="css-hxdcpj es62z2j21").find_all("span")[0].text) if n.isdigit()]) #there are 3 details attached to this p so we find all and then extract 0,1,2 of them#
    area=property.find("p",class_="css-hxdcpj es62z2j21").find_all("span")[1].text
    sqr_meter_price=''.join([n for n in (property.find("p",class_="css-hxdcpj es62z2j21").find_all("span")[2].text) if n.isdigit()])
    single_property=[title1,subtitle,tot_price,rooms_no,area,sqr_meter_price]
    print('title1', title1, '\n subtitle', subtitle, "tot_price", tot_price,"rooms_no", rooms_no,"area", area,"sqr_meter",sqr_meter_price)
    all_properties.append(single_property)

df=pd.DataFrame(all_properties, columns=['title','subtitle','price','rooms_no','area','sqr_m_price'])
df.to_csv('properties.csv', index=False)

print(all_properties)


