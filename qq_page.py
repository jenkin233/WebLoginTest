# -*- coding: utf-8 -*-

# import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
# import pytesseract
import time
# import logging
# from PIL import Image, ImageEnhance


class BasePage(object):
    """ 定义所有页面类的基类 """

    def __init__(self, driver):
        self.driver = driver

    def get_source(self):
        """
        获取页面源码
        :return:
        """
        return self.driver.page_source

    def accept_alert(self):
        """
        切换到alert窗口，并且点击确定
        :return: 返回alert信息
        """
        wait = WebDriverWait(self.driver,1, 0.5)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert

    def check_selected(self,id):

    	wait = WebDriverWait(self.driver,2, 0.5)
    	wait.until(EC.element_to_be_selected((By.ID,id)))

class LoginPage(BasePage):
    """ 登录页面类 """

    # 定义第一个待测页面
    url = "https://mail.qq.com"

    # def get_verify_code(self):

    #     # 截图
    #     self.driver.get_screenshot_as_file(r'C:\Users\lzsun\Pictures\base.png')

    #     img = self.driver.find_element_by_xpath("//div[@id='login_main']//img")
        
    #     location = img.location
    #     print location
    #     size = img.size
    #     print size

    #     width = img.get_attribute("width")
    #     height = img.get_attribute("height")

    #     left = location['x']
    #     top = location['y']
    #     right = left + float(width)
    #     bottom = top + float(height)

    #     box = (left,top,right,bottom)

    #     im = Image.open(r'C:\Users\lzsun\Pictures\base.png')
    #     region = im.crop(box)
    #     region.save(r'C:\Users\lzsun\Pictures\1.png')
    #     time.sleep(1)
    #     ima = Image.open(r'C:\Users\lzsun\Pictures\1.png')
    #     imgry = ima.convert('L')  # 图像加强，二值化
    #     sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    #     sharp_img = sharpness.enhance(2.0)
    #     sharp_img.save(r'C:\Users\lzsun\Pictures\2.png')
    #     tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
    #     code = pytesseract.image_to_string(Image.open(r'C:\Users\lzsun\Pictures\2.png'),config=tessdata_dir_config) # code即为识别出的图片数字str类型
    #     print "code:",code

    #     time.sleep(10)
    #     img.location()
    #     return code
    
    def get_element_attr(self,id,attr):
        return self.driver.find_element_by_id(id).get_attribute(attr)

    def back(self):
        self.driver.back()

    def login_success(self):
    	return "写信" in self.get_source()	

    def click_by_id(self,id):
        self.driver.find_element_by_id(id).click()
    def click_by_xpath(self,path):
        self.driver.find_element_by_xpath(path).click()

    def open_login(self):

        # 打开首页
        self.driver.get(LoginPage.url)

        #跳转到登陆界面
        login_frame = self.driver.find_element_by_id("login_frame")
        login_url = login_frame.get_attribute("src")

        self.driver.get(login_url)
        # 切换到账号密码登陆
        self.driver.find_element_by_id("switcher_plogin").click()

    def input_user_pwd(self,user,pwd):
        # 输入用户名
        account = self.driver.find_element_by_id("u")
        account.clear()
        account.send_keys(user)

        # 输入密码
        password = self.driver.find_element_by_id("p")
        password.clear()
        password.send_keys(pwd)

    def login_submit(self,delay=True):
        submit = self.driver.find_element_by_id("login_button")
        submit.click()
        if delay:
            time.sleep(3)
    
    def remember_me(self):
        self.driver.find_element_by_id("low_login_wording").click()

    def login(self, user, pwd,remember_me=False):

        self.open_login()
        self.input_user_pwd(user,pwd)
        if remember_me:
            self.remember_me()
        self.login_submit()


if __name__ == '__main__':
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    driver = webdriver.Chrome(chrome_options=options)
    login_page = LoginPage(driver)
    login_page.login("gfc@qq.com", "123456")