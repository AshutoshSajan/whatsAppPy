#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# above line is added for imoji support 

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# geckodriver direct executable_path
driver = webdriver.Firefox(executable_path=r"/home/ashu/Downloads/geckodriver-v0.26.0-linux64/geckodriver");

# or add executable in /usr/local/bin
# driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver");
# driver = webdriver.Firefox();

# or using chromedriver executable_path
# driver = webdriver.Chrome('/home/ashu/Downloads/chromedriver_linux64/chromedriver')

# or add the chromedriver executable to /usr/local/bin
# driver = webdriver.Chrome()


  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = '"Anjli Sis"'

# Replace the below string with your own message 
msg_string = "😃😃"

x_arg = '//span[contains(@title,' + target + ')]'

group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 

group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'

input_box = wait.until(EC.presence_of_element_located(( 
    By.XPATH, inp_xpath)))

    
for i in range(100): 
    input_box.send_keys(msg_string + Keys.ENTER) 
    time.sleep(1)
