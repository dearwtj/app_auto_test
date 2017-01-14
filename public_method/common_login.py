#coding:utf8
'''
Created on 2017��1��14��

@author: CANDAO
'''

'''
传入
用户名和密码
登录
'''

class Login:
    def __init__(self,driver,account,password):
        driver.find_element_by_id("et_username").send_keys(account)
        driver.find_element_by_id("et_password").send_keys(password)
        driver.find_element_by_id("btnLogin").click()
