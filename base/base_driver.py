#fileName:base_driver.py
from appium import webdriver
#函数功能：封装了前置代码，并返回driver对象
def init_driver():
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = '192.168.164.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.jym.mall' #交易猫app
    desired_caps['appActivity'] = '.home.HomeActivity'
    desired_caps['noReset'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
