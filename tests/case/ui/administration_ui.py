import time

from pages.UI._1_Administration.adm_roles import Roles


class AdministrationCase:

    def __init__(self, browser, host: str):
        self.browser = browser
        self.host = host

    def open_adm_roles(self):
        page = Roles(self.browser, self.host)
        page.auth()
        # time.sleep(4)   # fixme: delete
        # page.open_adm_roles()
        page.open()

    def another_case(self):
        pass
