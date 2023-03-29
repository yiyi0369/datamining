<center><font size=10>数据分析及实践</font>

<center><font size=8>实验二</middle>

<center><font size=4>PB21000024</middle>
<center><font size=4>王一鸣</middle>

### 实验目的

练习获取数据的能力

### 实验内容

编写爬虫爬取特定网站内容并进行解析

王者英雄数据网站 http://db.18183.com/wzry/ 英雄信息爬取

![image-20230329170350518](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329170350518.png)

### 实验过程

使用python

- 首先获取对应网站的代码

  ![image-20230329170611147](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329170611147.png)

调用request库对对应网站发起请求，爬取网站代码

此时r存取了网站代码，现在我们要获取对我们有用的数据

- 解析网站代码

  

  ![image-20230329170820731](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329170820731.png)

<img src="C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329170910813.png" alt="image-20230329170910813" style="zoom:150%;" />

通过观察网页的代码结构我们发现英雄子页面链接存放在标识符为 *\<li\>* 所在处，并且具有 *class=“mod-iconitem”* 属性，于是可以调用bs4进行查找，得到一个包含各英雄子页面的列表

- 爬取子网站的信息

  通过观察我们发现子网站地址即为主站地址下的 */hero/id.html* 	id即为英雄id，于是可以通过拼接得到子网站链接

  ![image-20230329171731153](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329171731153.png)

- 解析子网站

  同样通过观察子网站代码结构，发现标识符并进行查找

  同样还有基础属性，不予赘述

  ![image-20230329171912776](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329171912776.png)

​		

​			提取 *class=“otherinfo-datapanel”* ,以换行符为界就能分开每个属性，然后进行字符串处理制成字典

![image-20230329172344048](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329172344048.png)

![image-20230329181128677](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329181128677.png)

- 写入文件

  ![image-20230329172444314](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329172444314.png)

![image-20230329181017607](C:\Users\86138\AppData\Roaming\Typora\typora-user-images\image-20230329181017607.png)

以上即为本次实验过程