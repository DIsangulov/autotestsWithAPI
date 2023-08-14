import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._1_Administration.adm_users_page import UsersPage


class UsersCase(BaseCase):

    @allure.step("Открыть страницу Пользователи")
    def open_page_by_steps(self):
        page = UsersPage(self._page)

        # шаг нужен, чтобы боковое меню было закрыто
        with allure.step("Перейти в 'Настройка уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Администрирование'"):
            page.SB_ADMINISTRATION.click()

        with allure.step("Клик в меню 'Пользователи'"):
            page.SB_ADM_USERS.click()

        with allure.step("Открылась страница 'Пользователи'"):
            page.page.wait_for_url(page.host + UsersPage.page_path)
