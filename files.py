#!/usr/local/bin/python3

from colorama import init
from colorama import Fore, Back, Style
import time
import cowsay
import sys
import os

def fileRead(path):
    file = open(path, 'r')
    return file.read()
    file.close()

def writeBssidFile(path, data):
    seconds = time.time()
    local = time.ctime(seconds)
    write = 'BSSID_MARCO\n' + local + '\nAdress: ' + data + '\nipconfig_set_BSSID\nEND'
    file = open(path, 'w')
    file.write(write)
    file.close()

def writeIpFile(path, data):
    seconds = time.time()
    local = time.ctime(seconds)
    write = 'IP_MARCO\n' + local + '\nIP_Adress: ' + data + '\nipconfig_set\nEND'
    file = open(path, 'w')
    file.write(write)
    file.close()

def writeNMaskFile(path, data):
    seconds = time.time()
    local = time.ctime(seconds)
    write = 'Network_Mask_MARCO\n' + local + '\nNetworkMask: ' + data + '\nipconfig_set_nwmask\nEND'
    file = open(path, 'w')
    file.write(write)
    file.close()

def get_datafile():
    dir = os.listdir('/var/tmp')

    dir_str = ''
    for i in dir:
        dir_str += i

    nullStart = dir_str.find('(null)')
    pcap = dir_str.find('pcap')

    filename = dir_str[nullStart:pcap + 4]

    print(filename)

