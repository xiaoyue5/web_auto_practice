"""
    @ describe:夹具文件
    @ author:xiaoyue
    @ version:1.0.0
    @ copyright:yue
    @ datetime:2022/8/16 18:31
    
"""
import pytest
from selenium import webdriver


@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
