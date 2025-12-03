import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

link = "https://stepik.org/lesson/236895/step/1"

try:

    class TestStepik:
        def test_open_browser(self, browser):
            browser.get(link)

        def test_authorization(self, browser, wait, load_passwords):  # Используем фикстуру load_passwords
            # Фикстура load_passwords уже возвращает словарь, не нужно вызывать как функцию
            login = load_passwords['login_stepik']  # Просто обращаемся к словарю
            password = load_passwords['password_stepik']











# link = "http://selenium1py.pythonanywhere.com/"
#
# class TestMainPage1:
#
#     @pytest.mark.parametrize('language', ["ru", "en-gb"])
#     def test_guest_should_see_login_link(self, browser, language):
#         link = f"http://selenium1py.pythonanywhere.com/{language}/"
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
#
#     @pytest.mark.xfail(reason="fixing this bug right now")
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
#


