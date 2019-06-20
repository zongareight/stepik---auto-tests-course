import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


driver = webdriver.Chrome()

driver.get('http://suninjuly.github.io/get_attribute.html')

y = calc(driver.find_element_by_id('treasure').get_attribute('valuex'))

inp = driver.find_element_by_id('answer').send_keys(y)

robot_check = driver.find_element_by_id('robotCheckbox').click()

robot_rul = driver.find_element_by_id('robotsRule').click()

submit_button = driver.find_element_by_css_selector('.btn.btn-default').click()
time.sleep(15)

driver.quit()
