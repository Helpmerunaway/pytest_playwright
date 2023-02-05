from playwright.sync_api import Playwright, sync_playwright, expect
import re


def test_google_query_meme_cat_at_the_table_go_to_memepedia_and_check_title(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Найти").click()
    page.get_by_role("combobox", name="Найти").fill("мем с котом за столом")
    page.get_by_role("combobox", name="Найти").press("Enter")
    page.get_by_role("link", name="Озадаченный кот за столом - Memepedia https://memepedia.ru › Мемы › Пикча").click()
    expect(page).to_have_title(re.compile("Белый кот сидит за столом в ресторане, а женщина на него кричит"))

    # ---------------------
    context.close()
    browser.close()
