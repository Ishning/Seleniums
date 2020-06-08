import os
import os.path

from selenium import webdriver

from yamls import Selenimu_Yaml
from logs import Loggingyaml

logs=Loggingyaml().loggerin()

Selenimu_Yaml().file_judge()
logs.debug('debug')