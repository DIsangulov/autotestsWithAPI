import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._3_Analytics.visualization_page import VisualisationPage


@allure.step("Открыть страницу 'Визуализации'")
def open_page_by_steps(browser: Page):
    page = VisualisationPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Аналитика'"):
        page.SB_ANALYTICS.click()

    with allure.step("Клик в меню 'Визуализации'"):
        page.SB_ANALYTICS_VISUALISATIONS.click()

    with allure.step("Открылась страница 'Визуализации'"):
        browser.wait_for_url(page.host + VisualisationPage.page_path)
