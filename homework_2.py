# Задание на execute_script

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(math.fabs(12 * math.sin(x))))


link = "http://suninjuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)

    result = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(result)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    browser.execute_script("window.scrollBy(0, 100);")

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

finally:
    time.sleep(15)
    browser.quit()



# загрузка файлов

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Создаем пустой .txt файл
with open('file.txt', 'w') as f:
    pass  # Файл будет пустым


link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ya@ma.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

finally:
    time.sleep(15)
    browser.quit()


#работа с alert/confirm

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(math.fabs(12 * math.sin(x))))

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    btn2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn2.click()

finally:
    time.sleep(15)
    browser.quit()


#переход на новую вкладку

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(math.fabs(12 * math.sin(x))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn1.click()

    #переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    btn2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn2.click()

finally:
    time.sleep(15)
    browser.quit()



#работа с явными ожиданиями

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(math.fabs(12 * math.sin(x))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    btn = browser.find_element(By.ID, "book")
    btn.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    btn2 = browser.find_element(By.ID, "solve")
    btn2.click()

finally:
    time.sleep(10)
    browser.quit()
