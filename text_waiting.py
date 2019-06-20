import pyperclip
from calc import calc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 15 секунд, пока не появится нужный текст
WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR')
    )

button = browser.find_element_by_id('book').click()

y = calc(browser.find_element_by_id('input_value').text)

browser.find_element_by_id('answer').send_keys(y)

browser.find_element_by_id('solve').click()

# сохранение ответа в буфер
pyperclip.copy(browser.switch_to.alert.text.split(': ')[-1])

browser.quit()
