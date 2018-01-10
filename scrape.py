import selenium

from selenium import webdriver

address = "https://blackboard.boisestate.edu/"

username = ""

password = ""

driver = webdriver.Chrome()

url = driver.get(address)

username_field = driver.find_element_by_id("user_id")

username_field.clear()

username_field.send_keys(username)

password_field = driver.find_element_by_id("password")

password_field.clear()

password_field.send_keys(password)

login_button = driver.find_element_by_id("entry-login")

login_button.click()
