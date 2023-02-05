from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(**playwright.devices["iPhone 13"])
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("textbox", name="Поиск в Google").click()
    page.get_by_role("textbox", name="Поиск в Google").fill("apple")
    page.get_by_role("textbox", name="Поиск в Google").press("Enter")
    page.get_by_role("link", name="Служба поддержки").click()
    expect(page).to_have_url('https://support.apple.com/ru-ru')
    # page.get_by_role("heading", name="Служба поддержки Apple").click()
    page.get_by_role("link", name="Поддержка iPhone").click()
    page.get_by_role("link", name="Не помню код-пароль").click()
    expect(page).to_have_title('Если вы забыли код-пароль для iPhone - Служба поддержки Apple (RU) ')

    # ---------------------
    context.close()
    browser.close()
