# -*- coding: utf-8 -*-
"""
Notifications
-------------

Example showing how to add notifications to a characteristic and handle the responses.

Updated on 2019-07-03 by hbldh <henrik.blidh@gmail.com>

"""
import sys
import asyncio
import platform

from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic


# you can change these to match your device or override them from the command line
CHARACTERISTIC_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
CHARACTERISTIC_UUID2 = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

ADDRESS = (
    "C4:49:51:F3:54:F0"
)


def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    """Simple notification handler which prints the data received."""
    print(f"{characteristic.description}: {data}")

key = bytes([0x03, 0x00, 0x07])
async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        # print(await client.read_gatt_descriptor("0x7fa5ac5147c0"))
        # print(client.services.)
        
        # print(await client.read_gatt_char("6e400003-b5a3-f393-e0a9-e50e24dcca9e"))
        await client.start_notify(char_uuid, notification_handler)
        await client.write_gatt_char(CHARACTERISTIC_UUID2,key )
        # print(bytearray(b'\x01\x03\xc4IQ\xf3T\xf0\x01\x00\x01\x00\x00\x00\x00\x00:\x01\x02\x020\x07\x02\x02\x00\x00').decode('utf-16'))
        await asyncio.sleep(5.0)
        # await client.stop_notify(char_uuid)


if __name__ == "__main__":
    asyncio.run(
        # main(ADDRESS, CHARACTERISTIC_UUID)
        main(
            sys.argv[1] if len(sys.argv) > 1 else ADDRESS,
            sys.argv[2] if len(sys.argv) > 2 else CHARACTERISTIC_UUID,
        )
    )
