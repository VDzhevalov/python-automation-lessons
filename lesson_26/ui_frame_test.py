from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://localhost:8000/dz.html")
    wait = WebDriverWait(driver, 5)

    frame_data = [
        {"id": "frame1", "input_id": "input1", "secret": "Frame1_Secret"},
        {"id": "frame2", "input_id": "input2", "secret": "Frame2_Secret"}
    ]

    for frame in frame_data:
        driver.switch_to.frame(driver.find_element(By.ID, frame["id"]))

        input_elem = wait.until(EC.presence_of_element_located((By.ID, frame["input_id"])))
        input_elem.clear()
        input_elem.send_keys(frame["secret"])

        driver.find_element(By.TAG_NAME, "button").click()

        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text

        assert alert_text == "Верифікація пройшла успішно!", \
            f"Неочікуваний текст алерта: {alert_text}"
        print(f"[OK] {frame['id']} → {alert_text}")

        alert.accept()

        driver.switch_to.default_content()

finally:
    driver.quit()