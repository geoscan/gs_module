#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from gs_interfaces.srv import Led,Live
from rospy import ServiceProxy
from std_msgs.msg import ColorRGBA

class BoardLedController():
    def __init__(self, namespace = ""):
        if namespace != "":
            namespace += "/"

        self.__leds = []
        for _ in range(0,4):
            self.__leds.append(ColorRGBA())

        self.__alive = ServiceProxy(f"{namespace}geoscan/alive",Live)
        self.__led_service = ServiceProxy(f"{namespace}geoscan/led/board/set",Led)

    def changeColor(self, i=0.0, r=0.0, g=0.0, b=0.0):
        if self.__alive().status:
            try:
                if ( ( (r >= 0.0) and (r <= 255.0) ) and ( (g >= 0.0) and (g <= 255.0) ) and ( (b >= 0.0) and (b <= 255.0) ) ):
                    color = ColorRGBA()
                    color.r = r
                    color.g = g
                    color.b = b
                    self.__leds[i] = color
                    return self.__led_service(self.__leds).status
                else:
                    rospy.logerr("Color value must be between 0.0 and 255.0 inclusive")
            except:
                rospy.logerr(f"Index led: {i} is not correct")
        else:
            rospy.logwarn("Wait, connecting to flight controller")
    
    def changeAllColor(self, r=0.0, g=0.0, b=0.0):
        if self.__alive().status:
            if ( ( (r >= 0.0) and (r <= 255.0) ) and ( (g >= 0.0) and (g <= 255.0) ) and ( (b >= 0.0) and (b <= 255.0) ) ):
                for i in range(0,len(self.__leds)):
                    color = ColorRGBA()
                    color.r = r
                    color.g = g
                    color.b = b
                    self.__leds[i] = color
                return self.__led_service(self.__leds).status
            else:
                rospy.logerr("Color value must be between 0.0 and 255.0 inclusive")
        else:
            rospy.logwarn("Wait, connecting to flight controller")

class ModuleLedController():
    def __init__(self, namespace = ""):
        if namespace != "":
            namespace += "/"

        self.__leds = []
        self.__leds.append(ColorRGBA())

        self.__alive = ServiceProxy(f"{namespace}geoscan/alive", Live)
        self.__led_service = ServiceProxy(f"{namespace}geoscan/led/module/set", Led)

    def changeColor(self, i=0.0, r=0.0, g=0.0, b=0.0):
        if self.__alive().status:
            try:
                if ( ( (r >= 0.0) and (r <= 255.0) ) and ( (g >= 0.0) and (g <= 255.0) ) and ( (b >= 0.0) and (b <= 255.0) ) ):
                    color = ColorRGBA()
                    color.r = r
                    color.g = g
                    color.b = b
                    self.__leds[i] = color
                    return self.__led_service(self.__leds).status
                else:
                    rospy.logerr("Color value must be between 0.0 and 255.0 inclusive")
            except:
                rospy.logerr(f"Index led: {i} is not correct")
        else:
            rospy.logwarn("Wait, connecting to flight controller")
    
    def changeAllColor(self, r=0.0, g=0.0, b=0.0):
        if self.__alive().status:
            if ( ( (r >= 0.0) and (r <= 255.0) ) and ( (g >= 0.0) and (g <= 255.0) ) and ( (b >= 0.0) and (b <= 255.0) ) ):
                color = ColorRGBA()
                color.r = r
                color.g = g
                color.b = b
                self.__leds[0] = color
                return self.__led_service(self.__leds).status
            else:
                rospy.logerr("Color value must be between 0.0 and 255.0 inclusive")
        else:
            rospy.logwarn("Wait, connecting to flight controller")