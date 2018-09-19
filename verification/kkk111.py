import os

from PIL import Image


def cha_xun(image1, image2, x, y):
    pixel1 = image1.load()[x, y]
    pixel2 = image2.load()[x, y]
    threshold = 60
    if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(
            pixel1[2] - pixel2[2]) < threshold:
        return True
    else:
        return False


def get_gap(image1, image2):
    """
    获取缺口偏移量
    :param image1: 不带缺口图片
    :param image2: 带缺口图片
    :return:
    """
    z = 0
    for i in range(20, 60):
        for j in range(20, 60):
            if not cha_xun(image1, image2, i, j):
                z += 1
    return z


def qu_chong(path3, y):
    """
    把验证码截的图片与库存中的每张图片进行比对
    :param path3: 验证码图片地址
    :param y: 验证码点击次数
    :return: num:不同的点数 , 'lala':没找到相似图片
    """
    j = 0
    # 存放的库存图片路径
    path1 = '/home/liuzhilong/Downloads/git_objects/verification/img1'
    list1 = os.listdir(path1)
    while j < len(list1):
        path2 = os.path.join(path1, list1[j])
        image1 = Image.open(path3)
        if y == 0:
            image2 = Image.open(path2)
        else:
            image3 = Image.open(path2)
            image2 = image3.rotate(y * 90)
            # print(y * 90)
        num = get_gap(image1, image2)
        if num < 300:
            return num
        # print(j)
        j += 1
    return 'lala'


def he_he():
    """
    得到验证码转正需要的次数列表
    :return: 验证码从左到右需要低级的次数列表
    y： 需要点击的次数
    """
    y = 0
    list_num = []
    # 存放的验证码图片路径
    path1 = '/home/liuzhilong/Downloads/git_objects/verification/yanzhengma'
    list1 = os.listdir(path1)
    list1.sort(key=lambda x: int(x[:-4]))
    print(list1)
    i = 0
    while i < len(list1):
        # print('++++++++++', i)
        path3 = os.path.join(path1, list1[i])
        num = qu_chong(path3, y)
        # 如果一次就匹配到相似图片
        if num != 'lala':
            list_num.append(0)
            print('++++++++++', num)
        # 没有一次匹配成功
        else:
            x = 0
            # 通过旋转再次进行匹配
            for _ in range(3):
                y += 1
                # print(count)
                x = qu_chong(path3, y)
                if x != 'lala':
                    list_num.append(y)
                    break
            # 如果旋转了3次还没匹配到，说明我的库存没有这张图片或者算法匹配不到这张图
            if x == 'lala':
                list_num.append(0)
            print('x= %s' % x)
        y = 0
        i += 1
        print('=============')
    # print(list_num)
    return list_num


if __name__ == '__main__':
    he_he()
