import time
from selenium.webdriver import Keys
import pytest
from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators


class GroupsAndUsers(BasePage):

    def open_rm_groups_and_users(self):
        self.browser.find_element(*MainLocators.SIDE_BAR).click()
        # self.wait_until_elem_be_clickable(*RoleMiningLocators.ROLE_MINING)
        self.browser.find_element(*RoleMiningLocators.ROLE_MINING).click()
        self.browser.find_element(*RoleMiningLocators.GROPES_AND_USERS).click()

    def should_enter_rm_roups_and_users_be_successful(self):
        assert (self.is_element_present(By.XPATH, "//*[contains(text(),'Группы и пользователи Active Directory')]")), \
            "Найдено несовпадение ожидаемого результата с фактическим"
