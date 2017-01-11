#coding:utf8
'''
Created on 2017年1月5日

@author: WTJ
'''
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction







def begin():
    
    try:
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
        #搜索产品：永赢①期20170106
        driver.find_element_by_id("et_search").send_keys(u'永赢①期20170106')
        driver.find_element_by_id("btn_search").click()
        
        #选择产品
        driver.find_element_by_id("rl_intent_product_search_adapter").click()
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
        #输入验证码：999999
        driver.find_element_by_id("et_verify_code").click()
        i = 0
        while i < 6:
            driver.find_element_by_id("num_2").click()
        driver.find_element_by_id("btn_complete").click()
        
        
    #   滑动屏幕，从而输入银行卡信息
        driver.swipe(829, 1070, 700, 450, 500)
        
        #输入银行卡号：666666
        driver.find_element_by_id("et_pay_card").click()
        while i < 6:
            driver.find_element_by_id("num_6").click()
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
        
        #勾选合同前置阅读内容
        driver.find_element_by_class_name("android.widget.CheckBox").click()
    #    滑动屏幕，方便勾选第二个前置阅读内容
        driver.flick(1000, 960, 1000, 700)
    #    勾选合同前置阅读内容
        driver.find_element_by_class_name("android.widget.CheckBox").click()
        
        #完成合同编号确认，点击“完成确认”
        driver.find_element_by_id("completeConfirm").click()
        time.sleep(20)
        '''
        合同阅读部分
        分别点击查看合同信息
        完成签字
        勾选确认
        '''
    #     i = 0
    #     while i < 3:
    #         
    #         driver.find_elements_by_name("点击查看")[i].click()
    #         time.sleep(3)
    #         pagenum = driver.find_element_by_id("tv_pagenum").text
    #         totalpagenum = int(pagenum.split('/')[1])
    #         while totalpagenum > 0:
    #             driver.swipe(1190, 1850, 1190, 1850, 10)
    #             time.sleep(1)
    #             totalpagenum = totalpagenum - 1
    #         driver.find_element_by_id("btn_finshread").click()
        readcontract(driver,0, 3)
        
        driver.flick(1500, 646, 1500, 370)
        
        readcontract(driver,2, 4)
#         接受服务声明
        driver.find_element_by_id("cb_trade_contract").click()
        
#        签名 
        driver.find_element_by_id("imageView_elec_sign_thumb").click()
        driver.flick(936, 547, 984, 547)
        driver.find_element_by_id("btn_sure").click()
        time.sleep(1)
        driver.find_element_by_id("btn_sign").click()
             
        
        
        
        
        
        time.sleep(5)
        driver.find_element_by_name("转账付款").click()
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
        driver.find_elements_by_name("点击查看")[m].click()
        time.sleep(3)
        pagenum = driver.find_element_by_id("tv_pagenum").text
        totalpagenum = int(pagenum.split('/')[1])
        while totalpagenum > 0:
            driver.swipe(1190, 1850, 1190, 1850, 10)
            time.sleep(1)
            totalpagenum = totalpagenum - 1
        driver.find_element_by_id("btn_finshread").click()


if __name__ == "__main__":
    begin()


    