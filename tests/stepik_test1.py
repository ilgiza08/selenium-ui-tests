from dotenv import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math


config = dotenv_values()
link_list = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()


class TestInStepik():
    @pytest.mark.parametrize('links', link_list)
    def test_user_solved_the_equation_correctly(self, browser, links):
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.implicitly_wait(7)
        browser.get(link)
        browser.find_element(By.XPATH, "//nav/a[text()='Войти']").click()
        browser.find_element(By.ID, 'id_login_email').send_keys(config['LOGIN'])
        browser.find_element(By.ID, 'id_login_password').send_keys(config['PASSWORD'])
        browser.find_element(By.CLASS_NAME, 'sign-form__btn,button_with-loader').click()
        browser.find_element(By.TAG_NAME, 'textarea').send_keys(math.log(int(time.time())))
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        correct_answer_text = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        assert correct_answer_text == "Correct!", correct_answer_text
        
        


