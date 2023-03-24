from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import MainLocators, XbaLocators


class Profiles(BasePage):
    def open_xba_profiles(self):
        self.browser.find_element(*MainLocators.SIDE_BAR).click()
        self.wait_until_elem_be_clickable(*XbaLocators.XBA)
        self.browser.find_element(*XbaLocators.XBA).click()
        self.browser.find_element(*XbaLocators.PROFILES).click()

    def should_enter_xba_profiles_be_successful(self):
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'Профили хВА')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"
