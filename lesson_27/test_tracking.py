import pytest
from tracking_page import TrackingPage
from driver import get_driver

class TestNovaPoshtaTracking:
    def setup_method(self):
        self.driver = get_driver()
        self.tracking_page = TrackingPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_valid_tracking(self):
        tracking_number = "5900089085747"  # подставь реальный номер
        expected_status = "Посилка отримана"

        self.tracking_page.open()
        self.tracking_page.enter_tracking_number(tracking_number)
        actual_status = self.tracking_page.get_status()

        assert actual_status == expected_status, \
            f"Очікували: {expected_status}, Отримали: {actual_status}"

    def test_invalid_tracking(self):
        tracking_number = "123456789"

        self.tracking_page.open()
        self.tracking_page.enter_tracking_number(tracking_number)
        actual_status = self.tracking_page.get_status()

        assert "не знайдено" in actual_status.lower(), \
            f"Очікувалось повідомлення про відсутність статусу, отримали: {actual_status}"
