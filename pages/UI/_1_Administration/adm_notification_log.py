import time

from pages.Helpers.base_page import BasePage
from resourses.locators import AdminLocators


class NotificationLog(BasePage):
    def open_adm_notification_log_user(self):
        # self.browser.find_element(*AdminLocators.ADMINISTRATION).click()
        self.browser.find_element(*AdminLocators.NOTIFICATION_LOG).click()
        self.browser.find_element(*AdminLocators.NOTIFICATION_LOG_USER).click()
        time.sleep(1)

    def should_enter_adm_notification_log_user_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Журнал уведомлений", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/notifications-list/user", \
            "URL не совпадают"

    def open_adm_notification_log_admin(self):
        self.browser.find_element(*AdminLocators.NOTIFICATION_LOG_ADMIN).click()
        time.sleep(1)

    def should_enter_adm_notification_log_admin_be_successful(self):
        self.is_element_present(*AdminLocators.TITLE_MSG_OLD)
        assert self.is_element_present(*AdminLocators.TITLE_MSG_OLD).text == "Журнал уведомлений", \
            "Найдено несовпадение ожидаемого результата с фактическим"
        assert self.browser.current_url == self.url + "/notifications-list/admin", \
            "URL не совпадают"
