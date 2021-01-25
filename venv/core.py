from notifications import notifications
from PrinterStatus import PrinterStatus
from IpAddress import IpAddress
from logs import logs
class core():

    def sTART(self):
        message=[]
        final=[]
        PrintersIpAddres= IpAddress()
        PrintersIPs = PrintersIpAddres.readPrinterInformation()
        status=PrinterStatus()
        logger=logs()
        for x in PrintersIPs:
            var = x.split()
            for l in range(0, len(var), 2):
                ipAddress = var[l]
                printerLocation = var[l + 1]
                result = str(status.runStatus(var[l]))
                if len(result) > 3:
                    message.append(ipAddress)
                    message.append(printerLocation)
                    message.append(result)
                    a = "Printer located near pole "+ printerLocation+" with Ip Address "+ ipAddress+ " is facing the next error "+result+"\n"
                    final.append(a)
        if (len(final) != 0):
            multiline_str = ''.join((final))
            notifier = notifications()
            notifier.sendEmail(multiline_str)
        elif (len(final) == 0):
            logger.saveEvent("All printers are online \n")







