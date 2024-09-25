import time
from device_driver import DeviceDriver
from logic.message import Message

if __name__ == '__main__':
    caps = {
        'platformName': 'Android',
        'appPackage': 'com.instagram.android',
        'appActivity': 'com.instagram.mainactivity.InstagramMainActivity',
        'automationName': 'UiAutomator2',
        'platformVersion': '11',
        'noReset': True,
        'forceAppLaunch': True,
    }
    device = DeviceDriver('http://192.168.4.20:4723/wd/hub', caps)

    target = ''  # Provide the username to target
    message = Message(device)
    message.click_messages()
    message.click_compose_message()
    message.search_recipient(target)
    message.click_search_result(target)
    message.send_message("Hello!")

    print('Finished running the account')
    time.sleep(10)
    device.quit()
