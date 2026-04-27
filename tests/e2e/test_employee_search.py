from uuid import uuid4

from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_search_page import EmployeeSearchPage


def test_search_employee(admin_login):

    page = admin_login
    suffix = uuid4().hex[:6]
    first_name = f"halla{suffix}"
    middle_name = "a"
    last_name = f"sh{suffix}"
    full_name = f"{first_name} {middle_name} {last_name}"

    dashboard = DashboardPage(page)
    employee = AddEmployeePage(page)
    search = EmployeeSearchPage(page)
    dashboard.go_to_pim()


    employee.add_employee(first_name, middle_name, last_name)


    emp_id = employee.get_employee_id()


    search.open_pim()
    search.search_by_name(full_name)

 
    search.open_pim()
    search.search_by_id(emp_id)
