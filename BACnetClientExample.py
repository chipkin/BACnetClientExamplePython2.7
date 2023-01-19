import sys
import time
import socket
from io import BlockingIOError

import keyboard
from CASBACnetStackExampleConstants import *
from CASBACnetStackAdapter import *  # Contains all the Enumerations, and callback prototypes
import pathlib

APPLICATION_VERSION = "0.0.1"
SETTING_BACNET_IP_PORT = 47808
SETTING_CLIENT_DEVICE_INSTANCE = 389002
SETTING_DOWNSTREAM_DEVICE_PORT = SETTING_BACNET_IP_PORT
SETTING_DOWNSTREAM_DEVICE_INSTANCE = 389999
SETTING_DEFAULT_DOWNSTREAM_DEVICE_IP_ADDRESS = "192.168.2.217"

downstreamConnectionString = None  # TODO: Update accordingly
invokeId = None
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


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
        ExampleWhoIs()
        pass
    elif action == "r":
        ExampleReadProperty()
        pass
    elif action == "u":
        ExampleWriteProperty()
        pass
    elif action == "c":
        ExampleSubscribeCOV()
        pass
    elif action == "t":
        ExampleConfirmedTextMessage()
        pass
    else:
        print("CAS BACnet Stack Client Example v", APPLICATION_VERSION)
        print ("https://github.com/chipkin/BACnetClientExamplePython2.7")
        print ("Usage: BACnetClient {IPAddress}")
        print ("Example: BACnetClient 192.168.1.127")
        print ("Help")
        print ("- Q - Quit")
        print ("- W - Send WhoIs message")
        print("- R - Send Read property messages")
        print ("- U - Send Write property messages")
        print ("- C - Send Subscribe COV Request")
        print("- T - Send Confirmed Text Message Request")
    return True


def WaitForResponse(timeout=3):
    expireTime = time.time() + timeout
    while time.time() < expireTime:
        # fpLoop()
        pass


def octetStringCopy(source, destination, length, offset=0):
    for i in range(length):
        destination[int(i + offset)] = int(source[i])


def ExampleWhoIs():
    if not downstreamConnectionString:
        print ("Error: Invalid connection string")
        return

    print("Sending WhoIs with no range. timeout=[3]...")
    ctype_connection_string = ctypes.cast(downstreamConnectionString, ctypes.POINTER(ctypes.c_uint8))
    ctype_connection_string_length = ctypes.c_uint8(6)
    ctype_network_type = ctypes.c_uint8(casbacnetstack_networkType["ip"])
    ctype_broadcast = ctypes.c_bool(True)

    CASBACnetStack.BACnetStack_SendWhoIs(ctype_connection_string, ctype_connection_string_length
                                         , ctype_network_type, ctype_broadcast
                                         ,
                                         ctypes.c_uint16(65535), None, ctypes.c_uint8(0))
    # CASBACnetStack.BACnetStack_SendWhoIs(ctypes.c_uint32(downstreamConnectionString, 6, 0, True, 0, None, 0)
    WaitForResponse()
    print("Sending WhoIs with range, low=[389900], high=[389999] 3 second timeout...")
    CASBACnetStack.BACnetStack_SendWhoIsWithLimits(ctypes.c_uint32(389900), ctypes.c_uint32(389999),
                                                   ctype_connection_string, ctype_connection_string_length,
                                                   ctype_network_type, ctype_broadcast, 0,
                                                   None, 0)
    WaitForResponse()
    print("Sending WhoIs to specific network. network=[15], timeout=[3]")
    CASBACnetStack.BACnetStack_SendWhoIs(downstreamConnectionString, 6, 0, True, 15, None, 0)
    WaitForResponse()
    print("Sending WhoIs to broadcast network. network=[65535], timeout=[3]")
    CASBACnetStack.BACnetStack_SendWhoIs(downstreamConnectionString, 6, 0, True, 65535, None, 0)
    #
    WaitForResponse()


def CallbackGetSystemTime():
    return str(time.time())


