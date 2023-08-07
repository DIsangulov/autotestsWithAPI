import time

from pages.Helpers.base_page import BasePage
from resourses.locators import RoleMiningLocators, MainLocators, AdminLocators


class AdStatus(BasePage):

    def open_rm_ad_status_statistic(self):
        self.page.click(RoleMiningLocators.ROLE_MINING)
        self.page.click(RoleMiningLocators.ADSTATUS)

    def should_enter_rm_ad_status_statistic_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Состояние Active Directory" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/role-mining/state-ad/statistics", "URL's do not match"

    def open_rm_ad_status_recommendation(self):
        self.page.click(RoleMiningLocators.RECOMMENDATION)

    def should_enter_rm_ad_status_recommendation_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Состояние Active Directory" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.host + "/role-mining/state-ad/recommendations", "URL's do not match"

    def configuring_anomaly_distribution(self):
        self.page.click(RoleMiningLocators.GEAR_BUTTON)

    def input_server_address_and_port(self):
        self.page.fill(RoleMiningLocators.SERVER_ADDERESS, '100.123.0.11')
        self.page.fill(RoleMiningLocators.PORT, '333')

    def select_tcp_exchange_protocol(self):
        self.page.click(RoleMiningLocators.DROPDOWN_EXCHANGE_PROTOCOL)
        self.page.click(MainLocators.DROPDOWN1)

    def select_udp_exchange_protocol(self):
        self.page.click(RoleMiningLocators.DROPDOWN_EXCHANGE_PROTOCOL)
        self.page.click(MainLocators.DROPDOWN2)

    def click_add_button(self):
        self.page.click(RoleMiningLocators.ADD_BUTTON)
        time.sleep(2)

    def should_tcp_distribution_protocol_save_sucsess(self):
        assert self.page.wait_for_selector("text=100.123.0.11;333;TCP"), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def should_udp_distribution_protocol_save_sucsess(self):
        assert self.page.wait_for_selector("text=100.123.0.11;333;UDP"), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def enter_email(self):
        self.page.click(RoleMiningLocators.CHECKBOX_SYSLOG)
        self.page.click(RoleMiningLocators.CHECKBOX_EMAIL)
        self.page.fill(RoleMiningLocators.INPUT_EMAIL, 'dataplan_qaa@ngrsoftlab.ru')

    def should_email_save_sucsess(self):
        assert self.page.wait_for_selector("dataplan_qaa@ngrsoftlab.ru"), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def delete_last_entry(self):
        self.page.click(RoleMiningLocators.TRASH_ICON)
        self.page.click(RoleMiningLocators.DELETE_BUTTON)

    def should_last_entry_deleted(self):
        assert self.page.wait_for_selector("Настройка рассылки успешно удалена"), \
            "Найдено несовпадение ожидаемого результата с фактическим"

    def close_window(self):
        self.page.click(MainLocators.X_BUTTON)
        self.page.click(MainLocators.CLOSE_BUTTON)
