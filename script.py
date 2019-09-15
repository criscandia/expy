#!/usr/bin/env python
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select, WebDriverWait

URL = 'https://campaigns.automotoresonline.com/dietrich/1/'
FILENAME = 'vw.csv'
TIMEOUT = 15

data = pd.read_csv(FILENAME,
    encoding='UTF-16',
    index_col=False,
    #delim_whitespace=True,
    sep='\t',
    squeeze=True,
    usecols=['full_name', 'phone_number', 'email'],
    header=0,
    )

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get(URL)

for index, row in data.iterrows():
    wait = WebDriverWait(driver, TIMEOUT)
    # Get HTML elements
    name = driver.find_element_by_name('Nombre')
    phone = driver.find_element_by_name('Teléfono')
    email = driver.find_element_by_name('Email')
    car_model = driver.find_element_by_name('Modelo')
    button = driver.find_element_by_class_name('btn.form-btn.item-block')
    success = driver.find_element_by_xpath('//div[@id="submit-popup"]/div/div')
    # Fill form
    name.send_keys(row["full_name"])
    phone.send_keys(row["phone_number"])
    email.send_keys(row["email"])
    select = Select(car_model)
    select.select_by_value('Nuevo T-CROSS')
    # Submit form
    button.click()
    # Wait for the form to be ready again
    element = wait.until(ec.element_to_be_clickable((By.XPATH, '//div[@id="submit-popup"]/div/div')))
    element = wait.until(ec.element_to_be_clickable((By.XPATH, '//div[@id="submit-popup"]/div/div')))
    element = wait.until(ec.invisibility_of_element((By.XPATH, '//div[@id="submit-popup"]/div/div')))

driver.close()