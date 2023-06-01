from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(url)

time.sleep(10)

stars_data = []
headers=["name","distance","mass","radius"]
NAMES=[]
DISTANCE=[]
MASS=[]
RADIUS=[]

def scrape(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.page")

        temp_list=[]
        

        for tr_tag in soup.find_all("tr",attrs={"table"}):
            td_tags = tr_tag.find_all("td")
        
            for td_tag in td_tags:
                try:

                    td=td_tag.find_all("td")
                    row = [i.text.rstrip() for i in td]
                    temp_list.append(row)

                except:
                    temp_list.append("")
    except:
        time.sleep(1)
        scrape(hyperlink)
    
    for i in range(1,len(temp_list)):
        NAMES.append(temp_list[i][1])
        DISTANCE.append(temp_list[i][3])
        MASS.append(temp_list[i][5])
        RADIUS.append(temp_list[i][6])
  
                
                     
    

df1=pd.DataFrame(list(zip(NAMES,DISTANCE,MASS,RADIUS)), columns=['Star_name', 'Distance', 'Mass', 'Radius'])
print(df1)
df1.to_csv('scraped_data.csv', index=True, index_label="id")
        


