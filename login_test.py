from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTests():

    def test_validLogin(self):
        driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')
        baseURL = 'https://letskodeit.teachable.com'
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.LINK_TEXT, 'Login')
        loginLink.click()

        emailfield = driver.find_element(By.ID, 'user_email')
        emailfield.send_keys('apoorva.agrawal.86@gmail.com')

        passwordfield = driver.find_element(By.ID, 'user_password')
        passwordfield.send_keys('Formul@1')

        loginButton = driver.find_element(By.NAME, 'commit')
        loginButton.click()

        userIcon = driver.find_element(By.XPATH, './/*[@id="navbar"]//span[text()="User Settings"]')
        if userIcon is not None:
            print('Login Successful')
        else:
            print('Login Failed')

ff = LoginTests()
ff.test_validLogin()
