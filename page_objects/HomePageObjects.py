from selenium.webdriver.common.by import By


class HomePageObjects:

    url = "https://www.elefant.ro/"
    cookies_accept_button_locator = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    search_box_locator = (By.XPATH, "//input[@class='form-control searchTerm js-has-overlay']")
    search_button_locator = (By.XPATH, "//button[@class='btn-search btn btn-primary']")
    item = "iphone 14"
    cont_icon_locator = (By.XPATH, "//span[contains(text(), 'Cont')]/preceding-sibling::i")
    conectare_bttn_locator = (By.XPATH, "//a[@class='my-account-login btn btn-primary btn-block']")

