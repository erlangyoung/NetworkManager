# 导入模块
import pywifi
import time
import sys
import chardet


wifis = pywifi.PyWiFi()

count = len(wifis.interfaces())


iface = wifis.interfaces()[0]
# 起始获得的是列表，列表中存放的是无线网卡对象。
# 可能一台电脑有多个网卡，请注意选择

print(iface.name())
print(iface.status())
#print(iface.network_profiles())
profiles = iface.network_profiles()


# 如果网卡选择错了，程序会卡住，不出结果。
ret = iface.scan()
time.sleep(3)

#profile = pywifi.Profile()#配置文件
#profile.ssid="666666"#wifi名称
#profile.auth = pywifi.const.AUTH_ALG_OPEN#需要密码
#profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)#加密类型
#profile.cipher=pywifi.const.CIPHER_TYPE_NONE#加密单元
#profile.key = 'Lskj@123'
##ifaces.remove_all_network_profiles()#删除其他配置文件
#iface.add_network_profile(profile)
#ret = iface.connect(profile)
#time.sleep(10)

#ret = iface.disconnect()
#
#'''连接网络'''
profile = pywifi.Profile()  # 创建wifi链接文件
profile.ssid = '666666'  # wifi名称，不加会报错
profile.auth = pywifi.const.AUTH_ALG_OPEN  # 网卡的开放
profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)  # wifi加密算法
profile.cipher = pywifi.const.CIPHER_TYPE_CCMP  # 加密单元
profile.key = 'Lskj@123'  # 密码
iface.remove_all_network_profiles()  # 删除所有的wifi文件
tmp_profile = iface.add_network_profile(profile)  # 设定新的链接文件
iface.connect(tmp_profile)  # 链接
time.sleep(5)

connectStatus = iface.status() == pywifi.const.IFACE_CONNECTED

print('测试')


result=iface.scan_results()

for i in range(len(result)):
    #print((result[i].ssid).encode(encoding='UTF-8',errors='strict').decode(encoding='UNICODE'), result[i].signal, result[i].auth, result[i].cipher, result[i].akm, result[i].key, result[i].id)
    #print(chardet.detect(result[i].ssid))
    print(type(result[i].ssid))
    #print(str(result[i].ssid).decode("utf-8").encode("GBK","ignore"), result[i].signal, result[i].auth, result[i].cipher, result[i].akm, result[i].key, result[i].id)
#ssid 是名称 ，signal 是信号强度
