import time
from datetime import datetime
class logs():


    # Open function to open the file "MyFile1.txt"
    # (same directory) in append mode and
    filePrinter="logs.txt"

    def saveEvent(self,message):
        self.message=message
        now = datetime.now()
        current_time = now.strftime("%D %H:%M")
        with open(self.filePrinter, 'a') as file:
            file.write(current_time+ " "+self.message + "\n")
            file.close()
