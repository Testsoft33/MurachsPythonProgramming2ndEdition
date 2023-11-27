# Launch Chrome browser

import time
from selenium import  webdriver

# get chrome webdriver
driver = webdriver.Chrome()
# Launch site http://selium.dev web site
driver.get("http://selenium.dev")
# sleep 5 seconds
time.sleep(5)
driver.get("http://foxnews.com")
# sleep 5 seconds
time.sleep(5)
# quit program
driver.quit()