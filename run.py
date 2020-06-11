import getopt
import os
import sys

from selenimus import loggings
from selenimus import selenimu

print('start')
logs=loggings.Loggingyaml()

largv=list(sys.argv)
sys.path

def main():
    if len(largv)==1:
        print('-s 启动运行\n-t 检查')
    elif len(largv)>1 and largv[1]=='-s':
        print('启动')
        try:
            selenimu.useyamls()
        except BaseException as oser:
            logs.error(oser)
    else:
        print('-h 查看帮助')
        
if __name__ == "__main__":
    main()