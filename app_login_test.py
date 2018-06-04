#coding:utf8
'''
Created on 2017年1月5日

@author: CANDAO
'''
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
try:
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'M7TCMBQKQ8JFBMSW'
    desired_caps['appPackage'] = 'com.ms.ui.activity'
    desired_caps['appActivity'] = '.Welcome'
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
#     desired_caps = {
#         'platformName':'Android',
#         'platformVersion':'4.4.2',
#         'deviceName':'127.0.0.1:21503',
#         'appPackage':'com.ms.ui.activity',
#         'appActivity':'.Welcome'
#         }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(20)
#     while driver.find_element_by_id("et_username").is_displayed():
#         time.sleep(20)
    #输入用户性和密码，登录
    driver.find_element_by_id("et_username").send_keys("rcwtj")
    driver.find_element_by_id("et_password").send_keys("Abc123456")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(5)
    #进入投资人选择页
    driver.find_element_by_id("rd_tab_customer").click()
    time.sleep(2)
    #选择号码为：156****2703的投资人
    name = driver.find_element_by_name("555****5556")
    name.click()
#     driver.findElement(By.ClassName("android.widget.RelativeLayout")).click()
    time.sleep(8)
    #投资人主页，点击“去推荐”
#     driver.tap([(500,500)], 10)
#     driver.find_element_by_id("titlebar").click()
#     x = driver.get_window_size()['width']
#     y = driver.get_window_size()['height']
#     x = 100
#     y = 100
#     driver.swipe(x,y,x,y,1)
    
    time.sleep(10)
    driver.find_element_by_id("btn_order").click()
    time.sleep(2)
    #选择产品类型
    driver.find_element_by_name("会员精选")
    time.sleep(2)
    #选择产品
    driver.find_element_by_name("订单归属无合同").click()
    time.sleep(3)
    #点击立即投资
    driver.find_element_by_id("btn_sales").click()
    time.sleep(2)
    #选择投资金额框
#    driver.find_element_by_id("et_will_subscribe").click()
    #输入投资金额25
#     driver.find_element_by_id("num_2").click()   #需处理
#     driver.find_element_by_id("num_2").click()
#     driver.find_element_by_id("num_5").click()
#     driver.find_element_by_id("btn_complete").click()
    #点击立即投资  
    driver.find_element_by_id("btn_inveast").click()
    time.sleep(5)
    #点击立即投资，进入投资流程
    driver.find_element_by_id("btn_invest").click()
    time.sleep(5)
# 待研究
    '''
    action = TouchAction(driver)
    action.press(275,1019)
    '''
    
    
#     滑动屏幕，从而输入银行卡信息
    driver.swipe(829, 1070, 700, 450, 500)
    
    #输入银行卡号
    driver.find_element_by_id("et_pay_card").click()
    driver.find_element_by_id("num_2").click()
    driver.find_element_by_id("num_2").click()    
    driver.find_element_by_id("num_2").click()
    driver.find_element_by_id("btn_complete").click()
    
    
    
    driver.find_element_by_id("tv_pay_bank").click()
    driver.find_element_by_name("交通银行").click()
    driver.find_element_by_id("tv_pay_bank_area_1").click()
    # 输入开户支行
    driver.find_element_by_name("北京市").click()
    driver.find_element_by_id("et_open_pay_bank").send_keys(u"成都市总府路支行")
    #点击 “保存并下一步”
    driver.find_element_by_id("btn_transaction").click()
    
    time.sleep(2)
    #点击拍照
    driver.find_element_by_id("item_img1").click()
    driver.find_element_by_id("btn_camera").click()
#     driver.wait_activity('android.widget.Button',5,1)
    time.sleep(5)
    
    driver.find_element_by_id("btn_save").click()
    
    driver.find_element_by_id("btn_transaction").click()
    
    time.sleep(5)
    driver.find_element_by_id("item_image").click()
    driver.find_element_by_id("itemImage").click()
    driver.find_element_by_id("btn_camera").click()
#     driver.wait_activity('android.widget.Button',5,1)
    time.sleep(5)
    driver.find_element_by_id("btn_save").click()
    driver.find_element_by_id("btn_trade").click()
    
    
    print "执行成功"
    
    
    
    
    
    
    
    
    
    time.sleep(2)
    
    
    
    
    driver.quit()
except Exception as e:
    print e

