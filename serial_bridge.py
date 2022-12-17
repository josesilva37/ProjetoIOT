#!/usr/bin/python
# -*- coding: utf-8 -*-
import bluepy.btle as btle


class ReadDelegate(btle.DefaultDelegate):

    def handleNotification(self, cHandle, data):
        print(data.decode('utf-8'))  # printing the data received from HM-11


p = btle.Peripheral('C4:49:51:F3:54:F0', btle.ADDR_TYPE_RANDOM)  # change to address can be found using AT+ADDR?

# s = p.getServiceByUUID('00001800-0000-1000-8000-00805f9b34fb')  # mostly same for all modules
s = p.getServiceByUUID('6e400003-b5a3-f393-e0a9-e50e24dcca9e')  # mostly same for all modules
# s = p.getServiceByUUID('00001801-0000-1000-8000-00805f9b34fb')  # mostly same for all modules
# s = p.getServiceByUUID('00001800-0000-1000-8000-00805f9b34fb')  # mostly same for all modules
# s = p.getServiceByUUID('0000180a-0000-1000-8000-00805f9b34fb')  # mostly same for all modules
# s = p.getServiceByUUID('6e400001-b5a3-f393-e0a9-e50e24dcca9e')  # mostly same for all modules
p.withDelegate(ReadDelegate())
c = s.getCharacteristics()[0]

# only 20 bytes can be sent, 21+ will be split into a second packet.
# c.write(bytes('Hello world\n', 'utf-8'))  # send message once to HM-11

while True:

    # if running HM-11 serialProxy program, then just wait for Hello world to be printed on the Arduino Serial Monitor
    # and then type anything on the serial and press enter will be printed in this terminal

    while p.waitForNotifications(1):  # wait for any incoming messages from HM-11
        c.write(bytes('t', 'utf-8'))

p.disconnect()
