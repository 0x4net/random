import BAC0
import time

myIP = '<Your IP>/<MASK>' #You need to be on the same subnet as the bacnet device. Example: '192.168.1.4/24'
bacnet = BAC0.connect(ip=myIP)
bacnet.whois() #Broadcast request of bacnet devices
time.sleep(5)  #Wait for devices to respond
for i, (deviceId, companyId, devIp, numDeviceId) in enumerate(bacnet.devices):
    print(f"-------- Device #{numDeviceId} --------")
    print(f"Device:     {deviceId}")
    print(f"IP:         {devIp}")
    print(f"Company:    {companyId}")
    readDevice = bacnet.readMultiple(f"{devIp} device {numDeviceId} all")
    print(f"Model Name: {readDevice[11]}")
    print(f"Version:    {readDevice[2]}")
    # print(readDevice) #List all available info about the device
