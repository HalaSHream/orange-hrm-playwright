from uuid import uuid4

from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage



def test_add_employee_without_login(admin_login):
    page = admin_login
    suffix = uuid4().hex[:6]
    first_name = f"hala{suffix}"
    middle_name = "abed"
    last_name = f"shream{suffix}"
    dashboard = DashboardPage(page)
    employee = AddEmployeePage(page)

    dashboard.go_to_pim()
    employee.add_employee(first_name, middle_name, last_name)


def test_add_employee_with_login(admin_login):
    page = admin_login
    suffix = uuid4().hex[:6]
    first_name = f"menna{suffix}"
    middle_name = "abed"
    last_name = f"shream{suffix}"
    username = f"menna_{suffix}"
    dashboard = DashboardPage(page)
    employee = AddEmployeePage(page)

    dashboard.go_to_pim()
    employee.add_employee_with_login(
        first_name,
        middle_name,
        last_name,
        username,
        "menna@12345"
    )
