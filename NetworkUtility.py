
import socket


class NetworkUtility:
    def __init__(self):
        clientsInNetwork = []
        for ping in range(1,255):
            ipAddress = "192.168.1." + str(ping)
            try:
                ip = socket.gethostbyaddr(ipAddress)
                nameOfDevice = ip[0]
                address = ip[2][0]
                pointPos = nameOfDevice.index(".")
                newClient = [nameOfDevice[:pointPos],address ]
                clientsInNetwork.append(newClient)
            except:
                print(ipAddress,"is unused") 
        print("-----------------")
        print("Number of Devices Found:", len(clientsInNetwork)) 
        print("-----------------")
        for clients in clientsInNetwork:
            print(f"Name: {clients[0]:30} \tIp: {clients[1]}")


print("Starting NetworkUtility")
network =  NetworkUtility()