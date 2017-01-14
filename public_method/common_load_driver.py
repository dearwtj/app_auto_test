#coding:utf8
'''
Created on 2017��1��14��

@author: CANDAO
'''
from appium import webdriver


class Driver:
    '''
    传入
    设备android版本号，如：4.4.2
    设备名称，如：52030f30fa285305
    '''
    def get_driver(self,platformVersion,deviceName):
        mydict = {}
        mydict["platformName"] = "Android"
        mydict["platformVersion"] = platformVersion
        mydict["deviceName"] = deviceName
        mydict["appPackage"] = "com.ms.ui.activity"
        mydict["appActivity"] = ".Welcome"
        mydict["unicodeKeyboard"] = True
        mydict["resetKeyboard"] = True
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', mydict)
        return driver