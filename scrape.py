import selenium

from selenium import webdriver

address = "https://blackboard.boisestate.edu/"

username = ""

password = ""

driver = webdriver.Chrome()

url = driver.get(address)

username = driver.find_element_by_id("user_id")

username.clear()

username.send_keys(username)

password = driver.find_element_by_id("password")

password.clear()

password.send_keys(password)

login_button = driver.find_element_by_id("entry-login")

login_button.click()
