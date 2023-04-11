from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert

# Web driver'ı başlat
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")

# Kullanıcı adı ve şifre alanlarına veri girme
username_input = driver.find_element_by_id("user-name")
time.sleep(2)
password_input = driver.find_element_by_id("password")
time.sleep(2)
login_button = driver.find_element_by_id("login-button")
time.sleep(2)

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")

# Login butonuna tıkla
login_button.click()

# 6 adet ürünün bulunmasını bekle
time.sleep(2)

products = driver.find_elements_by_class_name("inventory_item")
assert len(products) == 6

# Test Case 1: Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
username_input.clear()
password_input.clear()
login_button.click()
alert = Alert(driver)
assert "Epic sadface: Username is required" in alert.text
alert.accept()

# Test Case 2: Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
username_input.send_keys("standard_user")
password_input.clear()
login_button.click()
alert = Alert(driver)
assert "Epic sadface: Password is required" in alert.text
alert.accept()

# Test Case 3: Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
username_input.clear()
password_input.clear()
username_input.send_keys("locked_out_user")
password_input.send_keys("secret_sauce")
login_button.click()
alert = Alert(driver)
assert "Epic sadface: Sorry, this user has been locked out." in alert.text
alert.accept()

# Test Case 4: Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
username_input.clear()
password_input.clear()
login_button.click()
username_input_error_icon = driver.find_element_by_xpath("//input[@id='user-name']/following-sibling::button")
password_input_error_icon = driver.find_element_by_xpath("//input[@id='password']/following-sibling::button")
assert username_input_error_icon.is_displayed()
assert password_input_error_icon.is_displayed()
alert = Alert(driver)
alert.accept()
assert not username_input_error_icon.is_displayed()
assert not password_input_error_icon.is_displayed()

# Web driver'ı kapat
driver.close()
