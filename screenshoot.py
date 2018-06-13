#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:10:36 2018

@author: little-frog
"""

import time
from PIL import Image
from selenium import webdriver

url = 'http://www.baidu.com'
path = 'geckodriver'
browser = webdriver.Firefox(executable_path=path)###切记一定要用火狐浏览器！！！谷歌不能这么搞
browser.get(url)

###获取截图
img = browser.find_element_by_css_selector('#form input.bg.s_btn')
print(img.get_attribute('value'))###看一下节点是不是我们要的
img.screenshot('result.png')###截图
###读取并展示
result = Image.open('result.png')
result.show()
time.sleep(5)
browser.close()
