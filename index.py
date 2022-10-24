import random
from time import sleep
import helper
import os
import uiautomator2

device_id = "YLDYKZT44TAUTS6L"
d = uiautomator2.connect('YLDYKZT44TAUTS6L')

# Check if device is on
#status = os.system(f'adb shell dumpsys input_method | findstr "mScreenOn=true"')
#print(status)

status = os.system('adb -s '+ device_id +' shell dumpsys power | findstr "mHoldingDisplaySuspendBlocker"')

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

# Open the settings
os.system(f'adb -s '+ device_id + ' shell input swipe 580 40 580 800')
os.system(f'adb -s '+ device_id + ' shell input tap 590 210')

# Find Google settings
os.system(f'adb -s '+ device_id + ' shell input swipe 400 1445 400 211')
os.system(f'adb -s '+ device_id + ' shell input swipe 400 1445 400 211')
os.system(f'adb -s '+ device_id + ' shell input tap 330 1045')
sleep(1)

# Creating account
os.system(f'adb -s '+ device_id + ' shell input tap 330 450')
sleep(1)
os.system(f'adb -s '+ device_id + ' shell input tap 330 990')
sleep(5)

# Type password
os.system(f'adb -s '+ device_id + ' shell input tap 370 1445')
os.system(f'adb -s '+ device_id + ' shell input tap 590 1265')
os.system(f'adb -s '+ device_id + ' shell input tap 370 1445')
os.system(f'adb -s '+ device_id + ' shell input tap 140 1150')
os.system(f'adb -s '+ device_id + ' shell input tap 535 920')

sleep(10)

# Press Create Account
os.system(f'adb -s '+ device_id + ' shell input tap 180 680')
os.system(f'adb -s '+ device_id + ' shell input tap 170 750')

sleep(5)

# Press First Name
os.system(f'adb -s '+ device_id + ' shell input tap 288 458')
os.system(f'adb -s '+ device_id + ' shell input tap 288 458')

# Generate first and last name
firstname = str(helper.generateFirstName())
lastname = str(helper.generateLastName())

sleep(5)

# Type the first name
split = [*firstname.upper()]
for i in split:
    helper.pressKey(i)
helper.pressKey('ENTER')

sleep(5)

# Type the last name
split = [*lastname.upper()]
for i in split:
    helper.pressKey(i)
helper.pressKey('ENTER')

sleep(7)

# Set the month
month = helper.randomMonth()
os.system(f'adb -s '+ device_id + ' shell input tap 150 450')
os.system(f'adb -s '+ device_id + ' shell input tap ' + month)

# Set the day
os.system(f'adb -s '+ device_id + ' shell input tap 340 465')
d = helper.randomDay()
day = str(d)
for i in day:
    helper.pressKey(i)

# Set the year
os.system(f'adb -s '+ device_id + ' shell input tap 540 465')
y = helper.randomYear()
year = str(y)
for i in year:
    helper.pressKey(i)

# Set the gender
gender = helper.randomGender()
os.system(f'adb -s '+ device_id + ' shell input tap 300 610')
os.system(f'adb -s '+ device_id + ' shell input tap ' + gender)

# Press Next
os.system(f'adb -s '+ device_id + ' shell input tap 620 1470')

sleep(5)

# Choose email
os.system(f'adb -s '+ device_id + ' shell input tap 320 570')

# Press next
os.system(f'adb -s '+ device_id + ' shell input tap 620 1470')

sleep(5)

# Input password
os.system(f'adb -s '+ device_id + ' shell input tap 200 500')
p = helper.generateAPassword()
passw = str(p)
for i in passw:
    helper.pressKey(i)