def ExampleReadProperty():
    print ("Sending Read Property. DeviceID=[" + str(SETTING_DOWNSTREAM_DEVICE_INSTANCE) + "], property=[" + str(
        PROPERTY_IDENTIFIER_ALL) + "], timeout=[3]...")
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_ANALOG_INPUT, 0, PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_ANALOG_OUTPUT, 1, PROPERTY_IDENTIFIER_OBJECT_NAME, False,
                                                 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_ANALOG_VALUE, 2, PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_BINARY_INPUT, 3, PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_BINARY_OUTPUT, 4, PROPERTY_IDENTIFIER_OBJECT_NAME, False,
                                                 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_BINARY_VALUE, 5, PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_DEVICE, 8, PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_MULTI_STATE_INPUT, 13, PROPERTY_IDENTIFIER_OBJECT_NAME,
                                                 False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_MULTI_STATE_OUTPUT, 14, PROPERTY_IDENTIFIER_OBJECT_NAME,
                                                 False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_MULTI_STATE_VALUE, 19, PROPERTY_IDENTIFIER_OBJECT_NAME,
                                                 False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_TREND_LOG, 20, PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_BITSTRING_VALUE, 39, PROPERTY_IDENTIFIER_OBJECT_NAME,
                                                 False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_CHARACTERSTRING_VALUE, 40, PROPERTY_IDENTIFIER_OBJECT_NAME,
                                                 False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_DATE_VALUE, 42, PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_INTEGER_VALUE, 45, PROPERTY_IDENTIFIER_OBJECT_NAME, False,
                                                 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_LARGE_ANALOG_VALUE, 46, PROPERTY_IDENTIFIER_OBJECT_NAME,
                                                 False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_OCTETSTRING_VALUE, 47, PROPERTY_IDENTIFIER_OBJECT_NAME,
                                                 False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_POSITIVE_INTEGER_VALUE, 48,
                                                 PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0);
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_TIME_VALUE, 50, PROPERTY_IDENTIFIER_OBJECT_NAME, False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_NETWORK_PORT, 56, PROPERTY_IDENTIFIER_OBJECT_NAME, False,
                                                 0)

    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_MULTI_STATE_INPUT, 13, PROPERTY_IDENTIFIER_PRESENT_VALUE,
                                                 False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_MULTI_STATE_OUTPUT, 14, PROPERTY_IDENTIFIER_PRESENT_VALUE,
                                                 False, 0)
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_MULTI_STATE_VALUE, 19, PROPERTY_IDENTIFIER_PRESENT_VALUE,
                                                 False, 0)

    CASBACnetStack.BACnetStack_SendReadProperty(invokeId, downstreamConnectionString, 6, 0, 0, None, 0)
    WaitForResponse()


def ExampleWriteProperty():
    print("Sending Read Property. AnalogValue, INSTANCE=[2], property=[" + str(PROPERTY_IDENTIFIER_PRESENT_VALUE
                                                                               ) + "], timeout=[3]...")
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_ANALOG_VALUE, 2, PROPERTY_IDENTIFIER_PRESENT_VALUE, False,
                                                 0)
    CASBACnetStack.BACnetStack_SendReadProperty(invokeId, downstreamConnectionString, 6, 0, 0, None, 0)
    WaitForResponse()

    print("Sending WriteProperty to the Present Value of Analog Value 2...")
    CASBACnetStack.BACnetStack_BuildWriteProperty(4, "1.0", 3, OBJECT_TYPE_ANALOG_VALUE, 2,
                                                  PROPERTY_IDENTIFIER_PRESENT_VALUE, False, 0, False,
                                                  16)
    CASBACnetStack.BACnetStack_SendWriteProperty(invokeId, downstreamConnectionString, 6, 0, 0, None, 0)
    WaitForResponse()

    print("Sending Read Property. AnalogValue, INSTANCE=[2], property=[" + str(PROPERTY_IDENTIFIER_PRESENT_VALUE
                                                                               ) + "], timeout=[3]...")
    CASBACnetStack.BACnetStack_BuildReadProperty(OBJECT_TYPE_ANALOG_VALUE, 2, PROPERTY_IDENTIFIER_PRESENT_VALUE, False,
                                                 0)
    CASBACnetStack.BACnetStack_SendReadProperty(invokeId, downstreamConnectionString, 6, 0, 0, None, 0)
    WaitForResponse()


def ExampleSubscribeCOV():
    timeToLive = 60 * 5
    analogValueProcessIdentifier = 0
    analogInputProcessIdentifier = 1
    print("Sending Subscribe COV Request. Analog Input, INSTANCE=[0], timeToLive = " + str(timeToLive) +
          ", processIdentifier = " + str(analogValueProcessIdentifier))
    CASBACnetStack.BACnetStack_SendSubscribeCOV(invokeId, analogInputProcessIdentifier, OBJECT_TYPE_ANALOG_INPUT, 0,
                                                False, timeToLive,
                                                downstreamConnectionString, 6, 0, 0, None, 0)
    WaitForResponse()

    print("Sending Subscribe COV Request. Analog Value, INSTANCE=[2], timeToLive = " + str(timeToLive) +
          ", processIdentifier = " + str(analogInputProcessIdentifier))
    CASBACnetStack.BACnetStack_SendSubscribeCOV(invokeId, analogValueProcessIdentifier, OBJECT_TYPE_ANALOG_VALUE, 2,
                                                False, timeToLive,
                                                downstreamConnectionString, 6, 0, 0, None, 0)

    WaitForResponse()


