# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value").text
    y = calc(x_element)

    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(y)

    button1 = browser.find_element(By.ID, "robotCheckbox")
    button1.click()
    button2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()

    button3 = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
    button3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()