#!/usr/bin/env python

import scapy.all as scapy

def scan (ip):
    scapy.arping(ip)

scan("192.168.1.1/24")
#change the subnet according to your own network 
