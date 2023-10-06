import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._5_RoleMining.rm_role_model_page import RMRoleModelPage


@allure.step("Открыть страницу 'Ролевая модель'")
def open_page_by_steps(browser: Page):
    page = RMRoleModelPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        page.page.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Role mining'"):
        page.SB_ROLE_MINING.click()

    with allure.step("Клик в боковом меню 'Ролевая модель'"):
        page.SB_RM_ROLE_MODEL.click()

    with allure.step("Открыта страница 'Ролевая модель'"):
        expect(browser).to_have_url(page.host + RMRoleModelPage.page_path)
