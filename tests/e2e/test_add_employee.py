from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage



def test_add_employee_without_login(admin_login):
    page = admin_login
    dashboard = DashboardPage(page)
    employee = AddEmployeePage(page)

    dashboard.go_to_pim()
    employee.add_employee("hala", "abed", "shream")


def test_add_employee_with_login(admin_login):
    page = admin_login
    dashboard = DashboardPage(page)
    employee = AddEmployeePage(page)

    dashboard.go_to_pim()
    employee.add_employee_with_login(
        "menna",
        "abed",
        "shream",
        "menna",
        "menna@12345"
    )