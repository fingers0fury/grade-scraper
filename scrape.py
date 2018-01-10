import selenium

from selenium import webdriver

import time

import bs4

from bs4 import BeautifulSoup

import requests


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

time.sleep(1.0)

databases = driver.find_element_by_link_text("Sp18 - CS 410/510 - Databases")
databases.click()
my_grades = driver.find_element_by_link_text("My Grades")
my_grades.click()

time.sleep(1.0)

r = requests.get("http://" + driver.current_url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

grades = soup.find("div", {"id", "grades_wrapper"})

print(grades)

driver.close()
