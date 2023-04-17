import os
import time

time.sleep(3)

devices = [i.strip().split(" ") for i in os.popen("wmic logicaldisk get name,description,volumename").read().strip().split("\n")]

time.sleep(3)

while True:
    Usb = os.popen("wmic logicaldisk get name,description,volumename").read()
    
    # put data in list
    newDevices = [i.strip().split(" ") for i in Usb.strip().split("\n")]
    print("detecting pendrive...")
    # check if new device is added
    if(newDevices[-1][-1].lower() == "ramansharma" and len(newDevices) > len(devices)):
        print("pendrive detected...")
        # get pendrive full path
        pendrivePath = os.popen(f"wmic logicaldisk where \"volumename='{newDevices[-1][-1]}'\" get name").read().strip().split("\n")[-1]
        programPath = f'{pendrivePath}\\start.py'


        # check if program is present in pendrive
        if(os.path.exists(programPath)):
            # run the program

            os.system(f"python {programPath}")
            time.sleep(10)
    