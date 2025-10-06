import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from lesson_28.pages.registration_page import RegistrationPage

logging.basicConfig(
    filename="test_log.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    logger.info("Запуск драйвера Chrome")
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    yield driver
    logger.info("Закрытие драйвера")
    driver.quit()


@pytest.fixture
def auth_url():
    username = "guest"
    password = "welcome2qauto"
    base_url = "qauto2.forstudy.space"
    url = f"https://{username}:{password}@{base_url}"
    return url


@pytest.fixture
def open_registration_page(driver, auth_url):
    driver.get(auth_url)
    # нажимаем на кнопку Sign up на главной
    sign_up_btn = driver.find_element("xpath", "//button[text()='Sign up']")
    sign_up_btn.click()
    return driver


@pytest.fixture
def registration_page(driver, open_registration_page):
    return RegistrationPage(driver)
