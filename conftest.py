import json
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10) #неявное ожидание, на поиск элемента максимум 10 секунд
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="session")
def load_passwords():
    with open('passwords.json', 'r') as passwords_file:   # Открываем файл с конфигом в режиме чтения
        passwords = json.load(passwords_file)  # С помощью библиотеки json читаем и возвращаем результат
        return passwords

@pytest.fixture
def wait(browser):
    from selenium.webdriver.support.ui import WebDriverWait
    return WebDriverWait(browser, timeout=20)  # явное ожидание! Ждать максимум 20 секунд

