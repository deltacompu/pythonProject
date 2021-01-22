import socket
import logging
import time

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

    def runStatus(self,IpAddress):
        a = []
        self.IpAddress = IpAddress
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.debug("Connect")
        try:
            s.connect((self.IpAddress, self.TCP_PORT))
            if s:
                print(str(s.getpeername())+" printer online ")
                s.send(bytes(self.zplCommand, "utf-8"))
                dataFromServer = s.recv(1024)
                ab = dataFromServer.decode()
                cd = ab.split(",")
                if int(cd[1]) == 0:
                    print("Media ok")
                    #a.append(" Media ok ")
                else:
                    #print("Media out")
                    a.append(" Media out ")
                if int(cd[2]) == 0:
                    print("Printer is not paused")
                    #a.append(" Printer is not paused ")
                else:
                    # print("Printer is paused")
                    a.append(" Printer is paused ")

                s.close()
            else:
                print(" aqui printer offline")
                a.append("Printer is offline")
                s.close()
            return a
        except socket.error as e:
            a.append("Printer is offline")
            return a
            logging.error("!!! Socket Connect FAILED: %s" % e)
            s.close()


