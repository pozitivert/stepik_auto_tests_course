from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()


finally:
    time.sleep(15)
    browser.quit()