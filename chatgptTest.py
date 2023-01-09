import struct
from datetime import datetime

# Assume that the byte array contains four integers, representing
# the number of seconds, minutes, hours, and days since the epoch,
# in that order

seconds, minutes, hours, days = struct.unpack('4B', b'\xb1\x00\x00\x00')

# Convert the integers to a datetime object
dt = datetime.utcfromtimestamp(seconds + minutes * 60 + hours * 3600 + days * 86400)

print(dt)
