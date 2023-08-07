from pages.Helpers.base_page import BasePage
from resourses.locators import AnalyticsLocators, MainLocators, AdminLocators


class MailingLists(BasePage):
    def open_an_mailing_lists_reports(self):
        self.page.click(AnalyticsLocators.ANALYTICS)
        self.page.click(AnalyticsLocators.MAILING_LISTS)
        self.page.click(AnalyticsLocators.MAILING_LISTS_REPORTS)

    def open_an_mailing_lists_new_data(self):
        self.page.click(AnalyticsLocators.MAILING_LISTS_NEW_DATA)

    def should_enter_an_mailing_lists_reports_be_successful(self):
        self.wait_for_page_load(AdminLocators.TITLE_MSG_NEW)
        assert "Рассылки" in self.is_element_present(AdminLocators.TITLE_MSG_NEW).inner_text(), \
            "Найдено несовпадение ожидаемого результата с фактическим"
        # assert self.page.url == self.url + "/storage/rules", "URL's do not match"
