from typing import re

import pytest
from playwright.async_api import Page
from playwright.sync_api import expect


class TestLogin:

    @pytest.fixture(scope="class", autouse=True)
    def select_board(self, page: Page):
        # Call open browser

        page.goto("https://trello.com/")

        # Expect a title "to contain" a substring.
        expect(page).to_have_title(re.compile("Trello"))
