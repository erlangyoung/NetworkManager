import sys
from os.path import abspath, join, dirname
#sys.path.append('/home/yang/Projects/NetworkManager/network-core')
#sys.path.append('/home/yang/Projects/NetworkManager')
#sys.path.insert(0, join(abspath(dirname(dirname(__file__))), 'network-core'))
#print(sys.path)


import nc_debian

def PrintInterfaces(interfaces):
    for ifac in interfaces.values():
        print(ifac.name)
        print(ifac.up)
        print(ifac.devclass)
        print(ifac.type)
        print(ifac.addressing)
        for param_key, param_value in ifac.params.items():
            print(param_key + ':' + param_value)
        print('\n')


network_config = nc_debian.DebianNetworkConfig()
interfaces = network_config.interfaces
PrintInterfaces(interfaces)
print('\n')
print(interfaces)
#
#op_ifac = None
#for ifac in interfaces.values():
#    if ifac.name == 'ens33':
#        op_ifac =ifac
#        for param_key, param_value in ifac.params.items():
#            if param_key == 'address':
#                ifac.params[param_key] = '192.168.1.20'
#
#network_config.save()
#network_config.rescan()
#
#PrintInterfaces(interfaces)
#network_config.down(op_ifac)
#network_config.up(op_ifac)