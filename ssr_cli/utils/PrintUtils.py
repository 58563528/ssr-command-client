'''
@Author: tyrantlucifer
@E-mail: tyrantlucifer@gmail.com
@Date: 2020/12/6 下午6:24
'''

import qrcode
from prettytable import PrettyTable
from colorama import init, Fore

class DrawInfoListTable(object):
    '''
    生成打印ssr节点信息表格工具类
    '''
    def __init__(self):
        self.table = []
        header = [
            "id",
            "name",
            "delay(ms)",
            "connect",
            "server",
            "port",
            "method"
        ]
        self.x = PrettyTable(header)
        self.x.reversesort = True

    def append(self,*args,**kwargs):
        if(kwargs):
            content=[
                kwargs['id'],
                kwargs['name'],
                kwargs['delay'],
                kwargs['connect'],
                kwargs['server'],
                kwargs['port'],
                kwargs['method']
            ]
            self.x.add_row(content)

    def str(self):
        return str(self.x)

    def print(self):
        print(self.str())

class DrawSpeedTable(object):
    '''
    生成ssr测速信息表格工具类
    '''
    def __init__(self):

        self.table = []
        header = [
            "id",
            "name",
            "download(MB/s)",
            "upload(MB/s)",
            "server",
            "port",
            "method"
        ]
        self.x = PrettyTable(header)
        self.x.reversesort = True

    def append(self,*args,**kwargs):
        if(kwargs):
            content=[
                kwargs['id'],
                kwargs['name'],
                kwargs['download'],
                kwargs['upload'],
                kwargs['server'],
                kwargs['port'],
                kwargs['method'],
            ]
            self.x.add_row(content)

    def str(self):
        return str(self.x)

    def print(self):
        print(self.str())

class Colored(object):
    '''生成不同颜色字体工具类'''
    def __init__(self):
        init(autoreset=False)

    def red(self,s):
        return Fore.LIGHTRED_EX + s + Fore.RESET

    def green(self,s):
        return Fore.LIGHTGREEN_EX + s + Fore.RESET

    def yellow(self,s):
        return Fore.LIGHTYELLOW_EX + s + Fore.RESET

    def white(self,s):
        return Fore.LIGHTWHITE_EX + s + Fore.RESET

    def blue(self,s):
        return Fore.LIGHTBLUE_EX + s + Fore.RESET

    def print(self, text, color):
        if color == 'red':
            print(self.red(text))
        if color == 'green':
            print(self.green(text))
        if color == 'yellow':
            print(self.yellow(text))
        if color == 'white':
            print(self.white(text))
        if color == 'blue':
            print(self.blue(text))

class PrintQrcode(object):

    def __init__(self):
        pass

    @staticmethod
    def print_qrcode(string):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=1,
        );
        qr.add_data(string)
        qr.make(fit=True)
        qr.print_ascii(tty=True, invert=True)
