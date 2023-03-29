import requests
from bs4 import BeautifulSoup
import re
import json
# 设置要爬取的页面的URL

url = 'http://db.18183.com/wzry/'
r=requests.get(url)

#爬取总页面
soup=BeautifulSoup(r.text,'lxml')
#从总页面得到各个分页面信息
heros=soup.find_all('li',class_='mod-iconitem')

if(len(heros)==0):
    print("failed!")
sample=[]
count=200
for hero in heros:
    count-=1
    if(count==0):
        break
    url_=url+'hero/'+hero['data-id']+'.html'#访问分页面
    
    #print(hero.p.text)
    r=requests.get(url_)
    soup=BeautifulSoup(r.text,'lxml')
    out=soup.find('div', class_='otherinfo-datapanel')#提取英雄信息列表
    base_attri=soup.find('div', class_='attr-list')
    
    pattern=re.compile('\n+')
    
    
    try:
        out=re.split(pattern,out.text)
        base_attri=[base_attri.select('span')[i]['class'][-1][5:] for i in range(4)]#星级
    except Exception:
        continue
    else:
        temp={}
        temp['id']=hero['data-id']
        temp['name']=hero.p.text
        temp['生存能力']=base_attri[0]
        temp['攻击伤害']=base_attri[1]
        temp['技能效果']=base_attri[2]
        temp['上手难度']=base_attri[3]
        for i in range(len(out)):
            if(out[i]==''):
                continue
            out[i]=out[i].split('：')
            out[i][1]=re.sub(re.compile('\s+'),'',out[i][1])
            out[i][1]=re.sub(re.compile('%+'),'%',out[i][1])
            temp[out[i][0]]=out[i][1]
        sample.append(temp)#生成字典
        #print(temp)
            
                
        #print(url_,'\n')
#文件写入
file=open('result.json','w',encoding='utf8')       
for item in sample:
    
    file.write(json.dumps(item,ensure_ascii=False))
    file.write('\n')
file.close()
#print(sample)
#print('end')
