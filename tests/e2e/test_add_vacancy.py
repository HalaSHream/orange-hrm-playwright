import pytest
from data.vacancy_data import VACANCY_CASES, build_vacancy_data
from pages.vacancies_page import VacanciesPage
from utils.tracing import playwright_trace


@pytest.mark.parametrize(
    "vacancy_case",
    VACANCY_CASES,
    ids=[
        "qa-engineer-active",
        "it-manager-inactive",
        "software-engineer-active",
    ],
)
@playwright_trace(page_fixture_name="admin_login")
def test_add_vacancy(admin_login, request, vacancy_factory, vacancy_case):
    _ = (admin_login, request)
    vacancy_data = build_vacancy_data(vacancy_case)
    created_vacancy = vacancy_factory(vacancy_data)
    VacanciesPage(created_vacancy["page"]).expect_vacancy_details(vacancy_data)
