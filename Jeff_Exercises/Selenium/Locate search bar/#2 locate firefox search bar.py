# from: https://www.bing.com/search?pc=U523&q=python+selenium+find+google+search+box&form=U523DF
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://www.google.com")
search = driver.find_element(By.CLASS_NAME,"gLFyf")
search.send_keys("selenium")
search.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()