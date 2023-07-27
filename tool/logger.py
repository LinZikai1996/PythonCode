import logging
import os
import time
import shutil
from logging.handlers import RotatingFileHandler

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Logger(object):

    def __init__(self):
        # 文件的命名
        self.logFileName = os.path.join(log_path, 'application-%s.log' % time.strftime('%Y-%m-%d'))
        self.logger = logging.getLogger(self.logFileName)
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(levelname)s: %(message)s')

        if not self.logger.hasHandlers():
            # 创建一个RotatingFileHandler，用于写到本地，最大文件大小为1GB，最多保留5个文件
            fh = RotatingFileHandler(self.logFileName, 'a', maxBytes=1 << 30, backupCount=5, encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(self.formatter)
            self.logger.addHandler(fh)

            # 创建一个StreamHandler,用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(self.formatter)
            self.logger.addHandler(ch)

    def __console(self, level, message):
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

    def rotate_logs(self):
        list_of_files = filter(os.path.isfile, os.listdir(log_path))
        sorted_files = sorted(list_of_files, key=os.path.getmtime)
        while self.get_dir_size(log_path) > 5 * 1024 * 1024 * 1024:  # 5GB
            if len(sorted_files) > 0:
                os.remove(sorted_files.pop(0))

    def get_dir_size(self, path='.'):
        total = 0
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                total += os.path.getsize(full_path)
            elif os.path.isdir(full_path):
                total += self.get_dir_size(full_path)
        return total

    def debug(self, message):
        self.rotate_logs()
        self.logger.debug(message)

    def info(self, message):
        self.rotate_logs()
        self.logger.info(message)

    def warning(self, message):
        self.rotate_logs()
        self.logger.warning(message)

    def error(self, message):
        self.rotate_logs()
        self.logger.error(message)
