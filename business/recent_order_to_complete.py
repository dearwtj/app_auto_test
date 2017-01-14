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
        time.sleep(25)
    #     while driver.find_element_by_id("et_username").is_displayed():
    #         time.sleep(20)
        #输入用户性和密码，登录
        '''
        driver.find_element_by_id("et_username").send_keys("rcwtj")
        driver.find_element_by_id("et_password").send_keys("Abc123456")
        driver.find_element_by_id("btnLogin").click()
        '''
        Login(driver,'rcwtj','Abc123456')
        
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
    
        driver.find_element_by_name("继续投资").click()
        time.sleep(5)
        driver.find_element_by_name("电子合同").click()
        time.sleep(4)
        driver.find_element_by_id("completeConfirm").click()
        time.sleep(1)
        driver.find_element_by_id("completeConfirm").click()
        time.sleep(10)
        driver.find_element_by_id("cb_trade_contract").click()
        driver.find_element_by_id("imageView_elec_sign_thumb").click()
        
        action = TouchAction(driver)
#         签名：
        
#         action.press(x=36, y=134).move_to(x=1848, y=926).release().perform()
#         action.press(x=1884, y=1060).wait(100).move_to(x=36, y=134).release().perform() #绝对路径，花不上线
        action.press(x=36, y=134).move_to(x=1848, y=926).release().perform()  #可以时间签名，相对路径实现
       
       
       
#         driver.flick(936, 547, 984, 547)
        driver.find_element_by_id("btn_sure").click()
        time.sleep(1)
        driver.find_element_by_id("btn_sign").click()
        
        time.sleep(5)
        driver.find_elements_by_id("item_image")[0].click()
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


def readcontract(driver,m,n):
    while m < n:        
        driver.find_elements_by_name("点击查看")[0].click()
        time.sleep(3)
        pagenum = driver.find_element_by_id("tv_pagenum").text
        totalpagenum = int(pagenum.split('/')[1])
        while totalpagenum > 0:
            driver.swipe(1190, 1850, 1190, 1850, 10)
            time.sleep(1)
            totalpagenum = totalpagenum - 1
        driver.find_element_by_id("btn_finshread").click()
        m = m + 1
        


if __name__ == "__main__":
    begin()