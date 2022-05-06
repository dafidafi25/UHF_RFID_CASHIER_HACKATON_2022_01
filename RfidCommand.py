import serial
from time import sleep
import functools
from Enum import CommandList,CommandBlock

ser = serial.Serial('COM4',115200,timeout=0.1)  # connect to RFID Device
address = 0xFF  # set RFID Address

# Generate CRC Based on cmd
def crc(cmd):
    uSum = 0
    for i in range(len(cmd)):
        uSum += cmd[i]
    cmd.append(((uSum ^ 0xFFF) & 0xFF )+ 1)
    return cmd

def getResponseFormat():
    sleep(0.1)
    dataLeft = ser.inWaiting()
    if dataLeft >= 2:
        head = ser.read(2)
        if head[0] == 0x43 and head[1] == 0x54:
            dataLength = ser.read(2)
            return responseParser(dataLength)
        else:
            flush()
            return False

def responseParser(dataLength):
    dataLength = functools.reduce(lambda a,b: a+b,dataLength)
    respond = ser.read(dataLength)
    status = respond[3:4]

    if status == 0x00:
        return status
    data = respond[5:5 + dataLength - 6]
    return data

def sendCommand(cmd):
    ser.write(cmd)
    return getResponseFormat()

def writeCommand(cmd,data = []):
    COMMAND_BLOCK = CommandBlock.HEAD.value
    COMMAND_BLOCK.append(0x00)
    COMMAND_BLOCK.append(len(data) + 3)
    COMMAND_BLOCK.append(address)
    COMMAND_BLOCK.append(cmd)
    COMMAND_BLOCK.extend(data)
    COMMAND_BLOCK = crc(COMMAND_BLOCK)
    return sendCommand(COMMAND_BLOCK)

def readSystemParam():
    return writeCommand(CommandList.READ_SYSTEM_PARAM.value)

def readProductID():
    data = []
    password = [0x00,0x00,0x00,0x00]
    region = [0x01] #0x00 reserved 0x01 EPC 0x02 TID 0x03 User
    startAddress = [0x00]
    length = [0x06]
    data.extend(region)
    data.extend(startAddress)
    data.extend(length)
    data.extend(password)
    return writeCommand(CommandList.COM_READ_TAG_DATA.value,data)




def flush():
    test = ser.readall()
    print("dump : " + str(test))


if __name__ == '__main__':
    flush()
    productID = readProductID()
    print(productID.hex())
    # readSystemParam()
    # ser.write([0x53,0x57,0x00,0x03,0xff,0x10,0x44])
    #
    # getResponseFormat()





