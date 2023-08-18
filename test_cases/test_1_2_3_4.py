"""
Test 1: Intrati pe site-ul https://www.elefant.ro/
Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
Test 3: Extrageti din lista produsul cu pretul cel mai mic [class="current-price "] (puteti sa va folositi de find_elements)
Test 4: Extrageti titlul paginii si verificati ca este corect
"""

import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.SearchResultsObjects import SearchResultsObjects
from pages.elefant_ro_home_page import HomePage
from pages.search_results_page import SearchResultsPage


class TestsFrom1To4(unittest.TestCase, SearchResultsObjects):

    GREEN = '\033[92m'
    RESET = '\033[0m'

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_1_2_3_4(self):

        elefant_ro = HomePage(self.driver)
        elefant_ro.open_page()  #Test 1
        elefant_ro.search_for_item()  #Test 2 (first part)

        search_page = SearchResultsPage(self.driver)
        search_page.check_number_of_products_returned()  #Test 2 (second part)
        search_page.smallest_price()  #Test 3
        assert search_page.is_correct_page_title() == super().expected_title, f"Titlul paginii curente: {search_page.is_correct_page_title()} este diferit de cel asteptat: {super().expected_title}"  #Test 4
        print(f"{self.GREEN}Titlul este corect: {super().expected_title}{self.RESET}")

    def tearDown(self):
        self.driver.quit()