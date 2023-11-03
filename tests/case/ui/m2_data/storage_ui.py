import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._2_Data.storage_page import *


@allure.step("Открыть страницу 'Хранилище'")
def open_page_by_steps(browser: Page):
    page = StoragePage(browser)

    with allure.step("Перейти в 'Профиль пользователя'"):
        page.goto_page("/personal")
        browser.wait_for_url(page.host + "/personal")

    with allure.step("Клик в боковом меню 'Данные'"):
        page.SB_DATA.click()

    with allure.step("Клик в меню 'Хранилище'"):
        page.SB_DATA_STORAGE.click()

    with allure.step("Открылась страница 'Хранилище'"):
        browser.wait_for_url(page.host + StorageStructurePage.page_path)


def storage_navigation_tabs(browser: Page):
    page = StoragePage(browser)

    with allure.step("Открыть страницу 'Хранилища' (tab Струкрура)"):
        page.open()

    with allure.step("Клик по вкладке 'Статистика'"):
        page.TAB_STATISTICS.click()
    with allure.step("Открылась страница 'Хранилище > Статистика'"):
        browser.wait_for_url(page.host + StorageStatisticPage.page_path)

    with allure.step("Клик по вкладке 'Поиск в хранилище'"):
        page.TAB_SEARCH.click()
    with allure.step("Открылась страница 'Хранилище > Поиск в хранилище(по содержимому)'"):
        browser.wait_for_url(page.host + StorageSearchContentPage.page_path)
    with allure.step("Клик по вкладке 'Поиск в хранилище > По столбцам'"):
        page.TAB_SEARCH_COLUMN.click()
    with allure.step("Открылась страница 'Хранилище > Поиск в хранилище(по столбцам)'"):
        browser.wait_for_url(page.host + StorageSearchColumnPage.page_path)

    with allure.step("Клик по кладке 'Поиск в хранилище > По содержимому'"):
        page.TAB_SEARCH_CONTENT.click()
    with allure.step("Открылась страница 'Хранилище > Поиск в хранилище(по содержимому)'"):
        browser.wait_for_url(page.host + StorageSearchContentPage.page_path)

    with allure.step("Клик по кладке 'Хранилище > Правила импорта'"):
        page.TAB_RULES.click()
    with allure.step("Открылась страница 'Хранилище > Правила импорта'"):
        browser.wait_for_url(page.host + StorageRulesPage.page_path)

    with allure.step("Клик по вкладке 'Хранилище > Структура'"):
        page.TAB_STRUCTURE.click()
    with allure.step("Открылась страница 'Хранилище > Структура'"):
        browser.wait_for_url(page.host + StorageStructurePage.page_path)
