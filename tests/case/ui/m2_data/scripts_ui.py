import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._2_Data.scripts_page import ScriptsPage

UI_AUTO_TEST_ = "UI_AUTO_TEST_"


@allure.step("Открыть страницу 'Скрипты'")
def open_page_by_steps(browser: Page):
    page = ScriptsPage(browser)

    with allure.step("Перейти в 'Профиль пользователя'"):
        page.goto_page("/personal")
        browser.wait_for_url(page.host + "/personal")

    with allure.step("Клик в боковом меню 'Данные'"):
        page.SB_DATA.click()

    with allure.step("Клик в меню 'Скрипты'"):
        page.SB_DATA_SCRIPTS.click()

    with allure.step("Переход на страницу 'Скрипты'"):
        browser.wait_for_url(page.host + ScriptsPage.page_path)
