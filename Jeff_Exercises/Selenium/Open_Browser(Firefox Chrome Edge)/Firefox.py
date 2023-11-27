import time

from selenium import  webdriver

driver = webdriver.Firefox()

driver.get("http://selenium.dev")

time.sleep(5)

driver.quit()


