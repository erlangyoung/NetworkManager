#import sys
#from os.path import abspath, join, dirname
#sys.path.append(join(abspath(dirname(dirname(__file__))), 'network-core'))

import network_api

def PrintInterfaces(interfaces):
    for ifac in interfaces.values():
        print('name:' + ifac.name)
        print('up:' + str(ifac.up))
        print('devclass:' + ifac.devclass)
        print('type:' + ifac.type)
        print('addressing:' + ifac.addressing)
        for param_key, param_value in ifac.params.items():
            print(param_key + ':' + param_value)
        print('\n')

networapi = network_api.NetworkApi()
interfaces = networapi.GetInterfaces()
print(interfaces)
PrintInterfaces(interfaces)