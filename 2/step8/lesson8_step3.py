import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')    # добавляем к этому пути имя файла
# # element.send_keys(file_path)

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Lox")
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys("Net")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("XZ")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')    # добавляем к этому пути имя файла
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button3 = browser.find_element(By.TAG_NAME, "button")
    button3.click()
finally:
    time.sleep(10)
    browser.quit()