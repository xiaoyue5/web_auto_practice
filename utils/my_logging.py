"""
    describe:日志工具
    author:xiaoyue
    version:1.0.0
    datetime:2022/7/1 9:32
"""
import os
import datetime
import logging
# 导入日志保存路径
from utils.my_path import LOG_PATH


class MyLogging:
    """
    使用单例模式创建日志文件信息，控制台输出实时信息，并保存到日志文件当中
    """

    def __init__(self, level):
        """

        :param level: 日志等级设置
        """
        # 检查日志保存路径所需要的目录是否存在，不存在则创建。
        log_dir = self.__get_log_dir()
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 获取日志存储位置
        log_save_path = self.__get_save_log_path()
        # 创建日志器
        self.logger = logging.getLogger()
        # logger = logging.Logger("mylog")
        # 设置日志器的处理等级
        self.logger.setLevel(level)
        # 创建日志处理器，并设置编码格式为utf-8
        handler = logging.FileHandler(log_save_path, encoding="utf-8")
        stream_handler = logging.StreamHandler()
        # 将处理器添加到日志器中
        self.logger.addHandler(handler)
        self.logger.addHandler(stream_handler)
        # 设置日志显示格式
        formatter = logging.Formatter("%(asctime)s %(filename)s %(lineno)d %(levelname)s : %(message)s")
        # 设置处理器的日志显示格式
        handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

    def __get_save_log_path(self):
        """
        生成日志保存路径，日志保存名称格式为年月日-时分秒.log
        :return: 日志保存路径
        """
        return os.path.join(self.__get_log_dir(), datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".log")

    def __get_log_dir(self):
        """
        获取日志保存路径所在目录
        :return: 日志保存路径目录
        """
        return os.path.join(LOG_PATH, str(datetime.date.today()))

    def get_logger(self):
        return self.logger


logger = MyLogging(logging.INFO).get_logger()

if __name__ == '__main__':
    logger.debug("debug 错误")
    logger.info("info 错误")
    logger.warning("warning 错误")
    logger.error("error 错误")
    logger.critical("critical 错误")
