#!/usr/bin/env python

# Python DBUS Test Server
# runs until the Quit() method is called via DBUS

from gi.repository import GLib
from pydbus import SessionBus
from pydbus.generic import signal

class LgAvnAudioManagerService(object):
    """
    <?xml version="1.0" encoding="UTF-8" ?>
    <node xmlns:doc="http://www.freedesktop.org/dbus/1.0/doc.dtd">

    <interface name="org.genivi.audiomanager.commandinterface">
        <method name="Connect">
            <arg type="q" name="sourceID" direction="in"/>
            <arg type="q" name="sinkID" direction="in"/>
            <arg type="n" name="result" direction="out"/> <!-- method return code (am_Error_e) -->
            <arg type="q" name="mainConnectionID" direction="out"/>
        </method>
        <method name="Disconnect">
            <arg type="q" name="mainConnectionID" direction="in"/>
            <arg type="n" name="result" direction="out"/> <!-- method return code (am_Error_e) -->
        </method>

        <signal name="MainConnectionStateChanged">
            <arg type="q" name="connectionID" direction="out"/>
            <arg type="n" name="connectionState" direction="out"/>
        </signal>
        <signal name="SourceNotification">
            <arg type="q" name="sourceID" direction="out"/>
            <arg type="n" name="type" direction="out"/> <!-- am_notification_e type; int16_t value; -->
            <arg type="n" name="value" direction="out"/> <!-- am_notification_e type; int16_t value; -->
        </signal>
    </interface>
    </node>
    """

    MainConnectionStateChanged = signal()
    SourceNotification = signal()

    def Connect(self, sourceId, sinkId):
        print("LG AVN DBus Server - method name: Connect, sourceId: " + str(sourceId) + ", sinkId: " + str(sinkId))
        self.MainConnectionStateChanged(1, 1)
        self.SourceNotification(123, 0, 1)
        return (0, 1)

    def Disconnect(self, s):
        print("LG AVN DBus Server - method name: Disconnect" + ", parameters: " + s)
        return (0)

bus = SessionBus()
bus.publish("org.genivi.audiomanager",
    LgAvnAudioManagerService(),
    ("commandinterface", LgAvnAudioManagerService()))
loop = GLib.MainLoop()
loop.run()
