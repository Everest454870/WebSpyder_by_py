# python网络爬虫实战
目标网页为："https://www.che168.com/beijing/list/" ，该网站上北京地区的在售二手车信息。
## 一、爬虫部分
（1）调用selenium库中的webdriver包，访问网站，获取网页源代码；

（2）使用BeautifulSoup包和正则表达式对源代码字符串进行处理；

（3）将处理后的字符串转换为Dataframe对象，利用pandas库将其写入.csv文件
## 二、数据可视化

在这一部分中，主要调用pandas库和matplotlib库。
其中，从pandas库中调用read_csv()函数，将.csv文件读取为dataframe数据类型。
再调用matplotlib库进行绘图操作：

（1）绘制柱状图：横坐标为上牌年份（包括“未上牌”），纵坐标为数量；

（2）绘制圆饼图：不同报价的在售汽车数量分布；

（3）绘制箱线图：横坐标为序号，代表的含义与柱状图相同；纵坐标为数量。共有两个图，一张包含报价低于百万的汽车，另一张只有售价高于百万的汽车。
