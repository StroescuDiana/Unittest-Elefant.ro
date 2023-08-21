"""
Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
Identificati elementele de tip user si parola si inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
- Dati click pe butonul "conectare" si verificati urmatoarele:
             1. Faptul ca nu s-a facut logarea in cont
             2. Faptul ca se returneaza eroarea corecta
Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@") si verificati faptul ca butonul "conectare" este dezactivat
"""

import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.LoginPageObjects import LoginPageObjects
from pages.base_page import BasePage
from pages.elefant_ro_home_page import HomePage
from pages.login_page import LoginPage


class TestsFrom5To6(unittest.TestCase, BasePage, LoginPageObjects):

    GREEN = '\033[92m'
    RESET = '\033[0m'


    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_5_6(self):

        elefant_ro = HomePage(self.driver)
        elefant_ro.open_page()
        elefant_ro.click_account()  #Test 5

        login_page = LoginPage(self.driver)
        #Checks if the redirected page is the same as the expected login page
        assert login_page.check_if_redirected_to_login_page() == super().log_in_url, f"Nu te afli pe pagina de conectare. Va aflati pe {login_page.check_if_redirected_to_login_page}"

        actual_url = super().get_page_url()  #unsuccessful URL
        expected_url = super().log_in_successful_url
        #Checks that the login was unsuccessful
        assert not actual_url == expected_url, "Te-ai logat cu succes in cont!"  #Test 5.1

        #Checks that the current error text is the same as the expected one
        assert login_page.login_with_invalid_credentials() == super().expected_error, f"Mesajul {login_page.login_with_invalid_credentials()} nu este la fel ca cel asteptat {super().expected_error}"  #Test 5.2
        print(f"{self.GREEN}Mesajul este cel asteptat.{self.RESET}")

        login_page.invalid_email_login()  #Test 6
        assert not login_page.visibility_of_conectare_btn() == True, "Butonul 'CONECTARE' nu este dezactivat."  #Test 6
        print(f"{self.GREEN}Butonul 'CONECTARE' este dezactivat.{self.RESET}")

    def tearDown(self):
        self.driver.quit()