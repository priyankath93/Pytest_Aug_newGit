from selenium import webdriver
from selenium.webdriver.common.by import By

class Testcrdekartlog01:
    def test_credkart01(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credencetest@test.com")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("login is passed")
            driver.close()
            assert True

        except:
            print("login case failed")
            driver.close()
            assert False
