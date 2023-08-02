from playwright.sync_api import Page


class BaseCase:

    def __init__(self, _page: Page):
        self._page = _page