def ExampleConfirmedTextMessage():
    useMessageClass = True
    messageClassUnsigned = 5
    messageClassString = ""
    messagePriority = 0
    message = "Hello from the Python client example"

    print("Sending Confirmed Text Message")
    CASBACnetStack.BACnetStack_SendConfirmedTextMessage(invokeId, SETTING_CLIENT_DEVICE_INSTANCE, useMessageClass,
                                                        messageClassUnsigned,
                                                        messageClassString, len(messageClassString), messagePriority,
                                                        message, len(message),
                                                        downstreamConnectionString, 6, 0, 0, None, 0);

    WaitForResponse()


def CallbackReceiveMessage(message, maxMessageLength, receivedConnectionString, maxConnectionStringLength,
                           receivedConnectionStringLength,
                           networkType):
    try:
        data, addr = udpSocket.recvfrom(maxMessageLength)
        # if not data:
        #     print("DEBUG: not data")
        # A message was received.
        # print ("DEBUG: CallbackReceiveMessage. Message Received", addr, data, len(data) )

        # Convert the received address to the CAS BACnet Stack connection string format.
        ip_as_bytes = bytes(map(int, addr[0].split(".")))
        for index, value in enumerate(ip_as_bytes):
            receivedConnectionString[index] = value
        # UDP Port
        receivedConnectionString[4] = int(addr[1] / 256)
        receivedConnectionString[5] = addr[1] % 256
        # New ConnectionString Length
        receivedConnectionStringLength[0] = 6

        # Convert the received data to a format that CAS BACnet Stack can process.
        for i in range(len(data)):
            message[i] = data[i]

        # Set the network type
        networkType[0] = ctypes.c_uint8(casbacnetstack_networkType["ip"])
        return len(data)
    except BlockingIOError:
        # No message, We are not waiting for a incoming message so our socket returns a BlockingIOError. This is normal.
        return 0

    # Catch all
    return 0


def CallbackSendMessage(message, messageLength, connectionString, connectionStringLength, networkType, broadcast):
    # Currently we are only supporting IP
    if networkType != casbacnetstack_networkType["ip"]:
        print("Error: Unsupported network type. networkType:", networkType)
        return 0

    # Extract the Connection String from CAS BACnet Stack into an IP address and port.
    udpPort = connectionString[4] * 256 + connectionString[5]
    if broadcast:
        # Use broadcast IP address
        # ToDo: Get the subnet mask and apply it to the IP address

        ipAddress = str(connectionString[0]) + "." + str(connectionString[1]) + "." + str(
            connectionString[2]) + "." + str(connectionString[3])
    else:
        ipAddress = str(connectionString[0]) + "." + str(connectionString[1]) + "." + str(
            connectionString[2]) + "." + str(connectionString[3])

    # Extract the message from CAS BACnet Stack to a bytearray
    data = bytearray(messageLength)
    for i in range(len(data)):
        data[i] = message[i]

    # Send the message
    udpSocket.sendto(data, (ipAddress, udpPort))
    print("Sent message:" + str(message) + "\n to:" + str(ipAddress) + "\n Port:" + str(
        udpPort) + "\n Message lenth:" + str(messageLength))
    return messageLength


def SetServiceIamEnabled():
    pass


def convertIpAddStringToConnectionString(IPAddress, Port):
    import struct
    ConnectionString = [None] * 6
    # print (IPAddress)

    ip_as_bytes = struct.unpack('BBBB', socket.inet_aton(IPAddress))  # bytes(map(int, IPAddress.split(".")))
    print (ip_as_bytes)
    for index, value in enumerate(ip_as_bytes):
        print (value)
        ConnectionString[index] = value

    # UDP Port
    ConnectionString[4] = int(Port / 256)
    ConnectionString[5] = Port % 256
    print (ConnectionString)

    return ConnectionString


def generateAddressString(ip_address, port):
    addressString = (ctypes.c_uint8 * 6)()
    octetStringCopy(ip_address.split("."), addressString, 4)
    addressString[4] = int(port / 256)
    addressString[5] = port % 256
    return addressString


