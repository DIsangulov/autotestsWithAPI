import re
import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._5_RoleMining.rm_groups_and_users_page import RMGroupsAndUsersPage


class RMGroupsAndUsersCase(BaseCase):

    @allure.step("Открыть страницу 'Группы и пользователи Active Directory'")
    def open_page_by_steps(self):
        page = RMGroupsAndUsersPage(self._page)

        with allure.step("Перейти в 'Настройки уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Role mining'"):
            page.SB_ROLE_MINING.click()

        with allure.step("Клик в меню 'Группы и пользователи'"):
            page.SB_RM_GROUPS_AND_USERS.click()

        with allure.step("Открыта страница 'Группы и пользователи Active Directory'"):
            expect_reg = re.compile('^' + page.host + RMGroupsAndUsersPage.page_path + '(/.*)?$')
            expect(page.page).to_have_url(expect_reg)
