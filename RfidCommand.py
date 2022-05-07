import serial
from time import sleep
import functools
from Enum import CommandList,CommandBlock

ser = serial.Serial('COM4',115200,timeout=0.1)  # connect to RFID Device
address = 0xFF  # set RFID Address

debug = False

# Generate CRC Based on cmd
def crc(cmd):
    uSum = 0
    for i in range(len(cmd)):
        uSum = uSum + cmd[i]
    cmd.append(((uSum ^ 0xFFF) & 0xFF )+ 1)
    return cmd

def sendCommand(cmd):
    ser.write(cmd)
    return getResponseFormat()

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


def test_write():
    readProductID()
    testProductID = "ISTTS123"
    cnt = 3
    writeProductID(testProductID, cnt)
    readProductID()

def setWorkMode(mode):
    AnswerMode = [0x02,0x00]
    ActiveMode = [0x02,0x01]
    if mode == "answer":
        flush()
        writeCommand(CommandList.SET_DEVICE_ONE_PARAM.value,AnswerMode)
    if mode == "active":
        writeCommand(CommandList.SET_DEVICE_ONE_PARAM.value,ActiveMode)

def startReadActive():
    writeCommand(CommandList.START_READ.value)

def stopReadActive():
    writeCommand(CommandList.STOP_READ.value)

def getResponseFormat():
    sleep(0.2)
    data = ser.readall()
    response_hex = data.hex().upper()
    hex_list = [response_hex[i:i + 2] for i in range(0, len(response_hex), 2)]
    hex_space = ' '.join(hex_list)
    if debug:
        print(hex_space)

def ActiveResponseParser():
    if ser.inWaiting():
        respond = ser.read(32)

        data = respond[18:len(respond)-2]
        rssi = respond[len(respond)-2:len(respond)-1]
        response_hex = data.hex().upper()
        hex_list = [response_hex[i:i + 2] for i in range(0, len(response_hex), 2)]
        data = ' '.join(hex_list)
        if data:
            print("Data : " + str(data) + " rssi: " + str(rssi.hex()))

#percobaan
setWorkMode("active")
startReadActive()
cart = [{'data':"aabbccddeeff",'cnt':1},{'data':"ssfdfadszcfzxc",'cnt':1},{'data':"sfthsfdgfsg",'cnt':1},]
detected_item = 'aabbccddeeff'

if not any(item['data'] == detected_item for item in cart):
    cart.append({'data':detected_item,'cnt':1})
else:
    data_index = next((index for (index, d) in enumerate(cart) if d["data"] == detected_item), None)
    print(data_index)
    cart[data_index].update({'cnt':cart[data_index]['cnt']+1})
print(cart)
#percobaan
if __name__ == '__main__':
    while(1):
        ActiveResponseParser()