def main(args):
    print ("CAS BACnet Stack Client Example v" + str(APPLICATION_VERSION) + ".")  # +CIBUILDNUMBER
    print("https://github.com/chipkin/BACnetClientExamplePython2.7")

    # Print the version information
    print("FYI: CAS BACnet Stack version: " + str(CASBACnetStack.BACnetStack_GetAPIMajorVersion()) + "." +
          str(CASBACnetStack.BACnetStack_GetAPIMinorVersion()) +
          "." + str(CASBACnetStack.BACnetStack_GetAPIPatchVersion()) + "." +
          str(CASBACnetStack.BACnetStack_GetAPIBuildVersion()))
    print("FYI: CAS BACnet Stack python adapter version:" + str(casbacnetstack_adapter_version))

    downstream_Device_ip_address = SETTING_DEFAULT_DOWNSTREAM_DEVICE_IP_ADDRESS
    if len(args) >= 1:
        downstream_Device_ip_address = args[0]
        print("FYI: Using " + str(downstream_Device_ip_address) + " for the downstream device IP address")
    print("FYI: Loading CAS BACnet Stack functions... ")
    # TODO:

    print ("OK")

    # "FYI: CAS BACnet Stack version: " << fpGetAPIMajorVersion() << "." << fpGetAPIMinorVersion() << "." <<
    # fpGetAPIPatchVersion() << "." << fpGetAPIBuildVersion()

    print("FYI: Registering the callback Functions with the CAS BACnet Stack")
    # ---------------------------------------------------------------------------

    # Note:
    # Make sure you keep references to CFUNCTYPE() objects as long as they are used from C code.
    # ctypes doesn't, and if you don"t, they may be garbage collected, crashing your program when
    # a callback is made
    #
    # Because of garbage collection, the pyCallback**** functions need to stay in scope.
    pyCallbackReceiveMessage = fpCallbackReceiveMessage(CallbackReceiveMessage)
    CASBACnetStack.BACnetStack_RegisterCallbackReceiveMessage(pyCallbackReceiveMessage)
    pyCallbackSendMessage = fpCallbackSendMessage(CallbackSendMessage)
    CASBACnetStack.BACnetStack_RegisterCallbackSendMessage(pyCallbackSendMessage)
    pyCallbackGetSystemTime = fpCallbackGetSystemTime(CallbackGetSystemTime)
    CASBACnetStack.BACnetStack_RegisterCallbackGetSystemTime(pyCallbackGetSystemTime)

    # TODO:

    print("Setting up client device. device.instance=[" + str(SETTING_CLIENT_DEVICE_INSTANCE) + "]")
    if not CASBACnetStack.BACnetStack_AddDevice(SETTING_CLIENT_DEVICE_INSTANCE):
        print("Failed to add Device.")
        return False

    # TODO:
    print("Created Device.")
    CASBACnetStack.BACnetStack_SetServiceEnabled(SETTING_CLIENT_DEVICE_INSTANCE, SERVICE_I_AM, True)
    CASBACnetStack.BACnetStack_SetServiceEnabled(SETTING_CLIENT_DEVICE_INSTANCE, SERVICE_I_HAVE, True)
    CASBACnetStack.BACnetStack_SetServiceEnabled(SETTING_CLIENT_DEVICE_INSTANCE, SERVICE_WHO_IS, True)
    CASBACnetStack.BACnetStack_SetServiceEnabled(SETTING_CLIENT_DEVICE_INSTANCE, SERVICE_WHO_HAS, True)
    CASBACnetStack.BACnetStack_SetServiceEnabled(SETTING_CLIENT_DEVICE_INSTANCE, SERVICE_READ_PROPERTY_MULTIPLE, True)
    CASBACnetStack.BACnetStack_SetServiceEnabled(SETTING_CLIENT_DEVICE_INSTANCE, SERVICE_WRITE_PROPERTY, True)
    CASBACnetStack.BACnetStack_SetServiceEnabled(SETTING_CLIENT_DEVICE_INSTANCE, SERVICE_WRITE_PROPERTY_MULTIPLE, True)

    print("Generated the connection string for the downstream device. ")

    # TODO:

    global downstreamConnectionString
    downstreamConnectionString = generateAddressString(ip_address=downstream_Device_ip_address,
                                                       port=SETTING_DOWNSTREAM_DEVICE_PORT)

    print ("FYI: Entering main loop...")
    while True:
        # Call the DLLs loop function which checks for messages and processes them.
        # fpLoop()
        if not DoUserInput():
            break
        # Call Sleep to give some time back to the system
        time.sleep(0)


if __name__ == "__main__":
    # Load the shared library into ctypes
    libpath = pathlib.Path().absolute() / libname
    print("FYI: Libary path: ", libpath)
    CASBACnetStack = ctypes.CDLL(str(libpath), mode=ctypes.RTLD_GLOBAL)
    args = sys.argv[1:]
    main(args=args)
