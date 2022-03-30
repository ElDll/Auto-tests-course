from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(a,b):
 return str(int (a) + int (b))

link = "http://suninjuly.github.io/selects2.html"

try:
 browser = webdriver.Chrome()
 browser.get(link)
 a_element = browser.find_element_by_id("num1")
 a = a_element.text
 b_element = browser.find_element_by_id("num2")
 b = b_element.text 
 x = calc(a,b)
 select = Select(browser.find_element_by_tag_name("select")) 
 select.select_by_value(x)
 button = browser.find_element_by_css_selector("[type='submit']")
 button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
