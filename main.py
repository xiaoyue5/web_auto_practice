"""
    @describe:主文件
    @author:xiaoyue
    @version:1.0.0
    @copyright:无
    @datetime:2022/7/8 18:35
"""
import pytest
import os

# import allure
# -v 显示执行过程
# --clean-alluredir 清除执行目录
# "--alluredir=./allure_result" 指定执行目录 目录可以任意指定 ./allure_result
# 注意：需要安装的包 pytest  pytest-html allure-pytest
from utils.my_remove_dir import remove_dir
path = "./output/report"
remove_dir(path)

pytest.main(["-v","--clean-alluredir","--alluredir=./allure_result"])
# 使用cmd命令生成执行结果报告

os.system('allure generate ./allure_result -o ./output/report')
