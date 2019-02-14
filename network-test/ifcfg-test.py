import ifcfg
import json

for name, interface in ifcfg.interfaces().items():
    # do something with interface
    print interface['device']
    print interface['inet']         # First IPv4 found
    print interface['inet4']        # List of ips
    print interface['inet6']
    print interface['netmask']
    print interface['flags']
    #print interface['broadcast']
    print('\n')

default = ifcfg.default_interface()
print(default)
print('\n')
print(ifcfg.interfaces())