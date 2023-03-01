import time
from selenium.webdriver import Keys
import pytest
from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators


class RoleMining(BasePage):
    def open_rm_settings(self):
        self.wait_until_elem_be_clickable(*MainLocators.SIDE_BAR)
        self.browser.find_element(*MainLocators.SIDE_BAR).click()
        self.wait_until_elem_be_clickable(*RoleMiningLocators.ROLE_MINING)
        self.browser.find_element(*RoleMiningLocators.ROLE_MINING).click()
        self.wait_until_elem_be_clickable(*RoleMiningLocators.SETTINGS)
        self.browser.find_element(*RoleMiningLocators.SETTINGS).click()
        assert (self.is_element_present(By.XPATH, "//*[contains(text(),'Настройки Role mining')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"
