### 破解四张图片的旋转验证码步骤

##### 本文是以```http://www.1kkk.com/vipindex/```为例

代码文件：
```
crop_img: 下载图片并进行切割
creak_kkk: 主程序代码
kkk111: 图片像素对比代码
```


###### 一、先获取网站的所有验证码图片

破解这个验证码我的方法比较繁琐，首先需要下载到这个验证码的所有图片，因为下载下来的是以16张小图组合的一张大图，所有需要把每张大图的最上面四张小图分别切出来存放好，然后把这些小图的方向全部转正（我只下载了500张大图，切完之后进行了去重，减少转正图片的工作量，不过这个工作量还是很大。。。。。。。。。）

下载图片的步骤我想应该不用写了吧。。。。如果实在不会可以看我的代码

我这个方法还是很繁琐(主要是需要 "手工" 把图片转正)，成功率大概百分之八九十所有，不过还是算是破了。。。

###### 二、拿到转正后的所有图之后的步骤

1、运用selenium模拟浏览器获取网页源码
2、解析网页源码，点击登录按钮，弹出登录的输入框
3、模拟输入用户名和密码
4、分别截取四张验证码，把验证码存起来
5、分别用这四张验证码与库存中所有转正的图片进行像素对比，如果匹配不到相同图片则旋转90度之后再次与所有图片进行匹配，旋转的同时以一个变量来计数，旋转一次，变量加1，以此来作为到时需要点击的次数，直到匹配到为止。(旋转三次后如果还匹配不到，则证明你的库存没有这个图片或者像素匹配算法不成功)
6、把点击的次数分别加入一个列表返回
7、通过返回的列表，分别以对应的次数点击验证码，则验证码会自动转正。



