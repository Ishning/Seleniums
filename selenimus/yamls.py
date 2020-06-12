import os
import yaml

from loggings import Loggingyaml

loggs=Loggingyaml().loggerin()

class Selenimu_Yaml(object):
    def __init__(self,
    fileyamlname='traffic.yaml'):
        self.fileyamlname=fileyamlname
        self.folder_name=r'./'

        self.file_path=self.folder_name+self.fileyamlname
    
    @property
    def file_judge(self):
        isExists=os.path.exists(self.fileyamlname)
        if not isExists:
            try:
                dict_var={"Environment": {"Env": {"Https": "https1","DingDingWebHook": "dwebh1","Title":"This is an example"},"Env1": {"Https": "https2","DingDingWebHook": "dwebh2","Title":"This is an example"}},"Username": {"name": "username","pw": "password"}}
                with open(self.file_path,'w',encoding='utf-8') as wf:
                    yaml.dump(dict_var,wf,default_flow_style=False)
                loggs.info('已创建默认配置文件，请修改')
            except BaseException as be:
                loggs.error(be)
        elif isExists:
            try:
                with open(self.file_path,encoding='utf-8') as rf:
                    yamlload=yaml.safe_load(rf)
                loggs.debug('已读取traffic.yaml')
                return yamlload
            except BaseException as be:
                loggs.error(be)
    