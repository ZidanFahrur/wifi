import json,os
os.system("termux-wifi-connectioninfo > /dev/null > wifi.json")
op = open("wifi.json","r").read()
j = json.loads(str(op))
print ("[+] WIFI INFO [+]")
print ("copyright 2019 TigerPo")
print ("=======================")
print ("BSSID: %s"%(j["bssid"]))
print ("Frequency mhz : %s"%(j["frequency_mhz"]))
print ("Speed: %s"%(j["link_speed_mbps"]))
print ("Network ID: %s"%(j["network_id"]))
print ("RSSI: %s"%(j["rssi"]))
print ("SSID: %s"%(j["ssid"]))
print ("SSID HIDDEN: %s"%(j["ssid_hidden"]))
print ("Wifi IP: %s"%(j["ip"]))
print ("Status: %s"%(j["supplicant_state"]))
