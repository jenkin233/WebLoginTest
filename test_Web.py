# -*- coding: utf-8 -*-
import pytest
import allure
import os
import time
import math
from selenium import webdriver
from qq_page import LoginPage
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def get_driver(request):
  
    driver = webdriver.Chrome()
    # 设置一个全局的等待超时时间 10s
    driver.implicitly_wait(10)

    def fin():
    	driver.quit()
    
    request.addfinalizer(fin)

    return driver

@allure.feature('登录模块测试')
class TestLogin(object):

	user = "2073561622@qq.com"
	correct_pwd = "sunlz961005"

	any_user = "2043531622@qq.com"
	error_passwd = "xxxxxxxxxx"

	### 功能测试
	# @allure.story('功能测试')
	# def test_login_success(self,get_driver):
	# 	'''测试正常登陆'''
	# 	print ("测试正常登陆...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面,输入正确的用户名，密码'):
	# 		login_page.login(self.user,self.correct_pwd,False)
	# 	with allure.step('登陆成功后，页面中包含写信'):
	# 		assert login_page.login_success()
	
	# @allure.story('功能测试')
	# def test_login_emptycheck(self,get_driver):
	# 	'''非空检查'''
	# 	print ("测试对于用户名/密码非空检查...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面'):
	# 		login_page.open_login()
	# 	with allure.step('什么都不输入,点击登录'):
	# 		# 登录且不等待
	# 		login_page.login_submit(False)
	# 	with allure.step('界面提示输入用户名'):
	# 		pass
	# 		# assert "输入账号" in login_page.get_source()
	# 	with allure.step('只输入用户名,点击登录'):
	# 		login_page.input_user_pwd(self.user,"")
	# 		login_page.login_submit(False)
	# 	with allure.step('界面提示输入密码'):
	# 		pass
	# 		#assert "输入密码" in login_page.get_source()
	# 	with allure.step('只输入密码,点击登录'):
	# 		login_page.input_user_pwd("","123456")
	# 		login_page.login_submit(False)
	# 	with allure.step('界面提示输入用户名'):
	# 		pass
	# 		#assert "输入账号" in login_page.get_source()

	# @allure.story('功能测试')
	# def test_login_fail(self,get_driver):
	# 	'''输入错误的用户名/密码'''
	# 	print ("测试错误用户名/密码登陆...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面,输入错误的用户名/密码'):
	# 		login_page.login(self.user,"any",False)
	# 	with allure.step('提示用户名/密码错误'):
	# 		print (login_page.get_source())
	# 		#assert "账号或密码不正确" in login_page.get_source()
	
	@allure.story('功能测试')
	def test_login_correct(self,get_driver):
		'''登陆后跳转到正确页面'''
		print ("测试登陆后跳转到正确页面..."),
		with allure.step('初始化浏览器driver'):
			login_page = LoginPage(get_driver)
		with allure.step('打开登陆界面,输入正确的用户名，密码'):
			login_page.login(self.user,self.correct_pwd,False)
		with allure.step('界面中包含邮箱首页'):
			assert "邮箱首页" in login_page.get_source()

	# @allure.story('功能测试')
	# def test_user_too_long(self,get_driver):
	# 	'''测试用户名/密码过长'''
	# 	print ("测试输入用户名/密码过长..."),
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面,输入20位用户名和密码'):
	# 		login_page.open_login()
	# 		user = "a"*20
	# 		login_page.input_user_pwd(user,user)
	# 	with allure.step('输入的用户名小于20位'):
	# 		if len(login_page.get_element_attr("u","value")) < 20:
	# 			pass
	# 		else:
	# 			pytest.fail("输入用户名长度没有限制")
	# 	with allure.step('输入的密码小于20位'):
	# 		if len(login_page.get_element_attr("p","value")) < 20:
	# 			pass
	# 		else:
	# 			pytest.fail("输入密码长度没有限制")
	
	# @allure.story('功能测试')
	# def test_auto_login(self,get_driver):
	# 	'''测试自动登录'''
	# 	print ("测试自动登陆..."),
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面,正确的用户名密码,并勾选记住我'):
	# 		login_page.login(self.user,self.correct_pwd,True)
	# 	with allure.step('后退并检查是否自动登陆'):
	# 		login_page.back()
	# 		time.sleep(3)
	# 		assert login_page.login_success()

	# @allure.story('功能测试')
	# def test_user_spce_filter(self,get_driver):
	# 	'''测试用户名空格过滤'''
	# 	print ("测试用户名空格过滤..."),
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面,正确的用户名密码,用户名前后加空格'):
	# 		login_page.login("  "+self.user+"  ",self.correct_pwd,False)
	# 	with allure.step('检查登陆成功'):
	# 		assert login_page.login_success()
	
	# @allure.story('功能测试')
	# def test_pwd_with_space(self,get_driver):
	# 	'''测试密码前后有空格'''
	# 	print ("测试密码前后有空格..."),
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面,正确的用户名密码,在密码前后加空格'):
	# 		login_page.login(self.user,"  "+self.correct_pwd+" ",False)
	# 	with allure.step('检查登陆失败'):
	# 		assert not login_page.login_success()

	# @allure.story('功能测试')
	# def test_func(self,get_driver):
	# 	'''注册、忘记密码等链接是否正确'''
	# 	print ("测试注册、忘记密码等链接是否正确..."),
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面'):
	# 		login_page.open_login()
	# 	with allure.step('点击忘记密码，确认跳到密码重置页面'):
	# 		login_page.click_by_id("forgetpwd")
	# 		time.sleep(3)
	# 		# 获得当前窗口句柄集合
	# 		handles = login_page.driver.window_handles
	# 		for handle in handles:
	# 			if handle != login_page.driver.current_window_handle:
	# 				login_page.driver.switch_to.window(handle)
	# 				break
	# 		assert "重置" in login_page.driver.title
	# 		login_page.driver.close()
	# 		# 切回主窗口
	# 		login_page.driver.switch_to.window(handles[0])
	# 	with allure.step("点击注册，进入注册页面"):
	# 		login_page.click_by_xpath("//a[@href='http://zc.qq.com/chs/index.html?type=1']")
	# 		time.sleep(3)
	# 		# 获得当前窗口句柄集合
	# 		handles = login_page.driver.window_handles
	# 		for handle in handles:
	# 			if handle != login_page.driver.current_window_handle:
	# 				login_page.driver.switch_to.window(handle)
	# 				break
	# 		assert "注册" in login_page.get_source()
	# 		login_page.driver.close()
	# 		# 切回主窗口
	# 		login_page.driver.switch_to.window(handles[0])
	# 		time.sleep(1)

	# @allure.story('功能测试')
	# def test_pwd_hidden_show(self,get_driver):
	# 	'''测试密码是否加星显示'''
	# 	print ("测试密码是否加星显示..."),
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面,输入密码'):
	# 		login_page.open_login()
	# 		login_page.driver.find_element_by_id("p").send_keys("testpassword")
	# 		time.sleep(1)
	# 	with allure.step('判断密码是否加星显示'):
	# 		assert "password" == login_page.get_element_attr("p","type")


	# ### 界面测试
	# @allure.story('界面测试')
	# def test_box_allignment(self,get_driver):
	# 	'''测试textbox和按钮是否对齐'''
	# 	print ("测试textbox和按钮是否对齐..."),
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面，获得所有元素坐标'):
	# 		login_page.open_login()
	# 		user_location = login_page.driver.find_element_by_id("u").location
	# 		user_size = login_page.driver.find_element_by_id("u").size
			
	# 		pwd_location = login_page.driver.find_element_by_id("p").location
	# 		pwd_size = login_page.driver.find_element_by_id("p").size

	# 		btn_location = login_page.driver.find_element_by_id("login_button").location
	# 		btn_size = login_page.driver.find_element_by_id("login_button").size
	# 	with allure.step('判断所有元素对齐'):
	# 		# 最左侧坐标
	# 		assert abs(user_location['x']-pwd_location['x']) < 3
	# 		assert abs(user_location['x']-btn_location['x']) < 3

	# 		#最右侧坐标
	# 		assert abs(user_size['width'] - pwd_size['width']) < 3
	# 		assert abs(user_size['width'] - btn_size['width']) < 3

	# ### 性能测试
	# @allure.story('性能测试')
	# def test_open_login_speed(self,get_driver):
	# 	'''测试打开速度'''
	# 	print ("测试打开速度...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('测试界面打开速度'):
	# 		start = time.clock()
	# 		login_page.open_login()
	# 	with allure.step('检测是否在5s内完成'):
	# 		if time.clock()-start >5:
	# 			pytest.fail("打开登陆界面超时")

	# @allure.story('性能测试')
	# def test_login_succ_speed(self,get_driver):
	# 	'''登陆速度测试'''
	# 	print ("测试登录速度...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登录界面'):
	# 		login_page.open_login()
	# 	with allure.step('输入正确的用户名,密码,开始计时'):
	# 		login_page.input_user_pwd(self.user,self.correct_pwd)
	# 		start = time.clock()
	# 		login_page.login_submit(False)
	# 	with allure.step('检测是否在5s内完成'):
	# 		# 等待主界面加载
	# 		login_page.driver.find_element_by_id("mainFrameContainer")
	# 		if time.clock()-start > 5:
	# 			pytest.fail("登陆超时")
	# # 			
	# # 			
	# ### 安全性测试
	# @allure.story('安全性测试')
	# def test_cookie_httponly(self,get_driver):
	# 	'''登陆后的cookie'''
	# 	print ("测试登陆后的cookie...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('正确登录'):
	# 		login_page.login(self.user,self.correct_pwd,False)
	# 	with allure.step('获取cookie'):
	# 		cookies = login_page.driver.get_cookies()
	# 	with allure.step('检测cookie是否httponly'):
	# 		new_cookies = [cookie for cookie in cookies if cookie['value']=="2073561622@qq.com"]
	# 		for cookie in new_cookies:
	# 			assert cookie['httpOnly'] == True

	# @allure.story('安全性测试')
	# def test_user_passwd_enc(self,get_driver):
	# 	'''用户名密码是否加密传输'''
	# 	print ("测试用户名密码是否加密传输...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登录界面'):
	# 		login_page.open_login()
	# 	with allure.step('检查链接是否为https'):
	# 		url = login_page.driver.current_url
	# 		assert "https" in url
	
	# @allure.story('安全性测试')
	# def test_sql(self,get_driver):
	# 	'''SQL注入攻击'''
	# 	print ("测试SQL注入攻击...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登录界面,使用注释方法1'):
	# 		login_page.login(self.any_user+"'#","234")
	# 	with allure.step('不能登录成功'):
	# 		assert not login_page.login_success()

	# 	with allure.step('打开登录界面,使用注释方法2'):
	# 		login_page.login(self.any_user+"'-- ","234")
	# 	with allure.step('不能登录成功'):
	# 		assert not login_page.login_success()
	
	# @allure.story('安全性测试')
	# def test_xss(self,get_driver):
	# 	'''xss攻击'''
	# 	print ("测试xss攻击...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登录界面,输入脚本语句'):
	# 		login_page.login("<srcipt>alert('f')</srcipt>","234")
	# 	with allure.step('脚本不会被执行'):
	# 		try:
	# 			login_page.accept_alert()
	# 		except:
	# 			pass
	# 		else:
	# 			pytest.fail("xss攻击成功,alert被显示")
	
	# @allure.story('安全性测试')
	# def test_brute_force(self,get_driver):
	# 	'''错误登录次数限制'''
	# 	print ("测试防止暴力破解...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登录界面,输入脚本语句'):
	# 		login_page.open_login()
	# 		err = True
	# 		for i in range(5):
	# 			login_page.input_user_pwd(self.any_user,"xxx"*i)
	# 			try:
	# 				login_page.login_submit()
	# 			except:
	# 				# 出现拖动滑块限制
	# 				err = False
	# 				break
	# 	with allure.step('检查10此连续尝试是否被拦截'):
	# 		if err:
	# 			pytest.fail("未对暴力破解做限制")
	
	# ### 可用性测试			 			
	# @allure.story('可用性测试')
	# def test_login_by_enter(self,get_driver):
	# 	'''回车登录'''
	# 	print ("测试使用回车登录...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登录界面,正确的用户名密码'):
	# 		login_page.open_login()
	# 		login_page.input_user_pwd(self.user,self.correct_pwd)
	# 	with allure.step('输入回车，检查是否登录'):
	# 		login_page.driver.find_element_by_id("p").send_keys(Keys.ENTER)
	# 		time.sleep(3)
	# 		assert login_page.login_success()

	# @allure.story('可用性测试')
	# def test_tab_switch(self,get_driver):
	# 	'''输入框使用tab切换'''
	# 	print ("测试使用Tab切换输入框...")
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登录界面,输入用户名'):
	# 		login_page.open_login()
	# 		user = login_page.driver.find_element_by_id("u")
	# 		user.send_keys("test_tab")
	# 	with allure.step('输入Tab，检查是否切换到密码框'):
	# 		login_page.driver.find_element_by_id("u").send_keys(Keys.TAB)
	# 		pwd = login_page.driver.find_element_by_id('p')
	# 		# 检查密码框是否获得焦点
	# 		assert pwd == login_page.driver.switch_to.active_element

	# @allure.story('可用性测试')
	# def test_pwd_with_capslock(self,get_driver):
	# 	'''测试大写开启提示'''
	# 	print ("测试大写开启提示..."),
	# 	with allure.step('初始化浏览器driver'):
	# 		login_page = LoginPage(get_driver)
	# 	with allure.step('打开登陆界面,开启大写锁定输入密码'):
	# 		login_page.open_login()
	# 		login_page.driver.find_element_by_id("p").send_keys(Keys.CAPS)
	# 		login_page.driver.find_element_by_id("p").send_keys("test")
	# 		time.sleep(3)
	# 	with allure.step('判断存在大写锁定提示'):
	# 		assert "大写锁定" in login_page.get_source()
	

if __name__ == '__main__':
    pytest.main(['-s', '-q', 'test_Web.py','--alluredir', './result/'])
    os.system('allure generate ./result/ -o ./report/ --clean')
    os.system('allure open ./report')