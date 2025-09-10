from selenium import webdriver
from selenium.webdriver.common.by import By


# ----- KEEP CHROME OPEN ----- #
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# ----- OPEN BROWSER ----- #
URL = 'https://www.sportline.com.do/nike-air-force-1-07-cw2288-111-zapatillas-casual.html'

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# product_title = driver.find_element(By.ID, value='price')
price_dollar = driver.find_element(By.CLASS_NAME, value='price')
price_cents = driver.find_element(By.CLASS_NAME, value='page-title')

print(price_dollar.text)
print(price_cents.text)
# driver.quit() # - Close the browser
# driver.close() # - Just close 1 tab


