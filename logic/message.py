import time
from appium.webdriver.common.appiumby import AppiumBy
from device_driver import DeviceDriver


class Message:
    def __init__(self, device: DeviceDriver):
        self.device = device

    def click_messages(self) -> None:
        element = self.device.get_element_with_timeout("com.instagram.android:id/action_bar_inbox_button")
        element.click()

    def click_compose_message(self) -> None:
        element = self.device.get_element_with_timeout(
            '//android.widget.Button[@content-desc="New Message"]',
            by=AppiumBy.XPATH
        )
        element.click()

    def search_recipient(self, username: str) -> None:
        element = self.device.get_element_with_timeout('com.instagram.android:id/recipients_container')
        element.click()

        element = self.device.get_element_with_timeout('com.instagram.android:id/search_edit_text')
        element.send_keys(username)

    def click_search_result(self, username: str) -> None:
        element = self.device.get_element_with_timeout(
            f'//android.widget.TextView[@content-desc="{username}"]',
            by=AppiumBy.XPATH
        )
        element.click()

    def send_message(self, message: str) -> None:
        element = self.device.get_element_with_timeout('com.instagram.android:id/row_thread_composer_edittext')
        element.click()
        element.send_keys(message)

        time.sleep(5)
        element = self.device.get_element_with_timeout('com.instagram.android:id/row_thread_composer_button_send')
        element.click()
