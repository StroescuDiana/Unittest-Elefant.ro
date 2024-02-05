
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def wait_for_presence_of(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.presence_of_element_located(locator))

    def input_text(self, locator: tuple, message: str):
        return self.find(locator).send_keys(message)

    def click(self, locator):
        self.find(locator).click()

    def get_page_title(self):
        return self.driver.title

    def get_page_url(self):
        page_url = self.driver.current_url
        return page_url

    def get_text(self, locator: tuple):
        self.wait_for_presence_of(locator)
        return self.find(locator).text

    def is_enabled(self, locator: tuple):
        self.wait_for_presence_of(locator)
        return self.find(locator).is_enabled()