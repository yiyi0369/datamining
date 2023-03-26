import requests
from bs4 import BeautifulSoup
import re
import json
# 设置要爬取的页面的URL

url = 'http://db.18183.com/wzry/'
r=requests.get(url)


soup=BeautifulSoup(r.text,'lxml')

heros=soup.find_all('li',class_='mod-iconitem')


sample=[]
count=200
for hero in heros:
    count-=1
    if(count==0):
        break
    url_=url+'hero/'+hero['data-id']+'.html'
    
    print(hero.p.text)
    r=requests.get(url_)
    soup=BeautifulSoup(r.text,'lxml')
    out=soup.find('div', class_='otherinfo-datapanel')
    pattern=re.compile('\n+')
    try:
        out=re.split(pattern,out.text)
    except Exception:
        continue
    else:
        temp={}
        temp['id']=hero['data-id']
        temp['name']=hero.p.text
        for i in range(len(out)):
            if(out[i]==''):
                continue
            out[i]=out[i].split('：')
            out[i][1]=re.sub(re.compile('\s+'),'',out[i][1])
            out[i][1]=re.sub(re.compile('%+'),'%',out[i][1])
            temp[out[i][0]]=out[i][1]
        sample.append(temp)
        print(temp)
            
                
        print(url,'\n')
 
file=open('result.json','w',encoding='utf8')       
for item in sample:
    
    file.write(json.dumps(item,ensure_ascii=False))
    file.write('\n')
file.close()
print(sample)
print('end')
