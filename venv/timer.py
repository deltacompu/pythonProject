import time
import subprocess
from datetime import datetime
from core import core
process=None
firstShift=True
secondShift=False
thirdShift=False
start = core()
while True:
    now=datetime.now()
    print(now)
    current_time=now.strftime("%H:%M")
    time.sleep(10)
   if current_time == "08:00" and firstShift:
        print('Running script first shift')
        start.sTART()
        firstShift = False
        secondShift = True
    elif current_time == "15:00" and secondShift:
        print('Running script second shift 2')
        start.sTART()
        secondShift=False
        thirdShift=True
    elif current_time=="23:00" and thirdShift:
        print('Running script third shift 3')
        start.sTART()
        thirdShift=False
        firstShift=True


