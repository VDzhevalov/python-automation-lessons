from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://UserName:Password@qauto2.forstudy.space")

home_button = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Guest log in']")

driver.quit()