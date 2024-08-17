from bs4 import BeautifulSoup
import re 
import urllib
import pandas as pd
import time
import random
from selenium import webdriver

def main():
     baseurl = "https://www.che168.com/beijing/list/"
     datalist = getData(baseurl)
     saveData(datalist,"car_message.csv")

def getData(baseurl):

    Findcardname = re.compile(r'<h4 class="card-name">(.*?)</h4>',re.S)
    Findcardsunit = re.compile(r'<p class="cards-unit">(.*?)</p>',re.S)
    Findpirce = re.compile(r'<em>(.*?)</em>',re.S)
    FindFpirce = re.compile(r'<s>(.*?)万</s>',re.S)

    count = 0
    datalist = []
    driver = webdriver.Chrome()
    for i in range(1,101):#共100页
        time.sleep(Random())
        url = f"{baseurl}a0_0msdgscncgpi1ltocsp2exx0{i}exx0/?pvareaid=102179#currengpostion"#实现翻页操作
        html = askURL(driver,url)
        #获取网页源代码
        soup = BeautifulSoup(html,"html.parser")
        #使用"hyml.parser"解析器解析储存网页源代码的字符串
        count += 1
        for item in soup.find_all('div',class_="cards-bottom"):
            #查找<div>标签，其必须具有一个名为"cards-bottom"的属性；返回具有该属性的beautifulsoup对象
            #time.sleep(Random())
            data = []
            item = str(item)
            #将item从Beautifulsoup类型转换为str类型

            cardname = re.findall(Findcardname,item)
            if cardname:
                cardname = re.findall(Findcardname,item)[0].strip()
                #在返回的列表中取第一个元素，并使用strip()函数去除其两侧的空白字符
                if "<i class=\"tp-tags cxc-tip\"></i>" in cardname:
                    Cardname = cardname.replace("<i class=\"tp-tags cxc-tip\"></i>","")                     #将可能出现的"<i class=\"tp-tags cxc-tip\"></i>"剔除
                else:
                    Cardname = cardname.replace("\n","")
                data.append(Cardname)
            else:
                data.append("N/A")
            #寻找汽车名称信息

            cardsunit = re.findall(Findcardsunit,item)
            if cardsunit:
                cardsunit = re.findall(Findcardsunit,item)[0].strip()
                Cardsunit = cardsunit.replace("\n","")
                miles = re.findall(r'(.*?)万公里',Cardsunit)
                dates = re.findall(r'／(.*?)／北京',Cardsunit)
                data.append(miles[0] if miles else "N/A")
                data.append(dates[0] if dates else "N/A")
            else:
                data.append("N/A")              

            pirce = re.findall(Findpirce,item)
            if pirce:
                pirce = re.findall(Findpirce,item)[0].strip()
                Pirce = pirce.replace("\n","")
                data.append(Pirce)
            else:
                data.append("N/A")

            Fpirce = re.findall(FindFpirce,item)
            if Fpirce:
                Fpirce = re.findall(FindFpirce,item)[0].strip()
                data.append(Fpirce)
            else:
                data.append("N/A")
            datalist.append(data)
    print("总执行页数为：",count)
    return datalist

def Random():
    random_number = random.uniform(1.0, 1.5)
    return random_number

#打开目标网页，获取网页源代码，存入html并返回
def askURL(driver,url):
    driver.get(url)
    html = driver.page_source
    return html


def saveData(datalist, savepath):
    col = ["汽车型号", "公里数", "上牌日期", "报价", "新车含税价"]
    df = pd.DataFrame(datalist, columns=col)
    df.to_csv(savepath, index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    main()
