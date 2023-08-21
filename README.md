# Web Automation and Testing with Python and Selenium

![Python](https://img.shields.io/badge/Python-3.11.4-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.11.2-green)

## Introduction

This repository showcases my skills in web automation and testing using Python and Selenium. I successfully completed a series of exercises that involved automating interactions with a website, specifically [elefant.ro](https://www.elefant.ro/).

## Test Scenarios

### Test 1: Website Access
- I utilized Selenium to open the website [elefant.ro](https://www.elefant.ro/).

### Test 2: Product Search
- Employing Python and Selenium, I automated the process of searching for a product (e.g., "iPhone 14") and verified that at least 10 results were returned.

### Test 3: Lowest-Priced Product
- I extracted the product with the lowest price from the search results using Selenium and relevant selectors.

### Test 4: Page Title Verification
- Using Selenium, I extracted and validated the correctness of the webpage's title.

### Test 5: Login Functionality Testing
- I automated the login process by entering incorrect username and password values.
- I verified two crucial aspects:
    1. Ensured that login did not succeed (user remains unauthenticated).
    2. Checked if the correct error message was displayed.

### Test 6: Email Field Validation
- I simulated user input by entering an invalid email address (without the "@" symbol) into the email field.
- I verified that the "login" button was correctly disabled after entering an invalid email address.

## How to Run the Tests

To run these tests locally, follow these steps:

1. Clone this repository to your local machine.
2. Install Python 3.11.4 and the packages from requirements.txt.
3. Navigate to the `test_cases/` directory.
4. Run the test suite `test_suite.py`
