from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    input1.send_keys("Lapshin")
    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    input1.send_keys("IvanLapshin@mail.ru")
    current_dir = os.path.abspath(os.path.dirname('lesson2_step8.py'))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    input2 = browser.find_element_by_css_selector("[type='file']")
    input2.send_keys(file_path)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()