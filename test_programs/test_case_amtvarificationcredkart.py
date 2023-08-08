import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Testamtvarifiaction01:
    def test_credamtvar01(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@credence.in")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test@123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH, "//select[@class='quantity']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        driver.find_element(By.XPATH, "//h3[normalize-space()='Headphones']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select[1]").click()
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary btn-lg']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//h3[normalize-space()='Playstation 4']").click()
        driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        time.sleep(5)
        prod_qty1 = Select(driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/select[1]"))
        prod_qty1.select_by_index(3)
        time.sleep(2)
        prod_qty2 = Select(driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/select[1]"))
        prod_qty2.select_by_index(4)
        time.sleep(2)
        prod_qty3 = Select(driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/select[1]"))
        prod_qty3.select_by_index(4)
        time.sleep(2)

        l = len(driver.find_elements(By.XPATH, "//tbody/tr/td[4]"))

        product_price_list = []
        for r in range(1, l - 2):
            var1 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            prod_price = (var1[1:])
            product_price_list.append(float(prod_price))

        exp_subtotal = round((sum(product_price_list)), 2)
        print("subtotal-->" + str(exp_subtotal))
        print(product_price_list)

        system_value = []
        for r in range(l - 2, l + 1):
            var2 = driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            var3 = var2.replace(',', '')
            syst_price = (var3[1:])
            system_value.append(float(syst_price))

        print(system_value)
        if exp_subtotal == system_value[0]:
            print("sub total is match")
            assert True
        else:
            print("We are wrong")
            assert False