from playwright.sync_api import Page

from pages.Helpers.base_page import BasePage


class SourcesEditorPage(BasePage):

    page_path = "/datasource/create/editor"

    def __init__(self, page: Page):
        super().__init__(page)
        self.page_path = SourcesEditorPage.page_path

        self.ADD_THIS_THINGS = None

    def new_source(self):
        self.open()

    def edit_source(self, source_id):
        target_path = f"/datasource/{source_id}/editor"
        self.goto_page(target_path)
        self.page.wait_for_url(self.host + target_path)
