import enum

class CommandList(enum.Enum):
    READ_SYSTEM_PARAM = 0x10
    READ_DEVICE_PARAM = 0x20
    SET_DEVICE_PARAM = 0x21
    DEFAULT_DEVICE_PARAM = 0x22
    READ_DEVICE_ONE_PARAM = 0x23
    SET_DEVICE_ONE_PARAM = 0x24
    READ_DEVICE_NET_PARAM = 0x26
    SET_DEVICE_NET_PARAM = 0x28
    READ_DEVICE_TIME = 0x2B
    SET_DEVICE_TIME = 0x2C
    READ_DEVICE_SPECIAL_PARAM = 0x2E
    SET_DEVICE_SPECIAL_PARAM = 0x2F
    READ_FREQ = 0x3E
    SET_FREQ = 0x3F
    STOP_READ = 0x40
    START_READ = 0x41
    ACTIVE_DATA = 0x45
    CHECK_MODULE = 0xE0
    CHECK_ANT = 0xE1
    CLOSE_RELAY = 0x85
    RELEASE_RELAY = 0x86
    HEARTBEAT_PACK = 0xFF
    INVENTORY_TAG = 0x01
    COM_READ_TAG_DATA = 0x02
    COM_WRITE_TAG = 0x03

class CommandBlock(enum.Enum):
    HEAD = [0x53,0x57]
