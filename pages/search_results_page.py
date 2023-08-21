from page_objects.SearchResultsObjects import SearchResultsObjects
from pages.base_page import BasePage


class SearchResultsPage(BasePage, SearchResultsObjects):

    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

    def check_number_of_products_returned(self):
        #finds all product_title_locator elements displayed on the visible screen
        products_returned = super().find_elements(super().product_title_locator)

        if len(products_returned) >= 10:  #If the lenght of products_returned is greater or equal to 10 then:
            print(f"{self.GREEN}Exista cel putin 10 produse pe pagina elefant.ro{self.RESET}")
        else:
            print(f"{self.RED}Exista mai putin de 10 produse pe pagina elefant.ro{self.RESET}")

    def smallest_price(self):
        #finds all product_price_locator elements displayed on the visible screen
        web_elements = super().find_elements(super().product_price_locator)

        prices = []  #initialized an empty list in order to add the prices from the visible products in the carousel
        for price in web_elements:  #for each price in web_elements:
            price_without_currency = price.text.replace(" lei", "")  #removes the currency, leaving just the numeric part
            accepted_price_format = price_without_currency.replace(",", ".")  #replaces <,> with <.> in order to type cast into a float
            price = float(accepted_price_format)  #type casting to float data type
            prices.append(price)  #adds the float number to the list

        min_price = min(prices)  #finds the minimum price in the prices LIST
        print(f"Cel mai mic pret este {min_price} lei.")

    def is_correct_page_title(self):
        return self.get_page_title()  #returns the title of the current page