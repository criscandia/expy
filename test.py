# -*- coding: utf-8 -*-
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import Select



binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox()
driver.get('https://campaigns.automotoresonline.com/dietrich/1/')



data = pd.read_csv('/home/candiman/Projects/Expy/vw.csv',
                    encoding= 'UTF-16',
                    #delim_whitespace=True,
                    sep = '\t',
                    squeeze = True,
                    usecols = ['full_name', 'phone_number', 'email'],
                    header= 0)
                     #Youll want to change the .xlsx to .csv
depth = len(data['full_name'])

try:
    element = driver.find_element_by_xpath("//div[@class='form-block-select']")
    element.click()
    select = Select(driver.find_element_by_id('field-2b40cec773350be845715b976924fc96-3'))
    element = select.select_by_visible_text("Nuevo T-CROSS")
    element.click()
except:
    pass

for i in range (0,2):
    driver.find_element_by_xpath("//input[@id='field-2b40cec773350be845715b976924fc96-0']").send_keys(data['full_name'][i])
    driver.find_element_by_xpath("//input[@id='field-2b40cec773350be845715b976924fc96-1']").send_keys(data['phone_number'][i])
    driver.find_element_by_xpath("//input[@id='field-2b40cec773350be845715b976924fc96-2']").send_keys(data['email'][i])

