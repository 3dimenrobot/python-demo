from  .plugins.disk import  DiskPlugin

from .plugins.mem import MemPlugin

from .plugins.nic import NicPlugin

from  conf import  settings
def pack():
    for k,v in settings.PLUGINS.items():
        # dd = __import__(imp)
        # # 等价于import imp
        # inp_func = input("请输入要执行的函数：")
        # f = getattr(dd, inp_func，None)  # 作用:从导入模块中找到你需要调用的函数inp_func,然后返回一个该函数的引用.没有找到就烦会None
        response[k] = v().execute()


    disk_obj = DiskPlugin()
    disk_info = disk_obj.execute()

    mem_obj = MemPlugin()
    mem_info = mem_obj.execute()

    nic_obj = NicPlugin()
    nic_info = nic_obj.execute()

    response = {
        'nic':nic_info,
        'mem':mem_info,
        'disk':disk_info
    }
    return response