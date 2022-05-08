import serial
from time import sleep
import functools
from Enum import CommandList,CommandBlock

ser = serial.Serial('COM4',115200,timeout=0.1)  # connect to RFID Device
address = 0xFF  # set RFID Address

debug = True

# Generate CRC Based on cmd
def crc(cmd):
    uSum = 0
    for i in range(len(cmd)):
        uSum = uSum + cmd[i]
    cmd.append(((uSum ^ 0xFFF) & 0xFF )+ 1)
    return cmd


def writeCommand(cmd,data = []):
    COMMAND_BLOCK = []
    COMMAND_BLOCK.extend(CommandBlock.HEAD.value)
    COMMAND_BLOCK.append(0x00)
    COMMAND_BLOCK.append(len(data) + 3)
    COMMAND_BLOCK.append(address)
    COMMAND_BLOCK.append(cmd)
    COMMAND_BLOCK.extend(data)
    COMMAND_BLOCK = crc(COMMAND_BLOCK)
    if debug:
        print("Command : " + str(bytearray(COMMAND_BLOCK).hex()))
    return sendCommand(COMMAND_BLOCK)

def readSystemParam():
    return writeCommand(CommandList.READ_SYSTEM_PARAM.value)

def readProductID():
    data = []
    password = [0x00,0x00,0x00,0x00]
    region = [0x01] #0x00 reserved 0x01 EPC 0x02 TID 0x03 User
    startAddress = [0x02]
    length = [0x06]
    data.extend(region)
    data.extend(startAddress)
    data.extend(length)
    data.extend(password)
    return writeCommand(CommandList.COM_READ_TAG_DATA.value,data)

def writeProductID(ProductID,cnt):
    data = []
    ProductID = bytearray(ProductID.encode())
    password = [0x00,0x00,0x00,0x00]
    region = [0x01] #0x00 reserved 0x01 EPC 0x02 TID 0x03 User
    startAddress = [0x02]
    length = [6]
    data.extend(region)
    data.extend(startAddress)
    data.extend(length)
    data.extend(password)
    data.extend(ProductID)
    data.extend(cnt.to_bytes(4,'big'))
    return writeCommand(CommandList.COM_WRITE_TAG.value,data)

def inventoryScan():
    sendCommand([0x53,0x57,0x00,0x06,0xff,0x01,0x01,0x00,0x06,0x49])
    # return writeCommand(CommandList.INVENTORY_TAG.value)

def flush():
    test = ser.readall()
    if debug:
        print("dump : " + str(test))


def test_write(prefix,suffix):
    readProductID()
    testProductID = prefix
    cnt = suffix
    writeProductID(testProductID, cnt)
    readProductID()

def setWorkMode(mode):
    AnswerMode = [0x02,0x00]
    ActiveMode = [0x02,0x01]
    if mode == "answer":
        writeCommand(CommandList.SET_DEVICE_ONE_PARAM.value,AnswerMode)
    if mode == "active":
        writeCommand(CommandList.SET_DEVICE_ONE_PARAM.value,ActiveMode)

def startReadActive():
    writeCommand(CommandList.START_READ.value)

def stopReadActive():
    writeCommand(CommandList.STOP_READ.value)

def sendCommand(cmd):
    ser.write(cmd)
    return getResponseFormat()


def getResponseFormat():
    sleep(0.1)
    dataLength = ser.inWaiting()
    if dataLength > 10:
        data = ser.read()
        response_hex = data.hex().upper()
        hex_list = [response_hex[i:i + 2] for i in range(0, len(response_hex), 2)]
        hex_space = ' '.join(hex_list)
        if debug:
            print(hex_space)
        return  hex_space
    else:
        return False

def toHexString(data):
    data_hex = data.hex().upper()
    hex_list = [data_hex[i:i + 2] for i in range(0, len(data_hex), 2)]
    hex_space = ' '.join(hex_list)
    return hex_space


def ActiveResponseParser():
    if ser.inWaiting():
        respond = ser.read(32)
        prefix = respond[18:len(respond)-6]
        suffix = respond[18 + len(prefix):len(respond)-2]
        rssi = respond[len(respond)-2:len(respond)-1]
        prefix = toHexString(prefix)
        suffix = toHexString(suffix)
        if prefix:
            if debug:
                print("Prefix : " + str(prefix) + " Suffix : " + suffix + " rssi: " + str(rssi.hex()))
            return prefix, suffix
        else:
            return "", ""
    else:
        return "", ""

# setWorkMode('answer')
# test_write("UNSUR123",0)



if __name__ == '__main__':
    setWorkMode('active')
    startReadActive()
    while 1:
        prefix, suffix = ActiveResponseParser()
        if prefix != "":
            print("Prefix : " + prefix + " Suffix : " + suffix)







