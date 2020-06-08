import os
import os.path
import time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from logs import Loggingyaml
from yamls import Selenimu_Yaml

logs=Loggingyaml().loggerin()

default_yaml=Selenimu_Yaml().file_judge()

def useyamls():
    Environment=default_yaml['Environment']
    for i in range(0,len(Environment)+1):
        envs=list(Environment.keys())[i]
        env_info=Environment[envs]
        webdrivers(env_info['https'],default_yaml['Username'])
        print(i)


def webdrivers(infos,userinfo):
    # chrome模式
    chromedriver_path=r''
    
    chrome_options=Options()
    #无界面模式
    chrome_options.add_argument('headless')

    drivers=webdriver.Chrome(chromedriver_path,chrome_options=chrome_options)
    drivers.get(infos)

    # safari测试
    # driver=webdriver.Safari()
    # driver.get("")
    
    username=driver.find_element_by_name('username')
    username.send_keys(userinfo['name'])
    password=driver.find_element_by_id('inputPassword')
    password.send_keys(userinfo['pw'])
    driver.find_element_by_id('inputPassword').send_keys(Keys.ENTER)

    time.sleep(5)

    times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    screnhost_name='%a-%s.png' % times
    driver.save_screenshot(screnhost_name)


useyamls()

print('😀😃')