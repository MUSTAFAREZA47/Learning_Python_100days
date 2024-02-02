# https://selenium-python.readthedocs.io/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Keep Chrome browser open after programe finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Cosco-Acclaim-Volley-Ball-4/dp/B00ID6OVGM/?_encoding=UTF8&pd_rd_w=DBf8F&content-id=amzn1.sym.44901b9b-bd56-4240-8b6b-3ad72079fb43%3Aamzn1.symc.adba8a53-36db-43df-a081-77d28e1b71e6&pf_rd_p=44901b9b-bd56-4240-8b6b-3ad72079fb43&pf_rd_r=VT4WN1KP3PA8KMQ4SZVD&pd_rd_wg=BUD1n&pd_rd_r=36929b52-7c58-44bd-9a16-03936e9103f6&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

# driver.close()
driver.quit()

# Deprecated - no longer needed
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    title = driver.title
    assert title == "Web form"
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    # Closes Chrome
    # driver.quit()
    driver.close()


test_eight_components()

