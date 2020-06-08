import os
import logging
import time
import yaml

from logging import handlers
from logging import config

#内建logging配置
class Logger:
    _logger_level={
        'DEBUG':logging.DEBUG,
        'INFO':logging.INFO,
        'WARNING':logging.WARNING,
        'ERROR':logging.ERROR,
        'CRITICAL':logging.CRITICAL
    }

    def __init__(self,
        filename='default.log',
        level='DEBUG',
        logger=None):

        self._logger=logging.getLogger(logger)
        self._logger.setLevel(self._logger_level.get(level))

        self._log_time=time.strftime('_%Y-%m-%d')
        self._folder_name=r'./log'
        isExists=os.path.exists(self._folder_name)
        if not isExists:
            try:
                os.mkdir(self._folder_name)
            except OSError:
                pass
        else:
            print('目录已存在')
        self._filename=filename
        self._log_name=self._folder_name+'/'+self._filename

        fh=handlers.TimedRotatingFileHandler(filename=self._log_name,when='MIDNIGHT',interval=1,backupCount=30)
        fh.setLevel(self._logger_level.get(level))

        sh=logging.StreamHandler()
        sh.setLevel(self._logger_level.get(level))

        formatter=logging.Formatter('[%(levelname)s] - %(asctime)s - %(name)s - %(pathname)s[line:%(lineno)d] : %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        #给logger添加Handler
        self._logger.addHandler(fh)
        self._logger.addHandler(sh)
        
        # self._logger.removeHandler(fh)
        # self._logger.removeHandler(sh)
        # fh.close()
        # sh.close()

    def getlogger(self):
        return self._logger

#使用配置文件配置日志
class Loggingyaml(object):
    def __init__(self,
    default_name='logging_config.yaml',
    default_folder=r'./'):
        self.default_path=default_folder+default_name

    def loggerin(self):
        with open(self.default_path,'r',encoding='utf-8') as lgo:
            logging_config=yaml.safe_load(lgo)
        logging.config.dictConfig(logging_config)
        logger=logging.getLogger('app')
        return logger
            
# logb=Loggingyaml().loggerin()
# logb.debug('这是一条debug日志')
# logb.info('info日志')