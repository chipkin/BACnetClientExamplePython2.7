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


def HookIAm(deviceIdentifier, maxApduLengthAccepted, segmentationSupported, vendorIdentifier,
            connectionString, connectionStringLength, networkType, network, sourceAddress, sourceAddressLength):
    print("HookIAm. deviceIdentifier=[" + str(deviceIdentifier) + "], maxApduLengthAccepted=[" + str(
        maxApduLengthAccepted) +
          "], segmentationSupported=[" + str(segmentationSupported) + "], vendorIdentifier=[" + str(
                vendorIdentifier) + "], ")
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network,
                                    sourceAddress, sourceAddressLength)


def HookIHave(deviceIdentifier, objectType, objectInstance, objectName, objectNameLength, objectNameEncoding,
              connectionString, connectionStringLength, networkType, network, sourceAddress, sourceAddressLength):
    print("HookIHave. deviceIdentifier=[", deviceIdentifier, "], objectType=[", objectType,
          "], objectInstance=[" + str(objectInstance) + "], objectName=[" + str(objectName) +
          "], objectNameEncoding=[" + str(objectNameEncoding) + "], ")
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookError(originalInvokeId, errorChoice, errorClass, errorCode, connectionString, connectionStringLength,
              networkType, network, sourceAddress, sourceAddressLength, useObjectProperty, objectType,
              objectInstance, propertyIdentifier):
    print("HookError. originalInvokeId=[" + str(originalInvokeId) + "], errorChoice=[" + str(
        errorChoice) + "], errorClass=[" +
          str(errorClass) + "], errorCode=[" + str(errorCode) + "], ")
    print(
            "useObjectProperty=[" + str(useObjectProperty) + "], objectType=[" + str(
        objectType) + "], objectInstance=[" + str(objectInstance) +
            "], propertyIdentifier=[" + str(propertyIdentifier) + "], ")
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength);


def HookReject(originalInvokeId, rejectReason, connectionString, connectionStringLength, networkType, network,
               sourceAddress, sourceAddressLength):
    print("HookError. originalInvokeId=[" + str(originalInvokeId) + "], rejectReason=[" + str(rejectReason) + "], ")
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength);


