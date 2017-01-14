#coding:utf8
'''
Created on 2017��1��12��

@author: CANDAO
'''

from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from public_method.common_load_driver import Driver
from public_method.common_login import Login
def begin():
    
    try:
        '''
        desired_caps = {
            'platformName':'Android',
            'platformVersion':'4.4.2',
            'deviceName':'52030f30fa285305',
            'appPackage':'com.ms.ui.activity',
            'appActivity':'.Welcome',
            'unicodeKeyboard':True,
            'resetKeyboard':True
            }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        '''
        D = Driver()
        driver = D.get_driver("4.4.2", "52030f30fa285305")
        time.sleep(10)
    #     while driver.find_element_by_id("et_username").is_displayed():
    #         time.sleep(20)
        #输入用户性和密码，登录
        '''
        driver.find_element_by_id("et_username").send_keys("rcwtj")
        driver.find_element_by_id("et_password").send_keys("Abc123456")
        driver.find_element_by_id("btnLogin").click()
        '''
        Login(driver,'rcwtj','Abc123456')
        time.sleep(3)
        #点击“访”，切换到理财师模式
        driver.find_element_by_id("iv_laoban_icon").click()
#         driver.find_element_by_id("btn_save").click()  #点击确认提示框的“确认”
        
        action = TouchAction(driver)
        '''        
        action.press(x=518, y=513).move_to(x=445,y=0).move_to(x=442,y=0).release().perform()
        为什么release是以 move_to(x = -700,y =-900),的坐标释放
         action.press(x=518, y=513).move_to(x=445,y=0).move_to(x=442,y=0).move_to(x=-442,y=187).move_to(x=-442,y=188).move_to(x=442,y=0).move_to(x=442,y=0).move_to(x=-884,y=-188).wait(100).move_to(x=259,y=350).release().perform()
        '''
        action.press(x=518, y=513).release().perform()
#         action.press(x=518, y=513).wait(100).move_to(x=960,y=513).wait(100).move_to(x=1402,y=513).release().perform()
        
        
        
        time.sleep(3)
        
        
        
    except Exception as e:
        print e
        
if __name__ == "__main__":
    begin()