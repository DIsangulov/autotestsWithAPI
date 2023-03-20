import time
from selenium.webdriver import Keys
import pytest

from pages.Helpers.base_page import BasePage
from resourses.locators import AuthLocators, MainLocators, RoleMiningLocators


class AuthPage(BasePage):

    def enter_as_user(self):
        # self.wait_until_elem_be_clickable(*MainLocators.PRE_ENTER)
        # self.browser.find_element(*MainLocators.PRE_ENTER).click()
        # self.wait_until_elem_be_clickable(*MainLocators.PRE_ENTER_AGREE)
        # self.browser.find_element(*MainLocators.PRE_ENTER_AGREE).click()
        self.wait_until_elem_be_clickable(*AuthLocators.LOGIN_INPUT)
        self.browser.find_element(*AuthLocators.LOGIN_INPUT).send_keys("dataplan_qaa@ngrsoftlab.ru")
        self.browser.find_element(*AuthLocators.PAS_INPUT).send_keys("fHNHQBc7jEKfaO0kywZz!!")
        self.browser.find_element(*AuthLocators.PASS_VISIBLE).click()
        self.browser.find_element(*AuthLocators.ENTER_BUT).click()

    def should_enter_be_successful(self):
        # self.wait_until_elem_be_clickable(*MainLocators.SUCCESS_ENTER)
        assert self.is_element_present(*MainLocators.SUCCESS_ENTER), "Unsuccessful enter"
