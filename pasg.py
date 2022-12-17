#!/usr/bin/python
# -*- coding: utf-8 -*-
import bluepy.btle as btle
import time


class ReadDelegate(btle.DefaultDelegate):

    def handleNotification(self, cHandle, data):
        print ('Aqui vai ter que ser Broker Client')
        print (data.decode('utf-8'))  # printing the data received from HM-11


p = btle.Peripheral('C4:49:51:F3:54:F0')  # change to address can be found using AT+ADDR?

s = p.getServiceByUUID('0000ffe0-0000-1000-8000-00805f9b34fb')  # mostly same for all modules
p.withDelegate(ReadDelegate())
c = s.getCharacteristics()[0]

    # only 20 bytes can be sent, 21+ will be split into a second packet.

c.write(bytes('h'))
while True:

    # if running HM-11 serialProxy program, then just wait for Hello world to be printed on the Arduino Serial Monitor
    # and then type anything on the serial and press enter will be printed in this terminal

    index = 0
    while p.waitForNotifications(1):  # wait for any incoming messages
        if index % 10 == 0:
            c.write(bytes('l'))
        elif index % 10 == 1:
            c.write(bytes('t'))
        elif index % 10 == 2:
            c.write(bytes('h'))
        elif index % 10 == 3:
            c.write(bytes('X'))
        index = index + 1
        time.sleep(1)
p.disconnect()
