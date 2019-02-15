import nc_debian
import pywifi
import time
import api

class Helper:

    def __init__(self):
        pass

    def AMK2Str(self, cipher, akm = [pywifi.const.AKM_TYPE_NONE]):
        if pywifi.const.AKM_TYPE_WPA in akm or pywifi.const.AKM_TYPE_WPA2 in akm or pywifi.const.AKM_TYPE_WPAPSK in akm or pywifi.const.AKM_TYPE_WPA2PSK in akm:
            return 'WPA/WPA2'
        


class NetworkApi:
    network_config = None
    wifi = None
    def __init__(self):
        self.network_config = nc_debian.DebianNetworkConfig()
        self.wifi = pywifi.PyWiFi()

    def GetInterfaces(self):
        pass

    def SaveConfig(self, iface = api.NetworkInterface()):
        self.network_config.interfaces[iface.name] = iface
        self.network_config.save()

    def Wifis(self):
        wifis = {}
        for iface in self.wifi.interfaces():
            iface.scan()
            # 去重
            profiles = {}
            for profile in iface.scan_results():
                profiles[profile.ssid] = profile
            wifis[iface.name] = profiles.values()
        
        return wifis
        
    ''' '''
    def WifiConnect(self, interface, name, key, akm = pywifi.const.AKM_TYPE_NONE):
        iface = None
        for it in self.wifi.interfaces():
            if it.name == interface:
                iface = it
        if iface == None:
            return False
        profile = pywifi.Profile()  # 创建wifi链接文件
        profile.ssid = name  # wifi名称，不加会报错
        profile.auth = pywifi.const.AUTH_ALG_OPEN  # 网卡的开放
        profile.akm.append(akm)  # wifi加密算法
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # 加密单元
        profile.key = key  # 密码
        iface.remove_all_network_profiles()  # 删除所有的wifi文件
        tmp_profile = iface.add_network_profile(profile)  # 设定新的链接文件
        iface.connect(tmp_profile)  # 链接
        time.sleep(2)

        return iface.status() == pywifi.const.IFACE_CONNECTED

    def WifiDisconnect(self, interface):
        iface = None
        for it in self.wifi.interfaces():
            if it.name == interface:
                iface = it
        if iface == None:
            return
        iface.disconnect()
        time.sleep(1)

