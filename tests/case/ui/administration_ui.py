import time

from pages.Helpers.base_case import BaseCase
from pages.UI._1_Administration.adm_roles import Roles


class AdministrationCase(BaseCase):

    def open_adm_roles(self):
        page = Roles(self._page)
        page.open()
        # todo: case

    def another_case(self):
        pass
