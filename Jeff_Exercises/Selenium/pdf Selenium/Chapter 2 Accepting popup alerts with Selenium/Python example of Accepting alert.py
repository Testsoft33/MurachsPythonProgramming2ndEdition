# pdf Selenium Chapter 2
# Python example of Accepting alert
# Examples

from selenium import webdriver

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create a new webdriver
driver = webdriver.Chrome()
# Get a page that has a popup window (Use mouse to to click "try it" button)
driver.get("http://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
# Accept the opened alert
driver.switch_to.alert.accept()



