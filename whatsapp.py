# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 11:15:54 2019

@author: Abhishek Parashar
"""

from selenium import webdriver

driver= webdriver.Chrome("C://Users//Abhishek_Parashar//Downloads//chromedriver_win32//chromedriver.exe')
driver.get('https://web.whatsapp.com/')
name= input('enter the name of user group')
msg=input('enter your message')
count=int(input('enter the count'))
input('enter anything after scanning qr code')
user=driver.find_element_by_xpath('\\span[@title="{}"]'.format(name))
user.click()
msg_box=driver.find_element_by_class_name('input_container')
for i in range(count):
    msg_box.send_keys(msg)
    button=driver.find_element_by_class_name('compose-btn-send')
    button.click()