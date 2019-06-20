import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# link 'http://suninjuly.github.io/selects1.html'  'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects2.html')

answer = sum([int(browser.find_element_by_id(f'num{i + 1}').text) for i in range(2)])

select = Select(browser.find_element_by_id('dropdown'))
select.select_by_value(str(answer))

browser.find_element_by_css_selector('.btn.btn-default').click()
time.sleep(15)

browser.quit()
