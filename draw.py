import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType

desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# 应用参数desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.ChooseLockPattern'

# 获取driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 如果代码过长，可以使用回车进行换行
# 如果代码过长，可以使用回车进行换行
# 换行的时候默认会多一个 右斜线 是正常的
# 如果不希望出现这个 右斜线 可以将整句代码用括号括起来，然后再使用回车换行即可238 853  718

(TouchAction(driver).press(x=244, y=856).move_to(x=480, y=0)
 .move_to(x=480, y=0).move_to(x=0, y=480)
 .move_to(x=-480, y=0).move_to(x=-480, y=0)
 .move_to(x=480, y=480).release().perform())

TouchAction.tap()

driver.tap()
yuanzhoulv = 3.14159
time.sleep(10)
driver.quit()