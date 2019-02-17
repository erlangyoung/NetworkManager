class INetworkConfig (object):
    interfaces = {}

    @property
    def interface_list(self):
        return self.interfaces.values()

    def rescan(self):
        pass

    def save(self):
        pass


class INetworkConfigBit (object):
    def apply(self):
        pass

class NetworkInterface(object):
    def __init__(self):
        self.up = False
        self.auto = False
        self.name = ''
        self.devclass = ''
        self.addressing = 'static'
        self.bits = []
        self.params = {'address': '0.0.0.0'}
        self.type = ''
        self.editable = True

    def __getitem__(self, idx):
        if idx in self.params:
            return self.params[idx]
        else:
            return ''

    def __setitem__(self, idx, val):
        self.params[idx] = val
