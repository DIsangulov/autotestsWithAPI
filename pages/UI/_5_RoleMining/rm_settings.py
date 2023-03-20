import time
from selenium.webdriver import Keys
import pytest
from selenium.webdriver.common.by import By
from seleniumwire import webdriver

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators


class Settings(BasePage):
    def open_rm_settings(self):
        self.browser.find_element(*MainLocators.SIDE_BAR).click()
        self.wait_until_elem_be_clickable(*RoleMiningLocators.ROLE_MINING)
        self.browser.find_element(*RoleMiningLocators.ROLE_MINING).click()
        self.browser.find_element(*RoleMiningLocators.SETTINGS).click()

    def should_enter_rm_settings_be_successful(self):
        assert (self.browser.find_element(By.XPATH, "//*[contains(text(),'Настройки Role mining')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"
