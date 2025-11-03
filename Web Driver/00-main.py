# from selenium import webdriver


# chrome_driver_path = "/home/sumon/Documents/chromedriver-linux64/chromedriver"

# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("https://www.google.com")
# print(driver.title)
# driver.close()
# driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Optional: set your ChromeDriver path manually
chrome_driver_path = "/home/sumon/Documents/chromedriver-linux64/chromedriver"

service = Service(chrome_driver_path)
options = Options()

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")
print(driver.title)
driver.quit()