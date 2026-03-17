from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage
from pages.employee_search_page import EmployeeSearchPage


def test_search_employee(admin_login):

    page = admin_login

    dashboard = DashboardPage(page)
    employee = AddEmployeePage(page)
    search = EmployeeSearchPage(page)
    dashboard.go_to_pim()


    employee.add_employee("halla", "a", "sh")


    emp_id = employee.get_employee_id()


    search.open_pim()
    search.search_by_name("halla a sh")

 
    search.open_pim()
    search.search_by_id(emp_id)