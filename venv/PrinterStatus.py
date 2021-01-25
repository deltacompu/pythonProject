import socket
import logging
import time
from logs import logs

class PrinterStatus():
    TCP_PORT = 5964
    BUFFER_SIZE = 1024
    zplCommand = """
    ~HS
    """


    def __init__(self):
        self.TCP_PORT = 5964
        self.BUFFER_SIZE = 1024
        self.zplCommand = """
            ~HS
            """
        self.register=logs()

    def runStatus(self,IpAddress):
        a = []
        self.IpAddress = IpAddress
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        logging.debug("Connect")
        try:
            s.connect((self.IpAddress, self.TCP_PORT))
            if s:
                print(str(s.getpeername())+" printer online ")
                self.register.saveEvent(str(s.getpeername())+" printer online ")
                s.send(bytes(self.zplCommand, "utf-8"))
                dataFromServer = s.recv(1024)
                ab = dataFromServer.decode()
                cd = ab.split(",")
                if int(cd[1]) == 0:
                    print("Media ok")
                    self.register.saveEvent("Media ok")
                    #a.append(" Media ok ")
                else:
                    #print("Media out")
                    a.append(" Media out ")
                    self.register.saveEvent(" Media out ")
                if int(cd[2]) == 0:
                    print("Printer is not paused")
                    #a.append(" Printer is not paused ")
                    self.register.saveEvent("Printer is not paused")
                else:
                    # print("Printer is paused")
                    a.append(" Printer is paused ")
                    self.register.saveEvent("Printer is paused")
                s.close()
            else:
                a.append("Printer is offline")
                s.close()
            return a
        except socket.timeout:
            a.append("Printer is offline")
            self.register.saveEvent(self.IpAddress+ " printer offline ")
            print("Printer is offline")
            return a
            s.close()


