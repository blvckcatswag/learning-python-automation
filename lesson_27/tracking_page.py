from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TrackingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open(self):
        self.driver.get(self.url)

    def enter_tracking_number(self, tracking_number):
        field = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        field.clear()
        field.send_keys(tracking_number)
        field.send_keys(Keys.RETURN)

    def get_status(self):
        try:
            status_el = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
            )
            return status_el.text
        except:
            return "Статус не знайдено"
