link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time

def test_add_button(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector("[type = 'submit']"), 'basket button not found'
