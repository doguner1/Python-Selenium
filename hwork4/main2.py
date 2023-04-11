
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Odev:

    def __init__(self) -> None:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("http://www.saucedemo.com/")
        sleep(5)

    def kullanici_adi(self):
        userInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        userInput.send_keys("")
        passwordInput.send_keys("")
        sleep(5)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print("\n --- Kullanici adi ve şifre girilmemiştir uyarisi testi ---\n")
        print(f"Test Sonucu: {testResult}")


    def kullanici_sifre(self):
        userInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        userInput.send_keys("1234")
        passwordInput.send_keys("")
        sleep(5)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print("\n --- Kullanici şifre girilmemiştir uyarisi testi ---\n")
        print(f"Test Sonucu: {testResult}")


    def kullanici_kilit_kontrol(self):
        userInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        userInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print("\n --- Kullanici adi ve şifresi kilitli uyarisi testi ---\n")
        print(f"Test Sonucu: {testResult}")

    def icon_kontrol(self):
        userInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        userInput.send_keys("")
        passwordInput.send_keys("")
        sleep(5)
        loginBtn.click()
        errorBtnIcon = self.driver.find_element(By.CLASS_NAME,"svg-inline--fa fa-times-circle fa-w-16 error_icon")
        errorBtnIcon.click()
        print("\n --- Error button is closed ---\n")

    def inventory_kontrol(self):
        userInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        userInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginBtn.click()
        sleep(2)
        print("\n --- Login is successful ---\n")
        
    def product_kontrol(self):
        userInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        userInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginBtn.click()
        sleep(2)
        product_num = self.driver.find_elements(By.CLASS_NAME, "inventory-item")
        print(f"Product number is : {len(product_num)}")
        sleep(30)

        


testClass = Test_Odev()
# testClass.kullanici_adi()
# testClass.kullanici_sifre()
# testClass.kullanici_kilit_kontrol()
# testClass.icon_kontrol()
# testClass.inventory_kontrol()
testClass.product_kontrol()

while True:
    continue
