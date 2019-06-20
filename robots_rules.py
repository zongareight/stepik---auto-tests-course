import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/math.html')

x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

inp = driver.find_element_by_id('answer')
inp.send_keys(y)

robot_check = driver.find_element_by_id('robotCheckbox')
robot_check.click()

robot_rul = driver.find_element_by_id('robotsRule')
robot_rul.click()

submit_button = driver.find_element_by_css_selector('.btn.btn-default')
submit_button.click()
time.sleep(15)

driver.quit()
