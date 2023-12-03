# Selenium Login Test Automation

## Introduction
This Selenium test script demonstrates automated testing of the login functionality on a web application using Python's Selenium library.

### Test Scenario
- The test suite checks the login functionality of a web application by attempting to login with valid and invalid credentials.
- It validates the login process by checking if the appropriate error message is displayed for invalid credentials and verifies the successful redirection to the dashboard after logging in with valid credentials.

## Technologies Used
- Python
- Selenium WebDriver
- HTMLTestRunner

## Setup and Execution
1. Install Python if not already installed.
2. Install the necessary packages:
    ```bash
    pip install selenium webdriver-manager html-testRunner
    ```
3. Clone the repository:
    ```bash
    git clone <repository_URL>
    ```
4. Navigate to the project directory:
    ```bash
    cd path/to/project
    ```
5. Run the tests:
    ```bash
    python login_tests.py
    ```

## Test Cases
- **test_login_not_valid:** Validates the behavior of the login process with invalid credentials by checking for the 'Invalid credentials' error message.
- **test_login_valid:** Tests the successful login process with valid credentials and verifies the redirection to the dashboard.

## Test Execution Reports
The test execution generates HTML reports located in the `Reports` directory after test completion.

## Contributors
- [Massimiliano Visintainer](https://github.com/MassimilianoVisintainer)

## Acknowledgments
- The Selenium community and contributors for providing a robust testing framework.

