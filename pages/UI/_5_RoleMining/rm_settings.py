import time

from selenium.webdriver.common.by import By

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators, AdminLocators


class RmSettings(BasePage):
    def open_rm_settings_sources(self):
        self.page.click(RoleMiningLocators.ROLE_MINING)
        self.page.click(RoleMiningLocators.SETTINGS)

    def should_enter_rm_settings_sources_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки Role mining" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/role-mining/settings/source", "URL's do not match"

    def open_rm_settings_calculation_settings(self):
        self.page.click(RoleMiningLocators.CALCULATION_SETTINGS)

    def should_enter_rm_settings_calculation_settings_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Настройки Role mining" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/role-mining/settings/calc", "URL's do not match"

    def clear_sources_rm_settings(self):
        self.wait_until_elem_be_clickable(RoleMiningLocators.CLEAR_BUTTON)
        self.page.click(RoleMiningLocators.CLEAR_BUTTON)

    def not_confirm_cleaning_rm_settings(self):
        self.wait_until_elem_be_clickable(RoleMiningLocators.CLEAR_BUTTON_NO)
        self.page.click(RoleMiningLocators.CLEAR_BUTTON_NO)

    def confirm_cleaning_rm_settings(self):
        self.wait_until_elem_be_clickable(RoleMiningLocators.CLEAR_BUTTON_YES)
        self.page.click(RoleMiningLocators.CLEAR_BUTTON_YES)

    def selecting_values_from_dropdown_list(self):
        self.page.click(RoleMiningLocators.SELECT_DB)
        self.page.click(RoleMiningLocators.SELECT_DB_CHOISE)
        self.page.click(RoleMiningLocators.SELECT_TABLE)
        self.page.click(RoleMiningLocators.SELECT_DB_CHOISE)
        self.page.click(RoleMiningLocators.SELECT_TABLE)
        self.page.click(RoleMiningLocators.SELECT_DB_CHOISE)
        self.page.click(RoleMiningLocators.SAVE_BUTTON)

    def should_sources_saved(self):
        self.page.click(RoleMiningLocators.SAVE_BUTTON)
        assert self.page.wait_for_selector("text=Источники сохранены"), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def should_sources_recalculated(self):
        self.page.click(RoleMiningLocators.SAVE_DROPDOWN_BUTTON)
        self.page.click(RoleMiningLocators.RECALCULATE_BUTTON)
        self.page.click(RoleMiningLocators.RERUN_BUTTON)
        assert self.page.wait_for_selector("text=Расчёт запущен"), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def calculation_settings(self):
        self.page.click(RoleMiningLocators.CALCULATION_SETTINGS)