import re
from playwright.sync_api import Page, expect


def test_trello_login(page: Page, playwright, context):
    # Call open browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://trello.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Trello"))

    # Click the get started link.
    link = page.get_by_role("link", name="Log in").first
    link.click()

    # Expects page to have a heading with the name of Installation.
    locator = page.get_by_text("Log in to continue")
    expect(locator).to_be_visible()

    # Interact with login form
    page.get_by_test_id("username").fill("iaptest37@gmail.com")
    page.get_by_role("button", name="Continue").click()
    page.get_by_test_id("password").fill("Zz131313")
    page.get_by_role("button", name="Log in").click()

    # MFA challenge dismiss
    if page.get_by_role("button", name="Continue without two-step verification").is_visible():
        page.get_by_role("button", name="Continue without two-step verification").click()

    # Expects valid login.
    expect(page.get_by_text(re.compile("iaptest37")))
    storage = context.storage_state(path="login_state.json")
    page.wait_for_timeout(8000)
    print(storage, flush=True)
    page.wait_for_timeout(8000)


def test_trello_silent_login(page: Page, playwright, context):
    # Call open browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="login_state.json")
    page = context.new_page()
    page.goto("https://trello.com/u/iaptest37/boards")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Trello"))
    page.get_by_role("button", name="Accept all").click()
    page.wait_for_timeout(5000)
    # Expects valid login.
    expect(page.get_by_text(re.compile("iaptest37")))
    page.wait_for_timeout(8000)
