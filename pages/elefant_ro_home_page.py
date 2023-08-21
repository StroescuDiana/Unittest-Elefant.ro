import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from page_objects.HomePageObjects import HomePageObjects
from page_objects.SearchResultsObjects import SearchResultsObjects
from pages.base_page import BasePage


class HomePage(BasePage, HomePageObjects):

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        super().open(super().url)  #opens the inherited URL
        self.driver.implicitly_wait(5)  #waits for elements to load
        super().accept_cookies(super().cookies_accept_button_locator)  #Clicks on "Accept" cookies button

    def search_for_item(self):
        super().input_text(super().search_box_locator, super().item)  #inserts a text in the search box
        super().click(super().search_button_locator)  #clicks the search button

    def click_account(self):
        super().click(super().cont_icon_locator)  #clicks the cont icon
        super().click(super().conectare_bttn_locator)  #clicks "CONECTARE" button