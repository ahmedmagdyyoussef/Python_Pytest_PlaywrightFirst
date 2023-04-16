import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        pages = context.new_page()
        pages.goto("https://www.youtube.com/")
        ahmed="megz"
        yield pages
        return page
