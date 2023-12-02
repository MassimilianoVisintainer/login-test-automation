from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

from Locators.locators import Locators
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
import HtmlTestRunner


class LoginTet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_not_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('wrongPassword')
        login.click_login()
        actual_text = WebDriverWait(self.driver, 100).until(
            EC.presence_of_element_located((By.XPATH, Locators.alert_message_xpath))
        ).text
        self.assertIn('Invalid credentials', actual_text)

    def test_login_valid(self):
        login = LoginPage(self.driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        self.assertEqual(self.driver.current_url, expected_url)

        homePage = HomePage(self.driver)
        homePage.click_dropdown()
        homePage.logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/Utente/Desktop/MAX/automation testing/Selenium/loginProject/Reports'))
