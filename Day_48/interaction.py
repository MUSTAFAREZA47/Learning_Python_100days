from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys("Ahmed")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Reza")
email = driver.find_element(By.NAME, "email")
email.send_keys("mustafareza47@gmail.com")
sign_up = driver.find_element(By.CLASS_NAME, "btn-block")
sign_up.click()

driver.quit()

