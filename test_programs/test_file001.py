from selenium import webdriver

class TestCredence:
    def test_sum01(self):
        a = 3
        b = 7
        sum = a + b
        print("sum of A & b --." + str(sum))


    def test_crde_log1(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("you ae at credence site")

        else:
            print("you are at wrong site")