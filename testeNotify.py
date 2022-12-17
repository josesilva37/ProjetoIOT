import sys
import asyncio
import platform

from bleak import BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic


# you can change these to match your device or override them from the command line
# CHARACTERISTIC_UUID = "f000aa65-0451-4000-b000-000000000000"
# ADDRESS = (
#     "24:71:89:cc:09:05"
#     if platform.system() != "Darwin"
#     else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"
# )


def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
    """Simple notification handler which prints the data received."""
    print("entrou aqui")
    print(f"{characteristic.description}: {data}")


async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        desc = await client.read_gatt_char('6e400003-b5a3-f393-e0a9-e50e24dcca9e')
        print ("char: ", desc)
        await client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(5.0)
        await client.stop_notify(char_uuid)


if __name__ == "__main__":
    asyncio.run(main('C4:49:51:F3:54:F0', '6e400003-b5a3-f393-e0a9-e50e24dcca9e'))