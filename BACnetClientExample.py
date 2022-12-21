import time

import keyboard
from CASBACnetStackExampleConstants import *

APPLICATION_VERSION = "0.0.1"
SETTING_BACNET_IP_PORT = 47808


def main(argc, argv):
    pass


def DoUserInput():
    """
    Function checks if the user has hit any key and return false if quit key is hit
    :returns false for quit and true for no key hit
    :return:
    """
    action = keyboard.read_key()
    if not action:
        return True
    print (action)
    if action == "q":
        return False
    elif action == "w":
        pass
    elif action == "r":
        pass
    elif action == "u":
        pass
    elif action == "c":
        pass
    elif action == "t":
        pass
    else:
        print("CAS BACnet Stack Client Example v", APPLICATION_VERSION)
        print ("https://github.com/chipkin/BACnetClientExamplePython2.7")
        print ("Usage: BACnetClient {IPAddress}")
        print ("Example: BACnetClient 192.168.1.126")
        print ("Help")
        print ("- Q - Quit")
        print ("- W - Send WhoIs message")
        print("- R - Send Read property messages")
        print ("- U - Send Write property messages")
        print ("- C - Send Subscribe COV Request")
        print("- T - Send Confirmed Text Message Request")
    return True


def CallbackGetSystemTime():
    return int(time.time())


def ExampleWhoIs():
    pass


def ExampleReadProperty():
    pass


def ExampleWriteProperty():
    pass


def ExampleSubscribeCOV():
    pass


def ExampleConfirmedTextMessage():
    pass


def CallbackReceiveMessage(message, maxMessageLength, receivedConnectionString, maxConnectionStringLength,
                           receivedConnectionStringLength, networkType):
    if not message:
        print("Invalid input buffer")
        return 0
    if not receivedConnectionString or maxConnectionStringLength == 0:
        print("Invalid connection string buffer")
        return 0
    if maxConnectionStringLength < 6:
        print ("Not enough space for UDP connection string")
        return 0


#     Start reading message
def CallbackSendMessage(message, messageLength, connectionString, connectionStringLength, networkType, broadcast):
    if not message or messageLength == 0:
        print("Nothing to send")
        return 0
    if not connectionString or connectionStringLength == 0:
        print ("No connection string")
        return 0
    if networkType!=NETWORK_TYPE_IP:
        print ("Message for a different network")
def HelperPrintCommonHookParameters(connectionString, connectionStringLength,
                                    networkType, network, sourceAddress, sourceAddressLength):
    print ("networkType=[", networkType, "], ")
    print ("connectionString=[")
