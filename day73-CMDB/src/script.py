# 采集资产：三种不同的形式

from conf import settings
class BasePlugin(object):

    def __init__(self):
        mode_list = ['SSH','Salt','Agent']
        if settings.MODE in mode_list:
            self.mode = settings.MODE;
        else:
            raise  Exception('模式不存在')

    def ssh(self,cmd):
        pass

    def salt(self,cmd):
        pass

    def subp(self,cmd):
        pass

    def shell_cmd(self,cmd):
        if self.mode == 'SSH':
            ret = self.ssh("")
        elif self.mode == 'Salt':
            ret = self.salt("")
        else:
            ret = self.subp("")

        return ret

    def execute(self):
        # 判断平台
        # agent模式
        # import subprocess
        # subprocess.getoutput("")

        # ssh 模式

        # saltstack 模式

        ret = self.shell_cmd("查看平台的命令")

        if ret == 'win':
          return self.window()
        elif ret == 'linux':
          return self.linux()
        else:
            raise  Exception('只支持windows和linux')


    def linux(self):
        raise  Exception('....')
    def window(self):
        raise Exception('.....')

class DiskPlugin(BasePlugin):
    def linux(self):
        output = self.shell_cmd('ifconfig')
        # 正则表达式
        return output
    def window(self):
        output = self.shell_cmd('ipconfig')
        # 正则表达式
        return output

obj = DiskPlugin()
obj.execute()