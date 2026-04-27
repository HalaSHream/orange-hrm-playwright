from playwright.sync_api import Page


class AddEmployeePage:

    def __init__(self, page: Page):
        self.page = page

        self.add_employee_link = page.get_by_role("link", name="Add Employee")

        self.first_name = page.get_by_role("textbox", name="First Name")
        self.middle_name = page.get_by_role("textbox", name="Middle Name")
        self.last_name = page.get_by_role("textbox", name="Last Name")

        self.employee_id_input = page.get_by_role("textbox").nth(4)

        self.create_login_toggle = page.locator(".oxd-switch-input")
        self.username = page.get_by_role("textbox").nth(5)
        self.password = page.locator("input[type='password']").first
        self.confirm_password = page.locator("input[type='password']").nth(1)

        self.save_button = page.get_by_role("button", name="Save")

    def add_employee(self, first, middle, last):
        self.add_employee_link.click()
        self.first_name.fill(first)
        self.middle_name.fill(middle)
        self.last_name.fill(last)
        self.save_button.click()

    def add_employee_with_login(self, first, middle, last, username, password):
        self.add_employee_link.click()
        self.first_name.fill(first)
        self.middle_name.fill(middle)
        self.last_name.fill(last)

        self.create_login_toggle.click()
        self.username.fill(username)
        self.password.fill(password)
        self.confirm_password.fill(password)

        self.save_button.click()

    def get_employee_id(self):
        self.page.wait_for_timeout(1000)  
        emp_id = self.employee_id_input.input_value()
        return emp_id