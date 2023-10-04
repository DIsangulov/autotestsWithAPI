import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._5_RoleMining.rm_groups_and_users_page import RMGroupsAndUsersPage


class RMGroupsAndUsersCase(BaseCase):

    @allure.step("Открыть страницу 'Группы и пользователи Active Directory'")
    def open_page_by_steps(self):
        page = RMGroupsAndUsersPage(self._page)

        # todo: остальные шаги
        ...
