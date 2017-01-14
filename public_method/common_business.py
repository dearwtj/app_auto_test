#coding:utf8
'''
Created on 2017��1��13��

@author: CANDAO
'''
import time

class General:
    
    '''
    输入框
    点击弹出数字输入框
    传入driver，和字符串格式的数字，如：‘123456’
    '''
    def pop_frame_to_input_num(self,driver,str):
        i = 0
        while i < len(str):
            num_str = 'num_' + str[i]
            driver.find_element_by_id(num_str).click()
            i = i+1
        driver.find_element_by_id("btn_complete").click()
    
    '''
    阅读合同
    传入driver
    n：传入当前页可以操作的“点击查看数”
    注意：如果有向上滑动才可以查看，这种每次只能查看一个，因为阅读完后会自动回到进入合同模板阅读的格式，
    这个时候需要通过swipe来控制，才能继续阅读
    '''      
    def readcontract(self,driver,n):
        m=0
        while m < n:        
            driver.find_elements_by_name("点击查看")[0].click()
            time.sleep(5)
            pagenum = driver.find_element_by_id("tv_pagenum").text
            totalpagenum = int(pagenum.split('/')[1])
            while totalpagenum > 0:
                driver.swipe(1190, 1850, 1190, 1850, 10)
                time.sleep(1)
                totalpagenum = totalpagenum - 1
            driver.find_element_by_id("btn_finshread").click()
            m = m + 1

        