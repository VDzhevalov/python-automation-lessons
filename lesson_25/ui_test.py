from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

sign_up_button_by_class_name = driver.find_element(By.CLASS_NAME, "header_signin")




#XPATH локатори
#пошук за атрибутом @
about_button = driver.find_element(By.XPATH, "//button[@appscrollto='aboutSection']")

#Використовувати функцію text()
contacts_button = driver.find_element(By.XPATH, "//button[text()='Contacts']")

#Варіант з normalize-space() мені більш подобається при пошуку по тексту
home_button = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
guest_login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Guest log in']")
# складні локатори (більш ніж з одним елементом)
sign_up_button = driver.find_element(By.XPATH, "//div[contains(@class,'header_right')]/button[2]")

#CSS локатори
sign_up_button_by_css_selector = driver.find_element(By.CSS_SELECTOR,"button.header_signin")
sign_up_button_by_css_selector = driver.find_element(By.CSS_SELECTOR,"button[class$='header_signin']")

# складні локатори (більш ніж з одним елементом)
sign_in_button_by_complex_css_selector = driver.find_element(By.CSS_SELECTOR, "div.header_right button.header_signin")


guest_login_button.click()
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "expenses"))
)

driver.quit()