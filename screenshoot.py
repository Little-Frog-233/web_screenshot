#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:10:36 2018

@author: ruicheng
"""

import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://www.baidu.com'
path = '/Users/ruicheng/chromedriver01/geckodriver'
browser = webdriver.Firefox(executable_path=path)###切记一定要用火狐浏览器！！！谷歌不能这么搞

wait = WebDriverWait(browser,20)
browser.get(url)

###获取截图
img = browser.find_element_by_css_selector('#form input.bg.s_btn')
print(img.get_attribute('value'))###看一下节点是不是我们要的
img.screenshot('/Users/ruicheng/Documents/上海师范研究生/python相关/爬虫/屏幕截图/result.png')###截图
###读取并展示
result = Image.open('/Users/ruicheng/Documents/上海师范研究生/python相关/爬虫/屏幕截图/result.png')
result.show()
time.sleep(5)
browser.close()