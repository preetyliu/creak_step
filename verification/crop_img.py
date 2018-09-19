import os
#使用第三方库：Pillow
import math
import operator
from functools import reduce
import requests
from PIL import Image


def get_all_big_img(num):
    """
    下载网站的大部分大图(我是下载的500张, 可能没下载完)
    :param num: 下载的图片数
    """
    url = 'http://www.1kkk.com//image3.ashx?t=1537236807000'
    response = requests.get(url=url)
    if response.status_code == 200:
        with open('./imgs/' + num + '.jpg', 'wb') as f:
            f.write(response.content)


def get_all_small_img():
    """
    分别切出所有大图上面的四张小图
    :return:
    """
    path = '/home/liuzhilong/Downloads/wordspace/pachong_week2/imgs'
    num = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
    for i in range(num):
        print('左 上 右 下')
        ims = Image.open('./imgs/' + str(i) + '.jpg')
        img_small = ims.crop((0, 0, 76, 76))
        img_small.save('./images/' + str(i) + '_1.jpg')
        img_small = ims.crop((76, 0, 152, 76))
        img_small.save('./images/' + str(i) + '_2.jpg')
        img_small = ims.crop((152, 0, 228, 76))
        img_small.save('./images/' + str(i) + '_3.jpg')
        img_small = ims.crop((228, 0, 304, 76))
        img_small.save('./images/' + str(i) + '_4.jpg')


def del_img(i, image1):
    """
    去除一部分相似图片
    :param i: 比对到第几张图片
    :param image1: 正在进行比对的图片
    :return: 返回匹配到相似图片的下标(获得的所有的图片地址组成的是一个列表)
    """
    path1 = '/home/liuzhilong/Downloads/git_objects/verification/img1'
    list1 = os.listdir(path1)
    j = i + 1
    while j < len(list1):
        path3 = os.path.join(path1, list1[j])
        image3 = Image.open(path3)
        # 把图像对象转换为直方图数据，存在list h1、h2 中
        h1 = image1.histogram()
        h2 = image3.histogram()

        result = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
        '''
        sqrt:计算平方根，reduce函数：前一次调用的结果和sequence的下一个元素传递给operator.add
        operator.add(x,y)对应表达式：x+y
        这个函数是方差的数学公式：S^2= ∑(X-Y) ^2 / (n-1)
        '''
        print(result)
        # result的值越大，说明两者的差别越大；如果result=0,则说明两张图一模一样
        if result < 10:
            os.remove(path3)
            # shai_xuan()
            print('=========')
            return j
        j += 1
        print('++++++++++++++', j)


def shai_xuan():
    """
    去除一部分相似图片
    通过循环便利所有切出来的图片，然后分别与其他的图片进行相似度判断，如果相似则删除相似图片
    """
    path1 = '/home/liuzhilong/Downloads/git_objects/verification/img1'
    list1 = os.listdir(path1)
    i = 0
    while i < len(list1) - 1:
        print(i)
        path2 = os.path.join(path1, list1[i])
        image1 = Image.open(path2)
        num = del_img(i, image1)
        if num:
            path1 = '/home/liuzhilong/Downloads/git_objects/verification/img1'
            list1 = os.listdir(path1)
            i = i - 1
        i += 1


def main():
    # 循环500次，下载500张图片
    for num in range(500):
        get_all_big_img(str(num))
    get_all_small_img()
    shai_xuan()


if __name__ == '__main__':
    main()