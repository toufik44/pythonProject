'''
Created on 8 déc. 2019

@author: toufik
'''
from selenium import webdriver


driver = webdriver.Firefox(executable_path='/home/toufik/.local/lib/python3.6/site-packages/geckodriver')
driver.get('http://inventwithpython.com')