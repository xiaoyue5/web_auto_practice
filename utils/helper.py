"""
    @ describe:工具类
    @ author:xiaoyue
    @ version:1.0.0
    @ copyright:yue
    @ datetime:2022/8/16 18:27
    
"""
import os
import re
from datetime import datetime

from utils.my_logging import logger
from utils.my_path import PROJECT_PATH
from utils.my_mysql import MyMysql
import faker


def get_new_phone():
    """获取新的电话号码，验证数据库中是否存在该号码"""
    phone = None
    while True:
        phone = faker.Faker("zh_CN").phone_number()
        sql = f"select phone from test_phone where phone = {phone}"
        my_mysql = MyMysql()
        execute = my_mysql.execute(sql)
        if len(execute) == 0:
            break
    return phone


def get_old_phone():
    """获取旧的电话号码，从数据库中直接获取"""
    sql = "select phone from test_phone"
    my_mysql = MyMysql()
    execute = my_mysql.execute(sql)
    return execute[0].get("phone")


def my_replace(dict_replace):
    """字符替换"""
    str_replace = str(dict_replace)
    re_pattern = "#(\w+?)#"
    re_findall_list = re.findall(re_pattern, str_replace)
    for re_one in re_findall_list:
        if re_one.lower() == "phone":
            new_phone = get_new_phone()
            str_replace = str_replace.replace("#phone#", new_phone)
        if re_one.lower() == "old_phone":
            old_phone = get_old_phone()
            str_replace = str_replace.replace("#old_phone#", old_phone)
    return eval(str_replace)


def remove_dir(path):
    """
    删除指定路径文件夹下的所有数据
    :param path: 要删除的文件夹路径
    :return:None
    """
    result = os.path.exists(path)
    if result:
        listdir = os.listdir(path)
        for dir_temp in listdir:
            current_path = os.path.join(path, dir_temp)
            if os.path.isdir(current_path):
                remove_dir(current_path)
                os.rmdir(current_path)
            else:
                os.remove(current_path)


def get_screen_path():
    """"""
    png_path = os.path.join(PROJECT_PATH,"pngs")
    if not os.path.exists(png_path):
        os.makedirs(png_path)
    now__strftime = datetime.now().strftime("%Y%m%d-%H%M%S")
    name = now__strftime+".png"
    png_path = os.path.join(png_path,name)
    return png_path
