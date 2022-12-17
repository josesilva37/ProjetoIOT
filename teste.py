import logging
import asyncio
import platform

from bleak import BleakClient
from bleak import _logger as logger


CHARACTERISTIC_UUID = (
    '6e400001-b5a3-f393-e0a9-e50e24dcca9e'
)  # <--- Change to the characteristic you want to enable notifications from.


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    print("{0}: {1}".format(sender, data))


async def run(address, loop, debug=False):
    if debug:
        import sys

        # loop.set_debug(True)
        l = logging.getLogger("asyncio")
        l.setLevel(logging.DEBUG)
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(logging.DEBUG)
        l.addHandler(h)
        logger.addHandler(h)

    async with BleakClient(address, loop=loop) as client:
        x = await client.is_connected()
        logger.info("Connected: {0}".format(x))

        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
        await asyncio.sleep(5.0, loop=loop)
        await client.stop_notify(CHARACTERISTIC_UUID)


if __name__ == "__main__":
    import os

    os.environ["PYTHONASYNCIODEBUG"] = str(1)
    address = (
        "C4:49:51:F3:54:F0"  # <--- Change to your device's address here if you are using Windows or Linux
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(address, loop, True))