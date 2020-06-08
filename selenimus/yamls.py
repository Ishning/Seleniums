import os
import yaml

from logs import Logger

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
                dict_var={"Environment": {"env": {"https": "https","DingDingWebHook": "dwebh1"},"env1": {"https": "https","DingDingWebHook": "dwebh2"}},"Username": {"name": "username","psd": "password"}}
                with open(self.file_path,'w',encoding='utf-8') as wf:
                    yaml.dump(dict_var,wf,default_flow_style=False)
                print('已创建文件')
            except OSError:
                pass
        elif isExists:
            try:
                with open(self.file_path,encoding='utf-8') as rf:
                    yamlload=yaml.safe_load(rf)
                    return yamlload
                    print('已读取')
            except OSError:
                pass

a=Selenimu_Yaml().file_judge()

Logger()