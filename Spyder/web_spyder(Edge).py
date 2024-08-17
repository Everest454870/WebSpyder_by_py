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
    FindFpirce = re.compile(r'<s>(.*?)涓�</s>',re.S)

    count = 0
    datalist = []
    driver = webdriver.Edge()
    for i in range(1,101):#鍏�100椤�
        time.sleep(Random())
        url = f"{baseurl}a0_0msdgscncgpi1ltocsp2exx0{i}exx0/?pvareaid=102179#currengpostion"#瀹炵幇缈婚〉鎿嶄綔
        html = askURL(driver,url)
        #鑾峰彇缃戦〉婧愪唬鐮�
        soup = BeautifulSoup(html,"html.parser")
        #浣跨敤"hyml.parser"瑙ｆ瀽鍣ㄨВ鏋愬偍瀛樼綉椤垫簮浠ｇ爜鐨勫瓧绗︿覆
        count += 1
        for item in soup.find_all('div',class_="cards-bottom"):
            #鏌ユ壘<div>鏍囩锛屽叾蹇呴』鍏锋湁涓€涓悕涓�"cards-bottom"鐨勫睘鎬э紱杩斿洖鍏锋湁璇ュ睘鎬х殑beautifulsoup瀵硅薄
            #time.sleep(Random())
            data = []
            item = str(item)
            #灏唅tem浠嶣eautifulsoup绫诲瀷杞崲涓簊tr绫诲瀷

            cardname = re.findall(Findcardname,item)
            if cardname:
                cardname = re.findall(Findcardname,item)[0].strip()
                #鍦ㄨ繑鍥炵殑鍒楄〃涓彇绗竴涓厓绱狅紝骞朵娇鐢╯trip()鍑芥暟鍘婚櫎鍏朵袱渚х殑绌虹櫧瀛楃
                if "<i class=\"tp-tags cxc-tip\"></i>" in cardname:
                    Cardname = cardname.replace("<i class=\"tp-tags cxc-tip\"></i>","")                     #灏嗗彲鑳藉嚭鐜扮殑"<i class=\"tp-tags cxc-tip\"></i>"鍓旈櫎
                else:
                    Cardname = cardname.replace("\n","")
                data.append(Cardname)
            else:
                data.append("N/A")
            #瀵绘壘姹借溅鍚嶇О淇℃伅

            cardsunit = re.findall(Findcardsunit,item)
            if cardsunit:
                cardsunit = re.findall(Findcardsunit,item)[0].strip()
                Cardsunit = cardsunit.replace("\n","")
                miles = re.findall(r'(.*?)涓囧叕閲�',Cardsunit)
                dates = re.findall(r'锛�(.*?)锛忓寳浜�',Cardsunit)
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
    print("鎬绘墽琛岄〉鏁颁负锛�",count)
    return datalist

def Random():
    random_number = random.uniform(1.0, 1.5)
    return random_number

#鎵撳紑鐩爣缃戦〉锛岃幏鍙栫綉椤垫簮浠ｇ爜锛屽瓨鍏tml骞惰繑鍥�
def askURL(driver,url):
    driver.get(url)
    html = driver.page_source
    return html


def saveData(datalist, savepath):
    col = ["姹借溅鍨嬪彿", "鍏噷鏁�", "涓婄墝鏃ユ湡", "鎶ヤ环", "鏂拌溅鍚◣浠�"]
    df = pd.DataFrame(datalist, columns=col)
    df.to_csv(savepath, index=False, encoding="utf-8-sig")

if __name__ == "__main__":
    main()
