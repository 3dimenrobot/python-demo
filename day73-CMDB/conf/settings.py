MODE='Agent' # 'SSH' ,'Salt'

PLUGINS = {
    'disk':'src.plugins.disk.DiskPlugin',
    'mem':'src.plugins.mem.MemPlugin',
    'nic':'src.plugins.nic.NicPlugin'
}