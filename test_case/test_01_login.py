"""
    @ describe:
    @ author:xiaoyue
    @ version:1.0.0
    @ copyright:yue
    @ datetime:2022/8/16 18:42
    
"""
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.helper import get_screen_path

class TestLogin:
    def test_login_01(self,get_driver):
        driver = get_driver
        url = "http://www.baidu.com"
        driver.get(url)
        driver.find_element(By.ID,"kw").send_keys("十万个为什么")
        driver.find_element(By.ID,"su").click()
        driver.find_element(By.XPATH,'//*[@id="1"]/div/section/div[2]/div[1]/div/section[1]/div/div[1]/a[1]/span').click()
        sleep(3)
        driver.get_screenshot_as_file(get_screen_path())
        # ActionChains()