import os
import sys

from selenimus import loggings
from selenimus import selenimu

logs=loggings.Loggingyaml()
largv=list(sys.argv)

try:
    selenimu.webdrivers('-s').starts
except BaseException as be:
    print(be)

def main():
    if len(largv)==1:
        print('-s 启动运行\n-t 检查')
    elif len(largv)>1 and largv[1]=='-s':
        print('-h 查看帮助\n-c 启用chrome模式\n-s 启用safari模式')
        if len(largv)==3 and largv[2]=='-c':
            print('启动')
            try:
                selenimu.webdrivers('-c').starts
            except BaseException as oser:
                logs.error(oser)
        elif len(largv)==3 and largv[2]=='-s':
            print('启动')
            try:
                selenimu.webdrivers('-s').starts
            except BaseException as oser:
                logs.error(oser)
    else:
        print('-h 查看帮助')
        
# if __name__ == "__main__":
    # main()