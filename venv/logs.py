import time
from datetime import datetime
class logs():

    filePrinter="logs.txt"

    def saveEvent(self,message):
        self.message=message
        now = datetime.now()
        current_time = now.strftime("%D %H:%M")
        with open(self.filePrinter, 'a') as file:
            file.write(current_time+ " "+self.message)
            file.close()
