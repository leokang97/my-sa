#!/usr/bin/env python

# Python DBUS Test Server
# runs until the Quit() method is called via DBUS

from gi.repository import GLib
from pydbus import SessionBus
from pydbus.generic import signal

class AvnService(object):
    """
    <?xml version="1.0" encoding="UTF-8" ?>
    <node xmlns:doc="http://www.freedesktop.org/dbus/1.0/doc.dtd">

    <interface name="com.ssangyong.AutomotiveProxy.AudioManager">

    <method name="Get">
        <arg name="request" type="s" direction="in"/>
        <arg name="resp_result" type="b" direction="out"/>
        <arg name="resp_data" type="s" direction="out"/>
    </method>
    <method name="Set">
        <arg name="request" type="s" direction="in"/>
        <arg name="resp_result" type="b" direction="out"/>
        <arg name="resp_data" type="s" direction="out"/>
    </method>
    <method name="AddListener">
        <arg name="request" type="s" direction="in"/>
        <arg name="resp_result" type="b" direction="out"/>
        <arg name="resp_data" type="s" direction="out"/>
    </method>

    <signal name="UpdateInfo">
        <arg type="s" name="info"/>
    </signal>

    </interface>
    </node>
    """

    UpdateInfo = signal()

    def Get(self, s):
        print("com.ssangyong.AutomotiveProxy.AudioManager " + "Get : " + s)
        return (True, "{\"Data\":{\"Mute\":false,\"Volume\":1},\"Result\":{\"Message\":\"Success\",\"Status\":true}}")

    def Set(self, s):
        print("com.ssangyong.AutomotiveProxy.AudioManager " + "Set : " + s)
        return "Audio Manager - Set"

    def AddListener(self, s):
        print("com.ssangyong.AutomotiveProxy.AudioManager " + "AddListener : " + s)
        self.UpdateInfo("{\"Cmd\":123,\"Data\":{\"Action\":\"VrStartEvent123\"}}")
        return (True, "{\"Data\":null,\"Result\":{\"Message\":\"TEST Success\",\"Status\":true}}")

bus = SessionBus()
bus.publish("com.ssangyong.AutomotiveProxy",
    AvnService(),
    ("AudioManager", AvnService()))
loop = GLib.MainLoop()
loop.run()
