from playwright.sync_api import Page, expect


class EmployeeSearchPage:

    def __init__(self, page: Page):
        self.page = page

        self.pim_menu = page.get_by_role("link", name="PIM")

     
        self.employee_name_input = page.get_by_role(
            "textbox", name="Type for hints..."
        ).first
        self.search_button = page.get_by_role("button", name="Search")

       
        self.employee_id_input = page.get_by_role("textbox").nth(2)

    def open_pim(self):
        self.pim_menu.click()

 
    def search_by_name(self, name):
        self.employee_name_input.fill(name)
        self.page.get_by_role("option", name=name).click()
        self.search_button.click()

    
    def search_by_id(self, emp_id):
        self.employee_id_input.fill(emp_id)
        self.search_button.click()

    def open_result(self, emp_id, name):
        self.page.get_by_role(
            "row", name=f"{emp_id} {name}"
        ).click()