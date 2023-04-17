import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class NotificationLog(BasePage):
    def open_adm_notification_log_user(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.page.click(AdminLocators.NOTIFICATION_LOG)
        self.page.click(AdminLocators.NOTIFICATION_LOG_USER)

    def should_enter_adm_notification_log_user_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Журнал уведомлений" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/personal?tab=user", "URL's do not match"

    def open_adm_notification_log_admin(self):
        self.page.click(AdminLocators.NOTIFICATION_LOG_ADMIN)

    def should_enter_adm_notification_log_admin_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_OLD)
        assert "Журнал уведомлений" in self.is_element_present(AdminLocators.TITLE_MSG_OLD).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.page.url == self.url + "/personal?tab=admin", "URL's do not match"
