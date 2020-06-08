import os
import logging
import time
import yaml

from logging import handlers

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

# logger=Logger(filename='test.log',level='DEBUG').getlogger()
# while True:
#     logger.debug('😊')
#     time.sleep(1)
#     logger.info('ABC')