from .base import BasePlugin

class DiskPlugin(BasePlugin):
    def linux(self):
        output = self.shell_cmd('ifconfig')
        # 正则表达式
        return output
    def window(self):
        output = self.shell_cmd('ipconfig')
        # 正则表达式
        return output