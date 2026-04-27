import pytest
from playwright.sync_api import sync_playwright
from data.constants import ADMIN_PASSWORD, ADMIN_USERNAME
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.vacancies_page import VacanciesPage

@pytest.fixture
def admin_login():
    """Fixture to launch browser, login as Admin, and provide page for a test."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)  
        context = browser.new_context()
        page = context.new_page()

    
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)

    
        yield page

        
        context.close()
        browser.close()


@pytest.fixture
def vacancy_factory(admin_login):
    page = admin_login
    dashboard = DashboardPage(page)
    vacancies = VacanciesPage(page)
    created_vacancies = []

    def _create(vacancy_data):
        dashboard.go_to_recruitment()
        vacancies.open_vacancies()
        vacancies.delete_vacancies_by_name(vacancy_data["name"])
        dashboard.go_to_recruitment()
        vacancies.open_vacancies()
        vacancies.add_vacancy(vacancy_data)
        created_vacancies.append(vacancy_data["name"])
        return {
            "page": page,
            "vacancy_name": vacancy_data["name"],
        }

    yield _create

    for vacancy_name in reversed(created_vacancies):
        dashboard.go_to_recruitment()
        vacancies.open_vacancies()
        vacancies.delete_vacancies_by_name(vacancy_name)
