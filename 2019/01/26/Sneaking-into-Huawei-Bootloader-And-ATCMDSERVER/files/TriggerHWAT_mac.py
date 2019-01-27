
"""

author 		: TwizzyIndy
date 		: last days from 2018
description : just to be triggered

"""

# hook huawei at on mac

import serial
import os

def serio(ser , istr , timeout = 0.5):  
    ser.timeout = timeout  
    istr=istr +"\r\n"  
    ser.write(istr)  
    ostr = ser.readall()  
    #print "send:%s\trecv:%s"%(repr(istr),repr(ostr))  
    return ostr  


ser = serial.Serial('/dev/cu.usbmodem14103', baudrate=115200)

print("\n\n\n----===========----\n\n")

print("Sending ^CHECKAUTHORITY .... \n\n")

ostr = serio(ser , 'AT^CHECKAUTHORITY')
seed = ostr.split("\r\n")[1]  
seed = seed[seed.index(":")+1:].strip()
print(" reply : " +  seed)

key = raw_input()

"""
print("Send again ^CHECKAUTHORITY ....\n\n")

ostr = serio(ser , 'AT^CHECKAUTHORITY')
seed = ostr.split("\r\n")[1]  
seed = seed[seed.index(":")+1:].strip()


print(" reply : " +  seed)
"""

#HookAtcmd.g_inputKey = seed
#HookAtcmd.main()


ser.close()

print("\n\n\n----===========----\n\n")