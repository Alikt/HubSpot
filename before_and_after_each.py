from playwright.async_api import async_playwright, Page


async def open_browser_with_cookies():
    with async_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.newPage()
