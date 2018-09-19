import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lxml import etree
from PIL import Image
from io import BytesIO
from kkk111 import he_he


browser = webdriver.Chrome()
browser.set_window_size(1300, 600)
wait = WebDriverWait(browser, 10)
# 账号
username = '1315908135@qq.com'
# 密码
password = '123456'


def get_page():
    """
    获取页面的源码
    :return: 页面源码
    """
    url = 'http://www.1kkk.com/vipindex/'
    browser.get(url)
    # print('1')
    html = browser.page_source
    # print(html)
    return html


def get_msg(html):
    etree_html = etree.HTML(html)
    # 点击登录，弹出登录框
    login = wait.until(expected_conditions.element_to_be_clickable(
        (By.CSS_SELECTOR, '.account-info a')))
    login.click()
    print('登录')
    # 输入账号和密码
    user_input = wait.until(expected_conditions.presence_of_element_located(
        (By.NAME, 'txt_name')))
    user_input1 = wait.until(expected_conditions.element_to_be_clickable(
        (By.NAME, 'txt_name')))
    pass_input = wait.until(expected_conditions.presence_of_element_located(
        (By.NAME, 'txt_password')))
    pass_input1 = wait.until(expected_conditions.element_to_be_clickable(
        (By.NAME, 'txt_password')))
    user_input1.click()
    user_input.send_keys(username)
    time.sleep(1)
    pass_input1.click()
    pass_input.send_keys(password)
    time.sleep(1)
    # 把四张验证码图片截取到，然后通过与库存中的图片对比，产生转正验证码需要点击的次数的列表
    for num in range(2, 6):
        name = str(num) + '.png'
        num = str(num)
        get_geetest_image(name, etree_html, num)
    list_num = he_he()
    print(list_num)
    # 通过获取验证码转正的点击次数列表分别点击验证码
    for _ in range(list_num[0]):
        browser.find_element_by_xpath('//div[@class="rotate-background"][1]').click()
    time.sleep(1)
    for _ in range(list_num[1]):
        browser.find_element_by_xpath('//div[@class="rotate-background"][2]').click()
    time.sleep(1)
    for _ in range(list_num[2]):
        browser.find_element_by_xpath('//div[@class="rotate-background"][3]').click()
    time.sleep(1)
    for _ in range(list_num[3]):
        browser.find_element_by_xpath('//div[@class="rotate-background"][4]').click()
    time.sleep(1)
    # 验证码旋转完成后，点击登录按钮登录
    browser.find_element_by_xpath('//button[@id="btnLogin"]').click()
    print('点击完毕')
    time.sleep(2)


def get_position(html, num):
    """
    获取验证码位置
    :return: 验证码位置元组
    """
    img = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                      'body > section.modal-wrap > div > div > div > '
                                                                      'div > div > div:nth-child(' + num + ')')))
    time.sleep(2)
    location = img.location
    size = img.size
    print(size)
    top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
        'width']
    return (top, bottom, left, right)


def get_screenshot():
    """
    获取网页截图
    :return: 截图对象
    """
    screenshot = browser.get_screenshot_as_png()
    screenshot = Image.open(BytesIO(screenshot))
    return screenshot


def get_geetest_image(name, html, num):
    """
    获取验证码图片
    :return: 图片对象
    """
    top, bottom, left, right = get_position(html, num)
    print('验证码位置', top, bottom, left, right)
    screenshot = get_screenshot()
    captcha = screenshot.crop((left, top, right, bottom))
    path = './yanzhengma/' + name
    captcha.save(path)
    return captcha


def main():
    html = get_page()
    # print(html)
    get_msg(html)


if __name__ == '__main__':
    main()