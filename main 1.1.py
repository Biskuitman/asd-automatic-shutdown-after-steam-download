import os
import time
import winreg

x = 180  #countdown lengh (steam has to have time after the download is finished)

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\Valve\Steam")
steampath = winreg.QueryValueEx(key, "InstallPath")[0]
path = os.path.join(steampath, "steamapps", "downloading")

print("waiting for download to start")
print("")

run = True
while(run):  #looking for the download to start
    if os.listdir(path):
        print("download detected")
        print("waiting for download to end")
        run = False
run = True

while(run):  #waiting for the download to end
    if not os.listdir(path):
        print("")
        print("countdowm")
        while x != 0:  #the countdown
            print(x)
            time.sleep(1)
            x -= 1
        run = False

print("shut down")
os.system("shutdown /s /t 1")