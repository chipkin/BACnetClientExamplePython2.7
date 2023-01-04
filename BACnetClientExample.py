import sys
import time

import keyboard
from CASBACnetStackExampleConstants import *
from CASBACnetStackAdapter import *  # Contains all the Enumerations, and callback prototypes

APPLICATION_VERSION = "0.0.1"
SETTING_BACNET_IP_PORT = 47808
SETTING_CLIENT_DEVICE_INSTANCE = 389002
SETTING_DOWNSTREAM_DEVICE_PORT = SETTING_BACNET_IP_PORT
SETTING_DOWNSTREAM_DEVICE_INSTANCE = 389999
SETTING_DEFAULT_DOWNSTREAM_DEVICE_IP_ADDRESS = "192.168.2.217"


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


def WaitForResponse(timeout=3):
    expireTime = time.time() + timeout;
    while time.time() < expireTime:
        # fpLoop()
        pass


def ExampleWhoIs():
    print("Sending WhoIs with no range. timeout=[3]...")
    # fpSendWhoIs(downstreamConnectionString, 6, 0, true, 0, NULL, 0)
    WaitForResponse()
    print("Sending WhoIs with range, low=[389900], high=[389999] 3 second timeout...")
    # fpSendWhoIsWithLimits(389900, 389999, downstreamConnectionString, 6, 0, true, 0, NULL, 0)
    WaitForResponse()
    print("Sending WhoIs to specific network. network=[15], timeout=[3]")
    # fpSendWhoIs(downstreamConnectionString, 6, 0, true, 15, NULL, 0)
    WaitForResponse()
    print("Sending WhoIs to broadcast network. network=[65535], timeout=[3]")
    # fpSendWhoIs(downstreamConnectionString, 6, 0, true, 65535, NULL, 0)

    WaitForResponse()


def CallbackGetSystemTime():
    return time.time()


def ExampleReadProperty():
    print ("Sending Read Property. DeviceID=[" + str(SETTING_DOWNSTREAM_DEVICE_INSTANCE) + "], property=[" + str(
        PROPERTY_IDENTIFIER_ALL) + "], timeout=[3]...")


def ExampleWriteProperty():
    print("Sending Read Property. AnalogValue, INSTANCE=[2], property=[" + str(PROPERTY_IDENTIFIER_PRESENT_VALUE
                                                                               ) + "], timeout=[3]...")
    WaitForResponse()

    print("Sending WriteProperty to the Present Value of Analog Value 2...")
    WaitForResponse()

    print("Sending Read Property. AnalogValue, INSTANCE=[2], property=[" + str(PROPERTY_IDENTIFIER_PRESENT_VALUE
                                                                               ) + "], timeout=[3]...")
    WaitForResponse()


def ExampleSubscribeCOV():
    timeToLive = 60 * 5
    analogValueProcessIdentifier = 0
    analogInputProcessIdentifier = 1
    print("Sending Subscribe COV Request. Analog Input, INSTANCE=[0], timeToLive = " + str(timeToLive) +
          ", processIdentifier = " + str(analogValueProcessIdentifier))
    WaitForResponse()

    print("Sending Subscribe COV Request. Analog Value, INSTANCE=[2], timeToLive = " + str(timeToLive) +
          ", processIdentifier = " + str(analogInputProcessIdentifier))

    WaitForResponse()


def ExampleConfirmedTextMessage():
    useMessageClass = True
    messageClassUnsigned = 5
    messageClassString = ""
    messagePriority = 0
    message = "Hello from the C++ client example"

    print("Sending Confirmed Text Message")

    WaitForResponse()


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
    if networkType != NETWORK_TYPE_IP:
        print ("Message for a different network")


def HelperPrintCommonHookParameters(connectionString, connectionStringLength,
                                    networkType, network, sourceAddress, sourceAddressLength):
    print ("networkType=[" + str(networkType) + "], ")
    print ("connectionString=[" + str(connectionString[1]) + "." + str(connectionString[1]) + "." + str(
        connectionString[2]) + "." + str(connectionString[3]) + ":" + str(
        ((connectionString[4] * 256) + connectionString[5])) + "], ")


def HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex):
    print("InvokeID=[", originalInvokeId, "], service=[", service, "], objectInstance = [", objectInstance, "], ")
    if objectType == OBJECT_TYPE_ANALOG_OUTPUT:
        objectString = "analog_input(" + str(OBJECT_TYPE_ANALOG_INPUT) + ")"
    elif objectType == OBJECT_TYPE_ANALOG_OUTPUT:
        objectString = "analog_output(" + str(OBJECT_TYPE_ANALOG_OUTPUT) + ")"
    elif objectType == OBJECT_TYPE_ANALOG_VALUE:
        objectString = "analog_value(" + str(OBJECT_TYPE_ANALOG_VALUE) + ")"
    elif objectType == OBJECT_TYPE_BINARY_INPUT:
        objectString = "binary_input(" + str(OBJECT_TYPE_BINARY_INPUT) + ")"
    elif objectType == OBJECT_TYPE_BINARY_OUTPUT:
        objectString = "binary_output(" + str(OBJECT_TYPE_BINARY_OUTPUT) + ")"
    elif objectType == OBJECT_TYPE_BINARY_VALUE:
        objectString = "binary_value(" + str(OBJECT_TYPE_BINARY_VALUE) + ")"
    elif objectType == OBJECT_TYPE_DEVICE:
        objectString = "device(" + str(OBJECT_TYPE_DEVICE) + ")"
    elif objectType == OBJECT_TYPE_MULTI_STATE_INPUT:
        objectString = "multi_state_input(" + str(OBJECT_TYPE_MULTI_STATE_INPUT) + ")"
    elif objectType == OBJECT_TYPE_MULTI_STATE_OUTPUT:
        objectString = "multi_state_output(" + str(OBJECT_TYPE_MULTI_STATE_OUTPUT) + ")"
    elif objectType == OBJECT_TYPE_MULTI_STATE_VALUE:
        objectString = "multi_state_value(" + str(OBJECT_TYPE_MULTI_STATE_VALUE) + ")"
    elif objectType == OBJECT_TYPE_TREND_LOG:
        objectString = "trend_log(" + str(OBJECT_TYPE_TREND_LOG) + ")"
    elif objectType == OBJECT_TYPE_BITSTRING_VALUE:
        objectString = "bitstring_value(" + str(OBJECT_TYPE_BITSTRING_VALUE) + ")"
    elif objectType == OBJECT_TYPE_CHARACTERSTRING_VALUE:
        objectString = "characterstring_value(" + str(OBJECT_TYPE_CHARACTERSTRING_VALUE) + ")"
    elif objectType == OBJECT_TYPE_DATE_VALUE:
        objectString = "date_value(" + str(OBJECT_TYPE_DATE_VALUE) + ")"
    elif objectType == OBJECT_TYPE_INTEGER_VALUE:
        objectString = "integer_value(" + str(OBJECT_TYPE_INTEGER_VALUE) + ")"
    elif objectType == OBJECT_TYPE_LARGE_ANALOG_VALUE:
        objectString = "large_analog_value(" + str(OBJECT_TYPE_LARGE_ANALOG_VALUE) + ")"
    elif objectType == OBJECT_TYPE_OCTETSTRING_VALUE:
        objectString = "octetstring_value(" + str(OBJECT_TYPE_OCTETSTRING_VALUE) + ")"
    elif objectType == OBJECT_TYPE_POSITIVE_INTEGER_VALUE:
        objectString = "positive_integer_value(" + str(OBJECT_TYPE_POSITIVE_INTEGER_VALUE) + ")"
    elif objectType == OBJECT_TYPE_TIME_VALUE:
        objectString = "time_value(" + str(OBJECT_TYPE_TIME_VALUE) + ")"
    elif objectType == OBJECT_TYPE_NETWORK_PORT:
        objectString = "network_port(" + str(OBJECT_TYPE_NETWORK_PORT) + ")"
    elif objectType == OBJECT_TYPE_ELEVATOR_GROUP:
        objectString = "elevator_group(" + str(OBJECT_TYPE_ELEVATOR_GROUP) + ")"
    elif objectType == OBJECT_TYPE_ESCALATOR:
        objectString = "escalator(" + str(OBJECT_TYPE_ESCALATOR) + ")"
    elif objectType == OBJECT_TYPE_LIFT:
        objectString = "lift(" + str(OBJECT_TYPE_LIFT) + ")"
    else:
        objectString = str(objectType)
    print("objectType=[", objectString, "],")

    if propertyIdentifier == PROPERTY_IDENTIFIER_ALL:
        propertyString = "all(" + str(PROPERTY_IDENTIFIER_ALL) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_COV_INCURMENT:
        propertyString = "cov_incurment(" + str(PROPERTY_IDENTIFIER_COV_INCURMENT) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_DAY_LIGHT_SAVINGS_STATUS:
        propertyString = "day_light_savings_status(" + str(PROPERTY_IDENTIFIER_DAY_LIGHT_SAVINGS_STATUS) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_DESCRIPTION:
        propertyString = "description(" + str(PROPERTY_IDENTIFIER_DESCRIPTION) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_LOCAL_DATE:
        propertyString = "local_date(" + str(PROPERTY_IDENTIFIER_LOCAL_DATE) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_LOCAL_TIME:
        propertyString = "local_time(" + str(PROPERTY_IDENTIFIER_LOCAL_TIME) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_NUMBER_OF_STATES:
        propertyString = "number_of_states(" + str(PROPERTY_IDENTIFIER_NUMBER_OF_STATES) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_OBJECT_NAME:
        propertyString = "object_name(" + str(PROPERTY_IDENTIFIER_OBJECT_NAME) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_PRESENT_VALUE:
        propertyString = "present_value(" + str(PROPERTY_IDENTIFIER_PRESENT_VALUE) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_PRIORITY_ARRAY:
        propertyString = "priority_array(" + str(PROPERTY_IDENTIFIER_PRIORITY_ARRAY) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_RELIABILITY:
        propertyString = "reliability(" + str(PROPERTY_IDENTIFIER_RELIABILITY) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_STATE_TEXT:
        propertyString = "state_text(" + str(PROPERTY_IDENTIFIER_STATE_TEXT) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_STATUS_FLAGS:
        propertyString = "status_flags(" + str(PROPERTY_IDENTIFIER_STATUS_FLAGS) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_SYSTEM_STATUS:
        propertyString = "system_status(" + str(PROPERTY_IDENTIFIER_SYSTEM_STATUS) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_UTC_OFFSET:
        propertyString = "utc_offset(" + str(PROPERTY_IDENTIFIER_UTC_OFFSET) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_BIT_TEXT:
        propertyString = "bit_text(" + str(PROPERTY_IDENTIFIER_BIT_TEXT) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_MAX_PRES_VALUE:
        propertyString = "max_pres_value(" + str(PROPERTY_IDENTIFIER_MAX_PRES_VALUE) + ")"
    elif propertyIdentifier == PROPERTY_IDENTIFIER_MIN_PRES_VALUE:
        propertyString = "min_pres_value(" + str(PROPERTY_IDENTIFIER_MIN_PRES_VALUE) + ")"
    else:
        propertyString = str(propertyIdentifier)

    print("propertyIdentifier=[" + str(propertyString) + "]")

    if usePropertyArrayIndex:
        print("propertyArrayIndex=[" + str(propertyArrayIndex) + "], ")


