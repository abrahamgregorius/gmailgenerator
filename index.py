# Gmail Maker Bot by Abraham Gregorius

from time import sleep
import helper
import os
import uiautomator2
import name

device_id = "YLDYKZT44TAUTS6L"
d = uiautomator2.connect('YLDYKZT44TAUTS6L')

# Check if device is on
#status = os.system(f'adb shell dumpsys input_method | findstr "mScreenOn=true"')
#print(status)

status = os.system('adb -s '+ device_id +' shell dumpsys power | findstr "mHoldingDisplaySuspendBlocker"')
firstname = name.generateFirstName()
lastname = name.generateLastName()

# if status == False:
#     helper.pressKey('POWER')
#     os.system(f'adb -s '+ device_id +' shell input swipe 400 1100 400 300')
#     sleep(1)
#     os.system(f'adb -s '+ device_id +' shell input tap 365 1400')
#     sleep(0.5)
#     os.system(f'adb -s '+ device_id +' shell input tap 525 1166')
#     sleep(0.5)
#     os.system(f'adb -s '+ device_id +' shell input tap 365 1400')
#     sleep(0.5)
#     os.system(f'adb -s '+ device_id +' shell input tap 200 1065')

os.system(f'adb -s '+ device_id + ' shell input swipe 580 40 580 800')
os.system(f'adb -s '+ device_id + ' shell input tap 590 210')
os.system(f'adb -s '+ device_id + ' shell input swipe 400 1445 400 211')
os.system(f'adb -s '+ device_id + ' shell input swipe 400 1445 400 211')
os.system(f'adb -s '+ device_id + ' shell input tap 330 1045')
sleep(0.3)
os.system(f'adb -s '+ device_id + ' shell input tap 330 450')
sleep(0.3)
os.system(f'adb -s '+ device_id + ' shell input tap 330 990')
sleep(2)
os.system(f'adb -s '+ device_id + ' shell input tap 370 1445')
os.system(f'adb -s '+ device_id + ' shell input tap 590 1265')
os.system(f'adb -s '+ device_id + ' shell input tap 370 1445')
os.system(f'adb -s '+ device_id + ' shell input tap 140 1150')
os.system(f'adb -s '+ device_id + ' shell input tap 535 920')
sleep(2)
os.system(f'adb -s '+ device_id + ' shell input tap 180 680')
os.system(f'adb -s '+ device_id + ' shell input tap 170 750')
os.system(f'adb -s '+ device_id + ' shell input tap 288 458')
os.system(f'adb -s '+ device_id + ' shell input tap 288 458')
split = [*firstname.upper()]
for i in split:
    if i == " ":
        helper.pressKey("SPACE")
    helper.pressKey(i)

    
