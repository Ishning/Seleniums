import os
import yaml

from logs import Loggingyaml

# logs=Loggingyaml().loggerin()

class Selenimu_Yaml(object):
    def __init__(self,
    fileyamlname='traffic.yaml'):
        self.fileyamlname=fileyamlname
        self.folder_name=r'./'

        self.file_path=self.folder_name+self.fileyamlname
    
    def file_judge(self):
        isExists=os.path.exists(self.fileyamlname)
        if not isExists:
            try:
                dict_var={"Environment": {"env": {"https": "https1","DingDingWebHook": "dwebh1"},"env1": {"https": "https2","DingDingWebHook": "dwebh2"}},"Username": {"name": "username","pw": "password"}}
                with open(self.file_path,'w',encoding='utf-8') as wf:
                    yaml.dump(dict_var,wf,default_flow_style=False)
                # logger.info('已创建traffic.yaml')
            except OSError:
                pass
        elif isExists:
            try:
                with open(self.file_path,encoding='utf-8') as rf:
                    yamlload=yaml.safe_load(rf)
                # logs.debug('已读取traffic.yaml')
                return yamlload
            except OSError:
                pass
    