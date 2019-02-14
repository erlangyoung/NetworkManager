import netifaces

for interface in netifaces.interfaces():
    print(netifaces.ifaddresses(interface))
    print('\n')

print(netifaces.interfaces())