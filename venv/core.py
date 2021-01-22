
from notifications import notifications
from PrinterStatus import PrinterStatus
from IpAddress import IpAddress

PrintersIpAddres= IpAddress()
PrintersIPs = PrintersIpAddres.readPrinterInformation()
status=PrinterStatus()
for x in PrintersIPs:
    var = x.split()
    for l in range(0, len(var), 2):
        ipAddress = var[l]
        printerLocation = var[l + 1]
        result = str(status.runStatus(var[l]))
        if len(result) > 3:
            notifier = notifications(ipAddress, printerLocation, result)
            notifier.sendEmail()







