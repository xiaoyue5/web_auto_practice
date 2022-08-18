"""
    @ describe:路径管理工具
    @ author:xiaoyue
    @ version:1.0.0
    @ copyright:yue
    @ datetime:2022/7/14 18:39
    
"""
import os
# 项目路径
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件路径
CONF_PATH = os.path.join(PROJECT_PATH,"conf")
# 数据路径
DATA_PATH = os.path.join(PROJECT_PATH,"datas")
# 日志路径
LOG_PATH = os.path.join(PROJECT_PATH,"logs")
if __name__ == '__main__':
    print(DATA_PATH)