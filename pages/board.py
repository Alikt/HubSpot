class Board:
    def __init__(self, page):
        self.page = page

        # Page locators
        self.open_board_list_category = page.locator('[aria-label="open"]')
        self.categories_1 = page.locator('[name="Design"]')