from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.user_dropdown_xpath = Locators.user_dropdown_xpath
        self.logout_link_linkText = Locators.logout_link_linkText

    def click_dropdown(self):
        self.driver.find_element(By.XPATH,self.user_dropdown_xpath).click()

    def logout(self):
        logout_link = WebDriverWait(self.driver, 300).until(
            EC.presence_of_element_located((By.LINK_TEXT, self.logout_link_linkText))
        )
        logout_link.click()
