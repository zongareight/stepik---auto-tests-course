import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get('http://SunInJuly.github.io/execute_script.html')

y = calc(browser.find_element_by_id('input_value').text)

inp = browser.find_element_by_id('answer')
inp.send_keys(y)

browser.execute_script('window.scrollBy(0, 125);')

robot_check = browser.find_element_by_id('robotCheckbox')
# browser.execute_script('return arguments[0].scrollIntoView(true)', robot_check)
robot_check.click()

robot_rul = browser.find_element_by_id('robotsRule')
# browser.execute_script('return arguments[0].scrollIntoView(true)', robot_rul)
robot_rul.click()

submit_button = browser.find_element_by_css_selector('.btn.btn-default')
# browser.execute_script('return arguments[0].scrollIntoView(true)', submit_button)
submit_button.click()
time.sleep(25)

browser.quit()
