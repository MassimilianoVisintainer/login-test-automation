class Locators():

    #Login page objects
    username_textbox_xpath = "//input[@name='username' and contains(@class, 'oxd-input')]"
    password_textbox_xpath = "//input[@name='password' and contains(@class, 'oxd-input')]"
    login_button_xpath = "//button[@type='submit' and  contains(@class, 'orangehrm-login-button')]"
    alert_message_xpath = "//p[contains(@class, 'oxd-alert-content-text') and text()='Invalid credentials']"

    #Homepage objects
    user_dropdown_xpath = '//p[@class="oxd-userdropdown-name"]'
    logout_link_linkText = "Logout"