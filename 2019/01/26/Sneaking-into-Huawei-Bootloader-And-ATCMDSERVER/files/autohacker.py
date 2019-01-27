import serial  
import time  
  
def calckey(seed):  
    pass  #这里不给出具体加密算法，鉴于合同原因，只给出思路  
  
def serio(ser , istr , timeout = 0.5):  
    ser.timeout = timeout  
    istr=istr +"\r\n"  
    ser.write(istr)  
    ostr = ser.readall()  
    print "send:%s\trecv:%s"%(repr(istr),repr(ostr))  
    return ostr  
      
ser = serial.Serial('com31',115200)  
#ostr = serio(ser , 'AT^LED')  
#ostr = serio(ser , '?')  
#ostr = serio(ser , 'AT^FBLOCK?')  
ostr = serio(ser , 'AT^MODEM=0')  
ostr = serio(ser , 'AT^CURC=0')  
ostr = serio(ser , 'AT^WVKEY?')  
ostr = serio(ser , 'AT^CHECKAUTHORITY=?')  
ostr = serio(ser , 'AT^CHECKAUTHORITY')  
seed = ostr.split("\r\n")[1]  
seed = seed[seed.index(":")+1:].strip()  
key = calckey(seed)  
#key = 'aa06c7b48dd42909926e8223f34aed30baea9bbe44926d818aa81464f5178150a66da672483cbab08a13cc7240d85066878c2a640c4cf26f3d8a8b6969d0a788304bab1dd567fe80bc6c1ca170eda312af3cb0089f12bdde014dd2a0d516526e8ac403a112ec81e20f3f692dc3d7abb590c2b312613422d6a734817310732125'  
ostr = serio(ser , 'AT^CONFORMAUTHORITY='+key)  
time.sleep(3000)  
""" 
ostr = serio(ser , 'AT^CURC=0') 
ostr = serio(ser , 'AT^SN?') 
ostr = serio(ser , 'AT^BSN?') #Serial NR 
ostr = serio(ser , 'AT^PHYNUM?')  
ostr = serio(ser , 'AT^ALLVER?') 
ostr = serio(ser , 'AT^FBLOCK?') 
ostr = serio(ser , 'AT^GETRAM?') 
ostr = serio(ser , 'AT^GETEMMC?') 
ostr = serio(ser , 'AT^WVKEY?') 
ostr = serio(ser , 'AT^VENDORCOUNTRY?') 
 
ostr = serio(ser , 'AT^MODEM=1') 
ostr = serio(ser , 'AT^MODEM=1') 
ostr = serio(ser , 'AT^CURC=0') 
ostr = serio(ser , 'AT^CURC=0') 
ostr = serio(ser , 'AT^PHYNUM?') 
ostr = serio(ser , 'AT^SIMLOCKDATAREAD?') 
ostr = serio(ser , 'AT^IDENTIFYSTART') 
"""  
ser.close() 