#!/usr/bin/python3

########################################################################################
# 	Domoticz Tuya Smart Plug Python Plugin                                             #
#                                                                                      #
# 	MIT License                                                                        #
#                                                                                      #
#	Copyright (c) 2018 tixi                                                            #
#                                                                                      #
#	Permission is hereby granted, free of charge, to any person obtaining a copy       #
#	of this software and associated documentation files (the "Software"), to deal      #
#	in the Software without restriction, including without limitation the rights       #
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell          #
#	copies of the Software, and to permit persons to whom the Software is              #
#	furnished to do so, subject to the following conditions:                           #
#                                                                                      #
#	The above copyright notice and this permission notice shall be included in all     #
#	copies or substantial portions of the Software.                                    #
#                                                                                      #
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR         #
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,           #
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE        #
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER             #
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,      #
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE      #
#	SOFTWARE.                                                                          #
#                                                                                      #
########################################################################################

import sys
import pytuya
import socket #needed for socket.timeout exception


ip        = "192.168.1.111"
devid     = "56870708840d8eb6b437"
localkey  = "9ce95916cf8e4ba0"
dps_value = 1

device    = pytuya.OutletDevice(devid,ip,localkey)

try:
        payload = device.generate_payload('set', {str(dps_value):False})
        device._send_receive(payload)

except (ConnectionResetError, socket.timeout, OSError)  as e:
        print("A problem occur please retry...")
        exit(1)