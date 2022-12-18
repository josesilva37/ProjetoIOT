import logging
import asyncio
import platform
from random import randint

from bleak import BleakClient
from bleak import _logger as logger


BTN_A_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
# BTN_B_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"



async def run(address, debug=False):
    if debug:
        import sys

        l = logging.getLogger("asyncio")
        l.setLevel(logging.DEBUG)
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(logging.DEBUG)
        l.addHandler(h)
        logger.addHandler(h)


    async with BleakClient(address) as client:
        x = await client.is_connected()
        logger.info("Connected: {0}".format(x))

        def btn_a_handler(sender, data):
            """Simple notification handler for btn a events."""
            print("{0}: {1}".format(sender, data))
            # Pick random letter to send
            # if int.from_bytes(data, byteorder='little', signed=False) > 0:
                # letter = [randint(99, 122)]
                # loop.create_task(write_txt(letter))

        # async def write_txt(data):
        #     await client.write_gatt_char(LED_TXT_UUID,
        #                                  data)

        await client.start_notify(BTN_A_UUID, btn_a_handler)
        # await client.start_notify(BTN_B_UUID, btn_b_handler)

        while await client.is_connected():
            await asyncio.sleep(1)

if __name__ == "__main__":
    address = ("C4:49:51:F3:54:F0")

    loop = asyncio.get_event_loop()
    # loop.set_debug(True)
    loop.run_until_complete(run(address, True))