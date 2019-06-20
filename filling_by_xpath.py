import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
button = browser.find_element_by_xpath('//button[text()="Отправить"]')
button.click()
time.sleep(15)
browser.quit()
