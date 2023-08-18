from selenium.webdriver.common.by import By


class LoginPageObjects:
    log_in_url = "https://www.elefant.ro/login"
    log_in_successful_url = "https://www.elefant.ro/my-account?TrackingDataContainerID=#__sMDExNjY4MjE"
    email_field_locator = (By.XPATH, "//input[@class='form-control' and @name='ShopLoginForm_Login']")
    wrong_email_address = "fake_account@yahoo.com"
    invalid_email_address = "fake_account.com"
    password_field_locator = (By.XPATH, "//input[@class='form-control' and @type='password']")
    wrong_password = "ksjfbs1232@!"
    conectare_btn_locator = (By.XPATH, "//button[contains(text(), 'Conectare')]")
    error_alert_locator = (By.XPATH, "//div[@class='alert alert-danger']")
    expected_error = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."