def HookAbort(originalInvokeId, sentByServer, abortReason, connectionString, connectionStringLength, networkType,
              network, sourceAddress, sourceAddressLength):
    print("HookAbort. originalInvokeId=[" + str(originalInvokeId) + "], sentByServer=[" + str(
        sentByServer) + "], abortReason=[" + str(abortReason) + "], ")
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookSimpleAck(originalInvokeId, serverAckChoice, connectionString, connectionStringLength, networkType, network,
                  sourceAddress, sourceAddressLength):
    print("HookSimpleAck. originalInvokeId=[" + str(originalInvokeId) + "], serverAckChoice=[" + str(
        serverAckChoice) + "], ")
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookTimeout(originalInvokeId, connectionString, connectionStringLength, networkType, network, sourceAddress,
                sourceAddressLength):
    print("HookTimeout. originalInvokeId=[" + str(originalInvokeId) + "], ")
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyBitString(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                          usePropertyArrayIndex,
                          propertyArrayIndex, value, length, connectionString, connectionStringLength, networkType,
                          network, sourceAddress, sourceAddressLength):
    print("HookPropertyBitString. ")

    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyBool(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                     propertyArrayIndex, value, connectionString, connectionStringLength, networkType, network,
                     sourceAddress, sourceAddressLength):
    print("HookPropertyBool. value=[" + str(value) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyCharString(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                           usePropertyArrayIndex, propertyArrayIndex, value, length, encoding, connectionString,
                           connectionStringLength, networkType, network, sourceAddress, sourceAddressLength):
    print("HookPropertyCharString. value=[" + str(value) + "], length=[" + str(length) + "], encoding=[" + str(
        encoding) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyDate(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                     propertyArrayIndex, year, month, day, weekday, connectionString, connectionStringLength,
                     networkType, network, sourceAddress, sourceAddressLength):
    print("HookPropertyDate. year=[" + str(year) + "], month=[" + str(month) + "], day=[" + str(day) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyDouble(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                       propertyArrayIndex, value, connectionString, connectionStringLength, networkType,
                       network, sourceAddress, sourceAddressLength):
    print("HookPropertyDouble. value=[" + str(value) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyEnum(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                     propertyArrayIndex, value, connectionString, connectionStringLength, networkType, network,
                     sourceAddress, sourceAddressLength):
    print("HookPropertyEnum. value=[" + str(value) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyNull(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                     propertyArrayIndex, connectionString, connectionStringLength, networkType, network,
                     sourceAddress, sourceAddressLength):
    print("HookPropertyNull. value=[null], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyObjectIdentifier(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                 usePropertyArrayIndex, propertyArrayIndex, objectTypeValue, objectInstanceValue,
                                 connectionString, connectionStringLength, networkType, network, sourceAddress,
                                 sourceAddressLength):
    print("HookPropertyObjectIdentifier. objectInstanceValue=[" + str(objectInstanceValue) + "], objectTypeValue=[",
          str(objectTypeValue) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyOctString(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                          usePropertyArrayIndex, propertyArrayIndex, value, length, connectionString,
                          connectionStringLength, networkType, network, sourceAddress, sourceAddressLength):
    print("HookPropertyOctString. ")

    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyInt(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                    propertyArrayIndex, value, connectionString, connectionStringLength, networkType, network,
                    sourceAddress, sourceAddressLength):
    print("HookPropertyInt. value=[" + str(value) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyReal(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                     propertyArrayIndex, value, connectionString, connectionStringLength, networkType, network,
                     sourceAddress, sourceAddressLength):
    print("HookPropertyReal. value=[" + str(value) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyTime(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                     propertyArrayIndex, hour, minute, second, hundrethSecond, connectionString, connectionStringLength,
                     networkType, network, sourceAddress, sourceAddressLength):
    print("HookPropertyTime. hour=[" + str(hour) + "], minute=[" + str(minute) + "], second=[" + str(
        second) + "], hundrethSecond=[" + str(hundrethSecond) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookPropertyUInt(originalInvokeId, service, objectType, objectInstance, propertyIdentifier, usePropertyArrayIndex,
                     propertyArrayIndex, value, connectionString, connectionStringLength, networkType, network,
                     sourceAddress, sourceAddressLength):
    print("HookPropertyUInt. value=[" + str(value) + "], ")
    HelperPrintCommonHookPropertyParameters(originalInvokeId, service, objectType, objectInstance, propertyIdentifier,
                                            usePropertyArrayIndex, propertyArrayIndex)
    HelperPrintCommonHookParameters(connectionString, connectionStringLength, networkType, network, sourceAddress,
                                    sourceAddressLength)


def HookTextMessage(sourceDeviceIdentifier, useMessageClass, messageClassUnsigned, messageClassString,
                    messageClassStringLength, messagePriority, message, messageLength, connectionString,
                    connectionStringLength, networkType, sourceNetwork, sourceAddress, sourceAddressLength, errorClass,
                    errorCode):
    print("HookTextMessage. sourceDeviceIdentifier=[" + str(sourceDeviceIdentifier) + "], useMessageClass=[" + str(
        useMessageClass) + "], messageClassString=[" + str(messageClassString) + "], messageClassStringLength=[" + str(
        messageClassStringLength) + "], messagePriority=[" + str(messagePriority) + "], message=[" + str(
        message) + "], messageLength=[" + str(messageLength) + "], ")
    print("networkType=[" + str(networkType) + "], ")
    print("connectionString=[" + str(connectionString[0]) + "." + str(connectionString[1]) + "." + str(
        connectionString[2]) + "." + str(connectionString[3]) + ":" + str(
        ((connectionString[4] * 256) + connectionString[5])) + "], ")

    return True
