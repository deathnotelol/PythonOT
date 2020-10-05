#!/usr/bin/python3
# Wifi Hotspot enabler

import os
os.system('cls')
print('\n\n\n\n')
print('Death Note WiFi Hotspot Enabler')
print('(c) 2020 Death Note. All right reserved.')
print ()

ssid = 'Test'
password = '12345678'
cmd='o'
while cmd != '3':
    print ('1-Start Hotspot')
    print ('2-Stop Hotspot')
    print ('3-Exit')
    cmd = input ('Please Enter Your Choice (1,2,3): ')
    if cmd == '1':
        print('Starting WiFi Hotspot........')
        ssid = input('Please Enter SSID: ')
        password = input('Please Enter Password: ')
        os.system("netsh wlan set hostednetwork mode=allow ssid=" + ssid + " key=" + password)
        os.system('netsh wlan start hostednetwork')
    elif cmd == '2':
        print('Stopping WiFi Hotspot........')
        os.system('netsh wlan stop hostednetwork')
    elif cmd == '3':
        print('Exiting Program........')
        exit()
    else:
        print ("Bad input! Please try again (Only 1,2,3)")
        os.system('pause')