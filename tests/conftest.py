import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def admin_login():
    """Fixture to launch browser, login as Admin once, and provide page for all tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)  
        context = browser.new_context()
        page = context.new_page()

    
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.login("Admin", "admin123")

    
        yield page

        
        context.close()
        browser.close()