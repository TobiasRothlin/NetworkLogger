
import socket


class NetworkUtility:
    def __init__(self):
        self.clientsInNetwork = []
        self.findClientsInNetwork()
        self.printClientList()

    def findClientsInNetwork(self, ipBody = "192.168.1.", endIp = 255, startIp = 0):
        for ping in range(startIp,endIp):
            print(".", end = "")
            ipAddress = ipBody + str(ping)
            try:
                ip = socket.gethostbyaddr(ipAddress)
                nameOfDevice = ip[0]
                address = ip[2][0]
                pointPos = nameOfDevice.index(".")
                newClient = [nameOfDevice[:pointPos],address ]
                self.clientsInNetwork.append(newClient)
            except:
                pass

    def printClientList(self):
        print("\n-----------------")
        print("Number of Devices Found:", len(self.clientsInNetwork)) 
        print("-----------------")
        for clients in self.clientsInNetwork:
            print(f"Name: {clients[0]:30} \tIp: {clients[1]}")




print("Starting NetworkUtility")
network =  NetworkUtility()