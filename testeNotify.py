import base64
import sys
import os
import asyncio
# import aioconsole


from bleak import BleakClient


ADDRESS = "C4:49:51:F3:54:F0"
# #ADDRESS = '00:55:DA:B7:98:9C'
CHARACTERISTIC_UUID = '6e400003-b5a3-f393-e0a9-e50e24dcca9e'

if len(sys.argv) == 3:
    ADDRESS = sys.argv[1]
    CHARACTERISTIC_UUID = sys.argv[2]


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    print("{0}: {1}".format(sender, data))


async def run(address):
    async with BleakClient(address) as client:

        # await client.connect()
        print("Is connected")
        
        # key = base64.b16decode(b'00x30x09')
        key2 = bytes([0x03, 0x08])
        key3 = bytearray(b'Java2Blog').decode('utf-8')
        
        # print(key)
        print(key2)
        print(key3)

        # start notifications on control characteristic
        await client.start_notify('6e400003-b5a3-f393-e0a9-e50e24dcca9e', notification_handler)
        # write to control handle, set preset to 21
        await client.write_gatt_char('6e400002-b5a3-f393-e0a9-e50e24dcca9e', key2 , response=True)
        # write to control handle get device info
        # start notifications on TP9
        await client.start_notify('6e400003-b5a3-f393-e0a9-e50e24dcca9e', notification_handler)
        # wait for input
        # await aioconsole.ainput('Running: Press a key to quit')
        await client.stop_notify('6e400003-b5a3-f393-e0a9-e50e24dcca9e')


if __name__ == "__main__":

    os.environ["PYTHONASYNCIODEBUG"] = str(1)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run(ADDRESS))
    asyncio.run(run(ADDRESS))