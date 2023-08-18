from selenium.webdriver.common.by import By


class SearchResultsObjects:
    product_title_locator = (By.XPATH, "//a[@class='product-title']")
    product_price_locator = (By.XPATH, "//div[@class='current-price ']")
    expected_title = "Cauti iphone 14? - Vino pe Elefant.ro!"