import time
import subprocess
from datetime import datetime

process=None
firstShift=True
secondShift=False
thirdShift=False

while True:
    now=datetime.now()
    current_time=now.strftime("%H:%M")
    time.sleep(10)
    print(current_time)
    if current_time == "08:00" and firstShift:
        print('Running script first shift')
        process= subprocess.Popen("python3 core.py")
        firstShift = False
        secondShift = True
    elif current_time == "15:00" and secondShift:
        print('Running script second shift2')
        process=subprocess.Popen("python3 core.py")
        secondShift=False
        thirdShift=True
    elif current_time=="23:00" and thirdShift:
        print('Running script third shift3')
        process=subprocess.Popen("python3 core.py")
        thirdShift=False
        firstShift=True


