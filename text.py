from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(5)

IsComlete = False
try:
    while(not IsComlete):
        driver.get("https://twitter.com/login")

        try:
            email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")))
            email = driver.find_element_by_xpath("//input[@name='session[username_or_email]']")
            email.send_keys("eureq631@gmail.com")
        except(TimeoutException):
            continue
        finally:
            IsComlete = True

        try:
            password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")))
            password = driver.find_element_by_xpath("//input[@name='session[password]']")
            password.send_keys("ask me for this")
        except(TimeoutExceptoin):
            continue
        finally:
            IsComlete = True

        try:
            sing_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")))
            sing_in_button = driver.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']")
            sing_in_button.click()
        except(TimeoutException):
            continue
        finally:
            IsComlete = True
except(Exception):
    print(Exception)