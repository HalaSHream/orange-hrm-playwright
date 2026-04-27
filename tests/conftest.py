import pytest
from data.constants import ADMIN_PASSWORD, ADMIN_USERNAME
from pages.candidates_page import CandidatesPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.vacancies_page import VacanciesPage


@pytest.fixture
def admin_login(page, base_url):
    """Return a logged-in page using pytest-playwright's built-in page fixture."""
    login = LoginPage(page)
    login.navigate(base_url)
    login.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    return page


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


@pytest.fixture
def candidate_factory(admin_login):
    page = admin_login
    dashboard = DashboardPage(page)
    candidates = CandidatesPage(page)
    created_candidates = []

    def _create(candidate_data):
        dashboard.go_to_recruitment()
        candidates.open_candidates()
        candidates.delete_candidates_by_name(candidate_data.full_name)
        dashboard.go_to_recruitment()
        candidates.open_candidates()
        candidates.add_candidate(candidate_data)
        created_candidates.append(candidate_data)
        return {
            "page": page,
            "candidate": candidate_data,
        }

    yield _create

    for candidate_data in reversed(created_candidates):
        dashboard.go_to_recruitment()
        candidates.open_candidates()
        candidates.delete_candidates_by_name(candidate_data.full_name)
