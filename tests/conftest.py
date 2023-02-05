import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     response = authenticate(user)
#     return {
#         **browser_context_args
#         "storage_state": {
#             "cookies": [
#                 {
#                     "name": "token",
#                     "value": "sd4fFfv!x_cfc",
#                 },
#             ]
#         },
#     }