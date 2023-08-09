import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._2_Data.scripts_page import ScriptsPage

UI_AUTO_TEST_ = "UI_AUTO_TEST_"


class DataScriptsCase(BaseCase):

    @allure.step("Открыть страницу 'Скрипты'")
    def open_page_by_steps(self):
        page = ScriptsPage(self._page)

        with allure.step("Перейти в 'Профиль пользователя'"):
            page.goto_page("/personal")
            page.page.wait_for_url(page.host + "/personal")

        with allure.step("Клик в боковом меню 'Данные'"):
            page.SB_DATA.click()

        with allure.step("Клик в меню 'Скрипты'"):
            page.SB_DATA_SCRIPTS.click()

        with allure.step("Переход на страницу 'Скрипты'"):
            page.page.wait_for_url(page.host + ScriptsPage.page_path)
