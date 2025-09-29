from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")

driver.switch_to.frame("frame1")
driver.find_element(By.ID, "input1").send_keys("Frame1_Secret")
driver.find_element(By.TAG_NAME, "button").click()

alert = driver.switch_to.alert
assert alert.text == "Верифікація пройшла успішно!"
alert.accept()

driver.switch_to.default_content()

driver.switch_to.frame("frame2")
driver.find_element(By.ID, "input2").send_keys("Frame2_Secret")
driver.find_element(By.TAG_NAME, "button").click()

alert = driver.switch_to.alert
assert alert.text == "Верифікація пройшла успішно!"
alert.accept()

driver.quit()
