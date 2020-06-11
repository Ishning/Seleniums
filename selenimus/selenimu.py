import os
import os.path
import time
import sys

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from loggings import Loggingyaml
from yamls import Selenimu_Yaml

logs=Loggingyaml().loggerin()

default_yaml=Selenimu_Yaml().file_judge()

def useyamls():
    try:
        Environment=default_yaml['Environment']
    except (TypeError,OSError,ValueError) as errinfo:
        logs.error(errinfo)
        logs.info('配置未正确，已退出。请确认配置后运行')
        sys.exit(0)
    
    for i in range(0,len(Environment)):
        envs=list(Environment.keys())[i]
        env_info=Environment[envs]
        webdrivers(envs,env_info['Https'],default_yaml['Username'])

def directory():
    floder=r'./Screenshots'
    isExists=os.path.exists(floder)
    if not isExists:
        try:
            os.mkdir(floder)
        except BaseException as be:
            logs.error(be)
    return floder

def webdrivers(envs,infos,userinfo):
    # chrome模式
    # chromedriver_path=r''
    
    # chrome_options=Options()
    # #无界面模式
    # chrome_options.add_argument('headless')

    # drivers=webdriver.Chrome(chromedriver_path,chrome_options=chrome_options)
    # drivers.get(infos)

    # safari测试
    drivers=webdriver.Safari()
    try:
        drivers.get(infos)
    except BaseException as be:
        logs.error('网址错误，请确认.%s',be)
        drivers.close()
        return None
    
    #键入用户名和密码
    try:
        username=drivers.find_element_by_name('username')
        username.send_keys(userinfo['name'])
        password=drivers.find_element_by_id('inputPassword')
        password.send_keys(userinfo['pw'])
        drivers.find_element_by_id('inputPassword').send_keys(Keys.ENTER)

        time.sleep(5)
    except BaseException as be:
        logs.error('selenium.common.exceptions.NoSuchElementException:%s,未能找到相关页面元素，只截当前图',be)
    # username=drivers.find_element_by_name('username')
    # username.send_keys(userinfo['name'])
    # password=drivers.find_element_by_id('inputPassword')
    # password.send_keys(userinfo['pw'])
    # drivers.find_element_by_id('inputPassword').send_keys(Keys.ENTER)

    #设置大小
    width=drivers.execute_script('return document.documentElement.scrollWidth')
    height=drivers.execute_script('return document.documentElement.scrollHeight')
    drivers.set_window_size(width,height)
    time.sleep(1)

    times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    screnhost_name='%s-%s.png' % (envs,times)
    logs.info('已获取截图:%s',screnhost_name)
    
    directorys=directory()

    abc=r'%s/%s-%s.png' % (directory(),envs,times)
    drivers.save_screenshot(abc)
    # drivers.get_screenshot_as_file(abc)
    drivers.close()


# try:
    # useyamls()
# except BaseException as oser:
#     logs.error(oser)
