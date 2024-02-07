import BAC0
import time

# If your attack box has more than one adapter, you need to set the IP below so it knows which
# interface to send the broadcast request out of
# You should be on the same subnet as the bacnet device. This is untested for devices on different subnets

myIP = '192.168.1.4/24'
bacnet = BAC0.connect(ip=myIP)

# bacnet discovery works on your subnet broadcast address. x.x.x.255 for /24
bacnet.whois()

# wait about 5 seconds for the broadcast messages and bacnet devices to return data
# larger subnets or more bacnet devices on the network may require more time to responde
# wireshark can be helpful in watching the return data
print("Sleeping...")
time.sleep(5)


# bacnet.whois() will contain a list of tuples, with all the devices that responded to the whois()
# Example: [('Device 9981', 'VenderName', '192.168.1.150', 9981)]

for i, (deviceId, companyId, devIp, numDeviceId) in enumerate(bacnet.devices):
    print(f"-------- Device #{numDeviceId} --------")
    print(f"Device:     {deviceId}")
    print(f"IP:         {devIp}")
    print(f"Company:    {companyId}")

    # connect to the device to query more data
    # im not sure if this is the same output for all systems or if device specific
    readDevice = bacnet.readMultiple(f"{devIp} device {numDeviceId} all")
    print(f"Model Name: {readDevice[11]}")
    print(f"Version:    {readDevice[2]}")
    # too see all available info:
    # print(readDevice)

    # you can also query a list of points on the system
    # readPointsDevice = BAC0.device(devIp,numDeviceId, bacnet)
    # print(readPointsDevice.points)




