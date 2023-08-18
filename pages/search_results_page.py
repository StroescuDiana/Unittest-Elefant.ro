from page_objects.SearchResultsObjects import SearchResultsObjects
from pages.base_page import BasePage


class SearchResultsPage(BasePage, SearchResultsObjects):

    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

    def check_number_of_products_returned(self):
        products_returned = super().find_elements(super().product_title_locator)

        if len(products_returned) >= 10:
            print(f"{self.GREEN}Exista cel putin 10 produse pe pagina elefant.ro{self.RESET}")
        else:
            print(f"{self.RED}Exista mai putin de 10 produse pe pagina elefant.ro{self.RESET}")

    def smallest_price(self):
        web_elements = super().find_elements(super().product_price_locator)

        prices = []
        for element in web_elements:
            price_without_currency = element.text.replace(" lei", "")
            accepted_price_format = price_without_currency.replace(",", ".")
            price = float(accepted_price_format)
            prices.append(price)

        min_price = min(prices)
        print(f"Cel mai mic pret este {min_price} lei.")

    def is_correct_page_title(self):
        return self.get_page_title()