"""
    @ describe:
    @ author:xiaoyue
    @ version:1.0.0
    @ copyright:yue
    @ datetime:2022/8/15 14:12
    
"""
import configparser
from utils.my_logging import logger

class MyConf(configparser.ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        try:
            self.read(file_path)
        except Exception as e:
            logger.info(e)