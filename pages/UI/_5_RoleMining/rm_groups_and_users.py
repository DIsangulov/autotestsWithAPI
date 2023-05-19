import time
from selenium.webdriver import Keys
import pytest
from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators, AdminLocators


class GroupsAndUsers(BasePage):

    def open_rm_groups_and_users(self):
        self.page.click(RoleMiningLocators.GROPES_AND_USERS)

    def should_enter_rm_roups_and_users_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Группы и пользователи Active Directory" in self.is_element_present(
            AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/role-mining/groups-and-users/groups", "URL's do not match"
