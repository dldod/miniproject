# from typing import Coroutine
import pandas as pd
# import matplotlib.pyplot as plt
# from urllib.parse import quote
import urllib.request
from bs4 import BeautifulSoup
import re
import csv 



list = []

fclt_name = '고창갯벌축제'
df2019 = pd.read_csv('2019.csv',encoding='cp949')

for i in df2019.index:

    if fclt_name == df2019['fclt_name'][i] :

        query = urllib.parse.quote(df2019['fclt_name'][i])
        s_year = df2019['fstvl_bgn_dt_year'][i]
        s_month = format(df2019['fstvl_bgn_dt_month'][i],'02')   
        d_year = df2019['fstvl_end_dt_year'][i]
        d_month = format(df2019['fstvl_end_dt_month'][i],'02')



url = 'https://search.naver.com/search.naver?where=news&query={}&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds={}.{}.00&de={}.{}.32'.format(query,s_year,s_month,d_year,d_month)
# print(url)
search_url = urllib.request.urlopen(url).read()

soup = BeautifulSoup(search_url, 'html.parser')
links = soup.find_all(class_= 'news_tit')

for link in links :
    # print(link)
    news_link = urllib.request.urlopen(link.attrs['href']).read()
    news_html = BeautifulSoup(news_link,'html.parser')
    try : 
        title = news_html.find(class_ = 'article-head-title').get_text()
        title = title.split(' ')
        list.append(title)
        
        body  = news_html.find(class_ = 'user-snb-wrapper').get_text()
        body2=(re.sub("[^가-힣 ]", "", body))
        body2=body2.split(' ')
        list.append(body2)   
        
    except :
        print('안됨')
f = open('wordcloud_ssh.csv','w',encoding='cp949',newline='')

f2 = csv.writer(f)
for i in list :
    f2.writerow(i)
f.close()


















