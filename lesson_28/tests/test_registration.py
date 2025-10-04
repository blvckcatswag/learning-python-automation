import random
import string
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)


def random_string(length=6):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length)).capitalize()


def random_email():
    return f"{random_string(5).lower()}@gmail.com"


def random_password(length=10):
    if not (8 <= length <= 15):
        length = 10
    chars = string.ascii_letters + string.digits
    pwd = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
    ]
    pwd += random.choices(chars, k=length - 3)
    random.shuffle(pwd)
    return ''.join(pwd)


def test_registration(open_registration_page, registration_page):
    driver = open_registration_page
    page = registration_page

    name = random_string()
    last_name = random_string()
    email = random_email()
    password = random_password()

    logger.info(f"Тестовые данные: {name} {last_name}, {email}, {password}")

    page.enter_name(name)
    page.enter_last_name(last_name)
    page.enter_email(email)
    page.enter_password(password)
    page.repeat_password(password)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(page.REGISTER_BUTTON)
    )
    page.click_register_button()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/panel/garage")
    )
    assert "/panel/garage" in driver.current_url, "Регистрация не удалась"
