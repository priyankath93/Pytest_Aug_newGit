import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Testcheckoutcredkart01:
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

    def test_checkout(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@credence.in")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Priyanka")
        driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Mahalle")
        driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("8237100397")
        driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Ulwe new Mumbai")
        driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("410206")
        state = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
        state.select_by_index(2)
        driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")
        driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
        year = Select(driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        year.select_by_index(2)
        time.sleep(2)
        month = Select(driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        month.select_by_index(2)
        driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
        print(driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)
        time.sleep(2)
        driver.close()

    # def test_sum1(self):
    #     a = 10
    #     b = 20
    #     sum1 = a + b
    #     print("Sum of two no = " + str(sum1))
