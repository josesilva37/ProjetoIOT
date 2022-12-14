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
import numpy as np
from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic
import pika
import numpy as np
import threading

# you can change these to match your device or override them from the command line
CHARACTERISTIC_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
CHARACTERISTIC_UUID2 = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"

ADDRESS = (
    "C4:49:51:F3:54:F0"
)

# Const variables
G = 9.807
ACC_RANGE = 8.0
RAW_SCALLING = 32768.0
accScale = G / (RAW_SCALLING / ACC_RANGE)
PI = 3.14159
D2R = PI / 180.0
gyroScale = 1000.0 / RAW_SCALLING * D2R
magScale = 4912.0 / RAW_SCALLING
TEMP_OFFSET = 21
TEMP_SCALE = 333.87

# Send BLE Data to Broker
host = '192.168.1.158'
credentials = pika.PlainCredentials("admin", "admin")
parameters = pika.ConnectionParameters(host, 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()


# Read BLE Data


def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    """Simple notification handler which prints the data received."""
    print(f"{characteristic.description}: {data}")

    if (data[0] == 4):
        channel.queue_declare(queue='packet4')
        channel.basic_publish(exchange='', routing_key='packet4', body=data)
    elif(data[0] == 1):
        channel.queue_declare(queue='packet1')
        channel.basic_publish(exchange='', routing_key='packet1', body=data)


key_header = bytes([0x03, 0x08])
key_start_ble_stream = bytes([0x03, 0x00, 0x00])
key_setSR_mode = bytes([0x03, 0x01, 0x01, 0x04])


async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        # print(await client.read_gatt_descriptor("0x7fa5ac5147c0"))
        # print(client.services.)

        # print(await client.read_gatt_char("6e400003-b5a3-f393-e0a9-e50e24dcca9e"))
        await client.start_notify(char_uuid, notification_handler)
        await client.write_gatt_char(CHARACTERISTIC_UUID2, key_start_ble_stream)
        await asyncio.sleep(10.0)
        # await client.stop_notify(char_uuid)
        # connection.close()


if __name__ == "__main__":
    asyncio.run(
        # main(ADDRESS, CHARACTERISTIC_UUID)
        main(
            sys.argv[1] if len(sys.argv) > 1 else ADDRESS,
            sys.argv[2] if len(sys.argv) > 2 else CHARACTERISTIC_UUID,
        )
    )
