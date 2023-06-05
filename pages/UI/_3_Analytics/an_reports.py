import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AnalyticsLocators, MainLocators, AdminLocators
from faker import Faker

fake = Faker()
name = fake.sentence(nb_words=3)  # генерация случайного названия из 2 слов
description = fake.sentence(nb_words=20)  # генерация случайного описания из 20 слов
saved_report_name = None


class Reports(BasePage):
    def open_an_reports(self):
        self.page.click(AnalyticsLocators.REPORTS)

    def should_enter_an_reports_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Отчеты" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/report", "URL's do not match"

    def create_new_report(self):
        self.page.click(AnalyticsLocators.ADD_REPORT_BUTTON)
        self.page.fill(AnalyticsLocators.REPORT_NAME_AREA_IN, name)
        self.page.fill(AnalyticsLocators.REPORT_DESCRIPTION_IN, description)
        self.page.click(MainLocators.SAVE_BUTTON)
        self.page.click(AnalyticsLocators.ADD_REPORT_BUTTON)

    def open_access_settings(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)

    def do_report_public(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        self.page.click(AnalyticsLocators.PUBLESHED_TOGLER_ON)
        self.page.click(MainLocators.X_BUTTON)

    def do_report_open(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        self.page.click(AnalyticsLocators.REPORT_CLOSED_TOGLER)
        self.page.click(MainLocators.X_BUTTON)

    def save_last_report_name(self):
        time.sleep(2)
        global saved_report_name
        saved_report_name = self.page.locator("(//td[@data-label='Отчет']/a)[1]").inner_text()

    def should_report_not_visible_by_name(self):
        assert not self.is_element_present("//*[contains(text(),'" + name + "')]")

    def should_report_not_visible_by_saved_name(self):
        assert not self.is_element_present("//*[contains(text(),'" + str(saved_report_name) + "')]")

    def open_last_report(self):
        time.sleep(2)
        self.page.click(AnalyticsLocators.LAST_REPORT_IN_LIST)

    def should_edit_button_not_available(self):
        assert self.is_element_present(AnalyticsLocators.ADD_REPORT_BUTTON).is_disabled()

    def should_edit_button_available(self):
        assert self.is_element_present(AnalyticsLocators.ADD_REPORT_BUTTON).is_enabled()

    def should_access_settings_not_available_for_not_public_report(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        time.sleep(2)
        assert self.is_element_present(AnalyticsLocators.PUBLESHED_TOGLER_ON).is_disabled()
        assert self.is_element_present(AnalyticsLocators.REPORT_CLOSED_TOGLER).is_disabled()

    def should_access_settings_not_available_for_public_report(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        time.sleep(2)
        assert self.is_element_present(AnalyticsLocators.PUBLESHED_TOGLER_OFF).is_disabled()
        assert self.is_element_present(AnalyticsLocators.REPORT_CLOSED_TOGLER).is_disabled()

    def should_access_settings_available(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        time.sleep(2)
        assert self.is_element_present(AnalyticsLocators.PUBLESHED_TOGLER_OFF).is_enabled()
        assert self.is_element_present(AnalyticsLocators.REPORT_CLOSED_TOGLER).is_enabled()

    def should_role_added_not_available(self):
        self.page.click(AnalyticsLocators.ROLE)
        self.page.click(AnalyticsLocators.ROLE_SYSOP)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_READ)
        assert self.is_element_present(MainLocators.ADD_BUTTON).is_disabled()

    def should_role_added_available(self):
        self.page.click(AnalyticsLocators.ROLE)
        self.page.click(AnalyticsLocators.ROLE_SYSOP)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_READ)
        assert self.is_element_present(MainLocators.ADD_BUTTON).is_enabled()

    def should_user_added_not_available(self):
        self.page.click(AnalyticsLocators.USERS_TAB)
        self.page.click(AnalyticsLocators.USERS)
        self.page.click(AnalyticsLocators.USER_DATAPLAN_QAA)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_READ)
        assert self.is_element_present(MainLocators.ADD_BUTTON).is_disabled()

    def should_user_added_available(self):
        self.page.click(AnalyticsLocators.USERS_TAB)
        self.page.click(AnalyticsLocators.USERS)
        self.page.click(AnalyticsLocators.USER_DATAPLAN_QAA)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_READ)
        assert self.is_element_present(MainLocators.ADD_BUTTON).is_enabled()

    def delete_last_report(self):
        self.page.click(AnalyticsLocators.TRASH)
        self.page.click(AnalyticsLocators.CONFIRM_TRASH)

    def should_report_not_visible(self):
        assert not self.is_element_present("//*[contains(text(),'" + name + "')]")

    def role_add_read(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        self.page.click(AnalyticsLocators.ROLE)
        self.page.click(AnalyticsLocators.ROLE_SYSOP)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_READ)
        self.page.click(MainLocators.ADD_BUTTON)
        self.page.click(MainLocators.X_BUTTON)

    def role_add_write(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        self.page.click(AnalyticsLocators.ROLE)
        self.page.click(AnalyticsLocators.ROLE_SYSOP)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_WRITE)
        self.page.click(MainLocators.ADD_BUTTON)
        self.page.click(MainLocators.X_BUTTON)

    def role_add_execute(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        self.page.click(AnalyticsLocators.ROLE)
        self.page.click(AnalyticsLocators.ROLE_SYSOP)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_EXECUTE)
        self.page.click(MainLocators.ADD_BUTTON)
        self.page.click(MainLocators.X_BUTTON)

    def role_add_access_settings(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        self.page.click(AnalyticsLocators.ROLE)
        self.page.click(AnalyticsLocators.ROLE_SYSOP)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_ACCESS_SETTINGS)
        self.page.click(MainLocators.ADD_BUTTON)
        self.page.click(MainLocators.X_BUTTON)

    def should_checkbox_read_enable(self):
        assert self.page.locator(AnalyticsLocators.CHECKBOX_READ).is_checked()

    def should_checkbox_write_enable(self):
        assert self.page.locator(AnalyticsLocators.CHECKBOX_WRITE).is_checked()

    def should_checkbox_execute_enable(self):
        assert self.page.locator(AnalyticsLocators.CHECKBOX_EXECUTE).is_checked()

    def should_checkbox_access_settings_enable(self):
        assert self.page.locator(AnalyticsLocators.CHECKBOX_ACCESS_SETTINGS).is_checked()

    def switch_users_tab(self):
        self.page.click(AnalyticsLocators.ACCESS_SETTINGS)
        self.page.click(AnalyticsLocators.USERS_TAB)

    def should_checkbox_read_enable_for_users_tab(self):
        assert self.page.locator(AnalyticsLocators.CHECKBOX_READ_FOR_USERS_TAB).is_checked()

    def should_checkbox_write_enable_for_users_tab(self):
        assert self.page.locator(AnalyticsLocators.CHECKBOX_WRITE_FOR_USERS_TAB).is_checked()

    def should_checkbox_execute_enable_for_users_tab(self):
        assert self.page.locator(AnalyticsLocators.CHECKBOX_EXECUTE_FOR_USERS_TAB).is_checked()

    def should_checkbox_access_settings_enable_for_users_tab(self):
        assert self.page.locator(AnalyticsLocators.CHECKBOX_ACCESS_SETTINGS_FOR_USERS_TAB).is_checked()

    def user_add_read(self):
        self.page.click(AnalyticsLocators.USERS)
        self.page.click(AnalyticsLocators.USER_DATAPLAN_QAA)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_READ)
        self.page.click(MainLocators.ADD_BUTTON)
        self.page.click(MainLocators.X_BUTTON)

    def user_add_write(self):
        self.page.click(AnalyticsLocators.USERS)
        self.page.click(AnalyticsLocators.USER_DATAPLAN_QAA)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_WRITE)
        self.page.click(MainLocators.ADD_BUTTON)
        self.page.click(MainLocators.X_BUTTON)

    def user_add_execute(self):
        self.page.click(AnalyticsLocators.USERS)
        self.page.click(AnalyticsLocators.USER_DATAPLAN_QAA)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_EXECUTE)
        self.page.click(MainLocators.ADD_BUTTON)
        self.page.click(MainLocators.X_BUTTON)

    def user_add_access_settings(self):
        self.page.click(AnalyticsLocators.USERS)
        self.page.click(AnalyticsLocators.USER_DATAPLAN_QAA)
        self.page.click(AnalyticsLocators.ACCESS)
        self.page.click(AnalyticsLocators.ACCESS_ACCESS_SETTINGS)
        self.page.click(MainLocators.ADD_BUTTON)
        self.page.click(MainLocators.X_BUTTON)

    def uncheck_checkboxes_r_w_e(self):
        self.page.click(AnalyticsLocators.CHECKBOX_EXECUTE_FOR_USERS_TAB)
        self.page.click(AnalyticsLocators.CHECKBOX_WRITE_FOR_USERS_TAB)
        self.page.click(AnalyticsLocators.CHECKBOX_READ_FOR_USERS_TAB)
        self.page.click(MainLocators.X_BUTTON)
