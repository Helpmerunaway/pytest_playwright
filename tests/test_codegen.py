from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/", wait_until='domcontentloaded')
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_role("listitem").filter(has_text="Создать первый сценарий playwright").get_by_role("checkbox").check()

    # ---------------------
    context.close()
    browser.close()


def test_add_todo(page):
    page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