if __name__ == "__main__":
    args = sys.argv[1:]
    print ("CAS BACnet Stack Client Example v" + str(APPLICATION_VERSION) + ".")  # +CIBUILDNUMBER
    print("https://github.com/chipkin/BACnetClientExamplePython2.7")

    downstream_Device_ip_address = SETTING_DEFAULT_DOWNSTREAM_DEVICE_IP_ADDRESS
    if len(args) >= 1:
        downstream_Device_ip_address = args[0]
        print("FYI: Using " + str(downstream_Device_ip_address) + " for the downstream device IP address")
    print("FYI: Loading CAS BACnet Stack functions... ")
    # TODO:

    print ("OK")

    # "FYI: CAS BACnet Stack version: " << fpGetAPIMajorVersion() << "." << fpGetAPIMinorVersion() << "." <<
    # fpGetAPIPatchVersion() << "." << fpGetAPIBuildVersion()

    print("FYI: Connecting UDP Resource to port=[" + str(SETTING_BACNET_IP_PORT) + "]... ")

    # TODO:

    print("OK, Connected to port")

    print("FYI: Registering the callback Functions with the CAS BACnet Stack")

    # TODO:

    print("Setting up client device. device.instance=[" + str(SETTING_CLIENT_DEVICE_INSTANCE) + "]")

    # TODO:
    print("Created Device.")

    print("Generated the connection string for the downstream device. ")
    # TODO:

    print ("FYI: Entering main loop...")
    while True:
        # Call the DLLs loop function which checks for messages and processes them.
        # fpLoop()
        if not DoUserInput():
            break
        # Call Sleep to give some time back to the system
        time.sleep(0)
