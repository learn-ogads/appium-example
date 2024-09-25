from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DeviceDriver:
    def __init__(self, client_server: str, capabilities: dict):
        self.driver = webdriver.Remote(
            client_server,
            options=self._build_options(capabilities)
        )

    def get_element_with_timeout(self, text: str, timeout=15, by=AppiumBy.ID) -> WebElement:
        """
        Look for and wait for the specified element.
        If found, return it.
        :raises TimeoutException: The element wasn't found within the specific timeout
        """
        element = WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable((by, text)))
        return element

    def quit(self) -> None:
        """
        Used for closing the Appium instance with the device.
        Make sure to call it to clean up!
        """
        self.driver.quit()

    @staticmethod
    def _build_options(caps: dict[str, any]) -> UiAutomator2Options:
        """
        Used for building options for a UiAutomator.
        Specify the application, and device information.
        Note: Additional device information may be required.
        """
        options = UiAutomator2Options()
        options.load_capabilities(caps)
        return options
