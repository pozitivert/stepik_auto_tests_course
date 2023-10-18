from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

# Инициализация драйвера
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # Дождитесь, пока цена дома уменьшится до $100 (ожидание не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажмите на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решите математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    answer = math.log(abs(12 * math.sin(x)))

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(str(answer))

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Получите результат
    alert = browser.switch_to.alert
    result = alert.text
    print(f"Результат: {result}")

finally:
    # Закройте браузер
    browser.quit()
