from playwright.sync_api import Page


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page
        self.pim_menu = page.get_by_role("link", name="PIM")

    def go_to_pim(self):
        self.pim_menu.click()
        