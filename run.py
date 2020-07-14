import os
import sys
import click

from selenimus import loggings
from selenimus import selenimu

logs=loggings.Loggingyaml()
largv=list(sys.argv)
# print(len(largv))

def main():
    # if len(largv)==1:
    #     print('-s 启动运行\n-t 检查')
    #     return None
    
    # if len(largv)>1 and largv[1]=='-s':
    #     print('-h 查看帮助\n-c 启用chrome模式\n-s 启用safari模式')
    #     return None

    # if len(largv)==3 and largv[2]=='-c':
    #     print('启动')
    #     try:
    #         selenimu.webdrivers('-c').starts
    #         # return None
    #     except BaseException as oser:
    #         logs.error(oser)

    # if len(largv)==3 and largv[2]=='-s':
    #     print('启动')
    #     try:
    #         selenimu.webdrivers('-s').starts
    #         # return None
    #     except BaseException as oser:
    #         logs.error(oser)

    @click.command()
    @click.option('-s',help="start selemimus",default='-s')
    @click.option('-t',help='检查',default=None)
    def test():
        print('test')

    if len(largv)==1:
        print('-s 启动运行\n-t 检查')
    elif len(largv)>1 and largv[1]=='-s':
        if len(largv)==3 and largv[2]=='-c':
            print('启动')
            try:
                selenimu.webdrivers('-c').starts
                return None
            except BaseException as oser:
                logs.error(oser)
        elif len(largv)==3 and largv[2]=='-s':
            print('启动')
            try:
                selenimu.webdrivers('-s').starts
                return None
            except BaseException as oser:
                logs.error(oser)
        print('-h 查看帮助\n-c 启用chrome模式\n-s 启用safari模式')
    else:
        print('-h 查看帮助')
        
if __name__ == "__main__":
    main()