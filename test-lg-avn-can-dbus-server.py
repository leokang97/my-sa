#!/usr/bin/env python

# Python DBUS Test Server
# runs until the Quit() method is called via DBUS

from gi.repository import GLib
from pydbus import SessionBus
from pydbus.generic import signal

class LgAvnCanService(object):
    """
    <?xml version="1.0" encoding="UTF-8" ?>
    <node xmlns:doc="http://www.freedesktop.org/dbus/1.0/doc.dtd">

    <interface name="com.lge.car.micom.can">
        <method name="TriggerTest"/>

        <signal name="NotifyKeyFrontPannelEvent">
            <arg name="front" direction="out" type="ay"/>
        </signal>
    </interface>
    </node>
    """

    NotifyKeyFrontPannelEvent = signal()

    def TriggerTest(self):
        keyEvent = [0x16, 0x01]
        print("LG AVN Can DBus Server - method name: TriggerTest, key value: " + str(keyEvent[0]) + ", type1: " + str(keyEvent[1]))
        self.NotifyKeyFrontPannelEvent(keyEvent)
        pass

bus = SessionBus()
bus.publish("com.lge.car.micom",
    LgAvnCanService(),
    ("/Can", LgAvnCanService()))
loop = GLib.MainLoop()
loop.run()
