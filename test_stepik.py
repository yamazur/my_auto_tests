import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

LESSON_LINKS = ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"

]

class TestStepikAuth:

    #ЛОКАТОРЫ

    #перейти к авторизации
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".navbar__auth_login")

    #кнопки на странице авторизации
    LOGIN_INPUT = (By.ID, "id_login_email")
    PASSWORD_INPUT = (By.ID, "id_login_password")
    SUBMIT_BUTTON_1 = (By.CSS_SELECTOR, ".sign-form__btn")

    #элементы после авторизации
    USER_AVATAR = (By.CSS_SELECTOR, ".navbar__profile-img")
    ANSWER_INPUT = (By.CSS_SELECTOR, ".ember-text-area.textarea")
    SUBMIT_BUTTON_2 = (By.CSS_SELECTOR, ".submit-submission")
    CORRECT_TEXT = (By.CSS_SELECTOR, ".smart-hints__hint")

    @pytest.mark.parametrize('link',LESSON_LINKS)
    def test_authorization_on_stepik(self, browser, wait, load_passwords, link):  # Используем фикстуру load_passwords

        lesson_id = link.split('/')[-3]
        print(f"НАЧАЛО ТЕСТА: Урок {lesson_id}")

        try:
            # 1. Открываем страницу
            browser.get(link)
            print(f"Открыта страница {link}")

            #2. Получаем логин и пароль из фикстуры
            # load_passwords - это словарь с данными
            login = load_passwords['login_stepik']
            password = load_passwords['password_stepik']

            print(f"Используется логин: {login}")
            print(f"Длина пароля: {len(password)} символов")

            # 3. Кликаем кнопку "Войти" в навбаре
            # Используем * для распаковки кортежа
            # Ждем, пока кнопка станет кликабельной
            login_button = wait.until(
                EC.element_to_be_clickable(self.LOGIN_BUTTON)
            )
            login_button.click()
            print("Кликнута кнопка 'Войти' в шапке")

            # 4. Ждем форму
            wait.until(EC.visibility_of_element_located(self.LOGIN_INPUT))

            # 5. Заполняем форму
            login_field = browser.find_element(*self.LOGIN_INPUT)
            login_field.send_keys(login)
            print(f"Введен логин")

            password_field = browser.find_element(*self.PASSWORD_INPUT)
            password_field.send_keys(password)
            print("Введен пароль")

            # 6. нажимаем на кнопку "Войти"
            submit_button_1 = browser.find_element(*self.SUBMIT_BUTTON_1)
            submit_button_1.click()
            print("Нажата кнопка 'Войти' в форме")

            # 7. Ждем успешной авторизации
            # Ждем элемент, подтверждающий авторизацию
            wait.until(
                EC.visibility_of_element_located(self.USER_AVATAR),
                message = "Аватар пользователя не появился!"
            )

            print("✓ Авторизация прошла успешно!")

            # 8. Проверяем, остались ли мы на той же странице
            assert link in browser.current_url, \
                f"После авторизации ушли со страницы урока. Текущий URL: {browser.current_url}"
            print(f"Остались на странице урока: {browser.current_url}")

            # 9. Решаем задание и вставляем ответ на задание в поле ответа
            #ждем пока поле для ответа станет доступным
            answer_input = wait.until(
                EC.presence_of_element_located(self.ANSWER_INPUT),
                message="Поле для ответа не найдено"
            )

            #решаем задачу и вставляем ответ
            answer = math.log(int(time.time()))
            answer_input.clear()
            answer_input.send_keys(answer)
            print("Дали ответ на задание")

            # 10. Нажимаем на кнопку "Отправить"
            submit_button_2 = browser.find_element(*self.SUBMIT_BUTTON_2)
            submit_button_2.click()
            print("Нажата кнопка 'Отправить'")

            # 11. Проверяем, что текст в опциональном фидбеке полностью совпадает с "Correct!"
            correct_text = browser.find_element(*self.CORRECT_TEXT)
            actual_text = correct_text.text.strip()  # "Correct!"
            assert actual_text == "Correct!", \
                f"Ожидалось 'Correct!', получено '{actual_text}'"

            print("✓ Ответ верный!")
            print(f"\n ТЕСТ ПРОЙДЕН УСПЕШНО для урока {lesson_id}")

        except Exception as e:

            # 1. Извлекаем номер урока из URL
            # link = "https://stepik.org/lesson/236895/step/1"
            # link.split('/') = ['https:', '', 'stepik.org', 'lesson', '236895', 'step', '1']
            # link.split('/')[-3] = '236895' (третий с конца)
            lesson_id = link.split('/')[-3]

            # 2. Печатаем информацию об ошибке
            print(f"\n✗ ОШИБКА на уроке {lesson_id}:")
            print(f"   Тип ошибки: {type(e).__name__}")
            print(f"   Сообщение: {str(e)}")
            print(f"   URL: {link}")
            raise